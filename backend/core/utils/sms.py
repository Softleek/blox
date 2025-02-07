
import json
import logging

import requests
# from core.models import Reminder

logger = logging.getLogger(__name__)



def send_sms(phone_number, message):
    api_url = "https://api.softleek.com/sms/send"
    payload = {"phone": phone_number, "message": message, "sender_id": "SOFTLEEK"}
    json_payload = json.dumps(payload)
    headers = {"Content-Type": "application/json", "Accept": "application/json"}

    response = requests.post(api_url, data=json_payload, headers=headers)
    if response.status_code == 200:
        logger.info(f"SMS sent successfully to {phone_number}")
    else:
        logger.error(f"Failed to send SMS to {phone_number}. Response: {response.text}")
