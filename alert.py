import os
import smtplib
import requests
from email.message import EmailMessage
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Correct env variable names
TG_TOKEN = os.getenv("TELEGRAM_TOKEN")
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")


def send_alert(contacts, message):
    print("🔥 send_alert CALLED")
    print("CONTACTS:", contacts)

    for c in contacts:
        _, name, phone, telegram_id, email = c

        print(f"Processing: {name} {telegram_id} {email}")

        # Telegram
        if telegram_id:
            print("📨 Attempting Telegram send to:", telegram_id)
            res = requests.post(
                f"https://api.telegram.org/bot{TG_TOKEN}/sendMessage",
                data={"chat_id": telegram_id, "text": message}
            )
            print("Telegram HTTP status:", res.status_code)
            print("Telegram response:", res.text)

        # Email
        if email:
            try:
                print("📧 Attempting Email send to:", email)
                msg = EmailMessage()
                msg["Subject"] = "🚨 SOS ALERT 🚨"
                msg["From"] = EMAIL_ADDRESS
                msg["To"] = email
                msg.set_content(message)

                with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
                    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                    smtp.send_message(msg)

                print("Email sent OK")
            except Exception as e:
                print("Email failed:", e)
