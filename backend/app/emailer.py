import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import List
import os

def send_email(subject: str, body: str, recipients: List[str]):
    sender = os.getenv('EMAIL_SENDER', 'noreply@competiscan.com')
    smtp_server = os.getenv('SMTP_SERVER', 'localhost')
    smtp_port = int(os.getenv('SMTP_PORT', 25))
    smtp_user = os.getenv('SMTP_USER', '')
    smtp_pass = os.getenv('SMTP_PASS', '')

    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            if smtp_user and smtp_pass:
                server.starttls()
                server.login(smtp_user, smtp_pass)
            server.sendmail(sender, recipients, msg.as_string())
        return True
    except Exception as e:
        print(f"Email send failed: {e}")
        return False
