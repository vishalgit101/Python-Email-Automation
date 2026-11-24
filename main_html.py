
import os
import smtplib
from pathlib import Path
from email.message import EmailMessage
from dotenv import load_dotenv

# Load .env
base_dir = Path(__file__).parent
load_dotenv(base_dir / ".env")

sender = os.getenv("EMAIL_ADDRESS")
password = os.getenv("EMAIL_PASSWORD")
smtp_server = os.getenv("SMTP_SERVER", "smtp.gmail.com")
smtp_port = int(os.getenv("SMTP_PORT", "465"))

if not sender or not password:
    raise ValueError("Email credentials missing in .env")

# Read recipients
with open(base_dir / "emails.txt", "r") as file:
    recipients = [
        line.strip()
        for line in file
        if line.strip()
    ]

# Read HTML template
html_body = (base_dir / "business_template.html").read_text(
    encoding="utf-8"
)

plain_body = """
Hello,

We are pleased to introduce our company
and the professional services we offer.

Best Regards,
Your Company Team
"""

subject = "Business Introduction - Your Company"

# SMTP connection
with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:

    server.login(sender, password)

    for recipient in recipients:
        try:
            msg = EmailMessage()

            msg["Subject"] = subject
            msg["From"] = sender
            msg["To"] = recipient

            msg.set_content(plain_body)
            msg.add_alternative(html_body, subtype="html")

            server.send_message(msg)

            print(f"HTML email sent to: {recipient}")

        except Exception as e:
            print(f"Failed: {recipient} - {e}")

print("HTML email processing completed!")
