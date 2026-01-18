import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
FROM_NUMBER = os.getenv("TWILIO_FROM_NUMBER")

client = Client(ACCOUNT_SID, AUTH_TOKEN)

def send_alert(phones, maps_link):
    for phone in phones:
        client.messages.create(
            body=(
                "🚨 EMERGENCY ALERT 🚨\n"
                "They might be in danger.\n"
                f"Live location: {maps_link}"
            ),
            from_=FROM_NUMBER,
            to=phone
        )
