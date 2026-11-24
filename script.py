
import os
import smtplib
from pathlib import Path
from email.message import EmailMessage
from dotenv import load_dotenv

# Load environment variables
base_dir = Path(__file__).parent
load_dotenv(base_dir / ".env")

sender = os.getenv("EMAIL_ADDRESS")
password = os.getenv("EMAIL_PASSWORD")
smtp_server = os.getenv("SMTP_SERVER", "smtp.gmail.com")
smtp_port = int(os.getenv("SMTP_PORT", "465"))

print(sender)
print(password)
# Validate configuration
if not sender or not password:
    raise ValueError("Email credentials missing in .env file")

# Read recipients
with open(base_dir / "emails.txt", "r") as file:
    recipients = [
        line.strip()
        for line in file
        if line.strip()
    ]

# Read plain text template
email_body = (base_dir / "email_template.txt").read_text(
    encoding="utf-8"
)

print(email_body)

subject = "Introduction from Our Company"

# Send emails
with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:

    server.login(sender, password)

    for recipient in recipients:
        try:
            msg = EmailMessage()
            msg["Subject"] = subject
            msg["From"] = sender
            msg["To"] = recipient

            msg.set_content(email_body)

            server.send_message(msg)

            print(f"Email sent to: {recipient}")

        except Exception as e:
            print(f"Failed: {recipient} - {e}")

print("Email processing completed!")
