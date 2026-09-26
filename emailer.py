import base64
import logging
import os
from datetime import date
from email.message import EmailMessage
from html import escape
from pathlib import Path

from google.auth.exceptions import RefreshError
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

from storage import split_jobs

logger = logging.getLogger(__name__)
README_URL = "https://github.com/Aneel-Badesha/JobBot#current-jobs"

SCOPES = ["https://www.googleapis.com/auth/gmail.send"]
_CREDS_DIR = Path.home() / ".config" / "financialbot"


def _get_service():
    token_path = _CREDS_DIR / "token.json"
    if not token_path.exists():
        raise RuntimeError(
            f"No token found at {token_path}. Run: python -m financialbot.auth  "
            f"(or call emailer._run_consent() interactively) to authorize."
        )
    creds = Credentials.from_authorized_user_file(str(token_path), SCOPES)
    if not creds.valid:
        if creds.refresh_token:
            creds.refresh(Request())
            token_path.write_text(creds.to_json(), encoding="utf-8")
        else:
            raise RuntimeError(
                f"Token at {token_path} has no refresh_token and cannot be renewed headlessly. "
                f"Delete {token_path} and re-run the interactive auth flow."
            )
    return build("gmail", "v1", credentials=creds)


def _run_consent(token_path: Path) -> Credentials:
    flow = InstalledAppFlow.from_client_secrets_file(str(_CREDS_DIR / "credentials.json"), SCOPES)
    flow.redirect_uri = "urn:ietf:wg:oauth:2.0:oob"
    auth_url, _ = flow.authorization_url(prompt="consent")
    print(f"\nAuthorize the app:\n{auth_url}\n")
    code = input("Enter the authorization code: ")
    flow.fetch_token(code=code)
    creds = flow.credentials
    token_path.write_text(creds.to_json(), encoding="utf-8")
    return creds


def send_digest(jobs: list[dict]) -> None:
    recipient = os.environ.get("RECIPIENT_EMAIL", "")
    if not recipient:
        raise ValueError("RECIPIENT_EMAIL not set in environment")

    msg = EmailMessage()
    msg["Subject"] = f"Hardware Jobs Digest — {date.today().isoformat()} ({len(jobs)} new)"
    msg["To"] = recipient
    msg.set_content(_build_plain(jobs))
    msg.add_alternative(_build_html(jobs), subtype="html")

    service = _get_service()
    raw = base64.urlsafe_b64encode(msg.as_bytes()).decode()
    result = service.users().messages().send(userId="me", body={"raw": raw}).execute()
    logger.info(f"Sent digest with {len(jobs)} jobs to {recipient} (id={result.get('id')})")


def _build_plain(jobs: list[dict]) -> str:
    interns, full_time = split_jobs(jobs)
    lines = [f"New hardware/embedded jobs — {date.today().isoformat()} ({len(jobs)} new)", ""]
    for heading, rows in ((f"Internships & Co-ops ({len(interns)})", interns),
                          (f"Full-time ({len(full_time)})", full_time)):
        lines += [heading, "-" * len(heading)]
        if not rows:
            lines.append("None today.")
        for j in rows:
            lines.append(f"{j.get('posted', '')} | {j['company']} | {j['title']} | {j['location']}")
            lines.append(f"  {j['link']}")
        lines.append("")
    lines.append(f"All current jobs: {README_URL}")
    return "\n".join(lines)


_CELL = "padding:8px;border-bottom:1px solid #eee;vertical-align:top"


def _html_table(rows: list[dict]) -> str:
    if not rows:
        return '<p style="color:#888"><em>None today.</em></p>'
    body = "".join(f"""
      <tr>
        <td style="{_CELL};color:#888;white-space:nowrap">{escape(j.get('posted', ''))}</td>
        <td style="{_CELL};font-weight:bold;color:#0f766e">{escape(j['company'])}</td>
        <td style="{_CELL}"><a href="{escape(j['link'], quote=True)}" style="color:#1a0dab;text-decoration:none">{escape(j['title'])}</a></td>
        <td style="{_CELL};color:#555">{escape(j['location'])}</td>
      </tr>""" for j in rows)
    return f"""<table style="width:100%;border-collapse:collapse">
    <thead>
      <tr style="background:#f5f5f5">
        <th style="padding:8px;text-align:left">Posted</th>
        <th style="padding:8px;text-align:left">Company</th>
        <th style="padding:8px;text-align:left">Role</th>
        <th style="padding:8px;text-align:left">Location</th>
      </tr>
    </thead>
    <tbody>{body}
    </tbody>
  </table>"""


def _build_html(jobs: list[dict]) -> str:
    interns, full_time = split_jobs(jobs)
    return f"""<!DOCTYPE html>
<html>
<body style="font-family:Arial,sans-serif;color:#333;max-width:800px;margin:auto">
  <h2 style="border-bottom:2px solid #0f766e;padding-bottom:8px">
    New Hardware Jobs
    <span style="font-size:14px;color:#666;font-weight:normal">— {date.today().isoformat()}</span>
  </h2>
  <p>{len(jobs)} new posting(s) added today.</p>
  <h3>Internships &amp; Co-ops ({len(interns)})</h3>
  {_html_table(interns)}
  <h3 style="margin-top:28px">Full-time ({len(full_time)})</h3>
  {_html_table(full_time)}
  <p style="color:#888;font-size:12px;margin-top:24px">
    Automated digest from FinancialBot. Jobs filtered for Toronto/Montreal/Ottawa/Vancouver + firmware/embedded/systems keywords, posted in the last 14 days.<br>
    <a href="{README_URL}" style="color:#1a0dab">View all current jobs →</a>
  </p>
</body>
</html>"""
