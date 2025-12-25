import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os

load_dotenv()

SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv("SMTP_PORT", 0))
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")


def send_email(recipient, subject, body):
    try:
        # Validate environment variables
        if not all([SMTP_SERVER, SMTP_PORT, SENDER_EMAIL, EMAIL_PASSWORD]):
            return False, "SMTP environment variables not set properly"

        # Compose email
        message = MIMEMultipart()
        message["From"] = SENDER_EMAIL
        message["To"] = recipient
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))

        # ✅ Use SMTP SSL (NO starttls)
        server = smtplib.SMTP_SSL(
            SMTP_SERVER,
            SMTP_PORT,
            timeout=30
        )
        server.login(SENDER_EMAIL, EMAIL_PASSWORD)
        server.sendmail(SENDER_EMAIL, recipient, message.as_string())
        server.quit()

        return True, "Sent Successfully"

    except Exception as e:
        return False, f"Unable to send mail: {e}"
