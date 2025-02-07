import json

import requests



def send_sms(phone_number, message):
    api_url = "https://api.softleek.com/sms/send"
    max_length = 200  # Maximum length of each message part

    # Split the message into multiple parts if necessary
    def split_message(message, max_length):
        parts = []
        while len(message) > max_length:
            # Find the last space within the limit
            split_index = message.rfind(' ', 0, max_length)
            if split_index == -1:  # No space found, forcefully split
                split_index = max_length
            parts.append(message[:split_index])
            message = message[split_index:].strip()  # Remove leading spaces for the next part
        parts.append(message)  # Add the last remaining part
        return parts

    message_parts = split_message(message, max_length)

    # Send each part of the message
    for part in message_parts:
        payload = {"phone": phone_number, "message": part, "sender_id": "SOFTLEEK"}
        json_payload = json.dumps(payload)
        headers = {"Content-Type": "application/json", "Accept": "application/json"}

        response = requests.post(api_url, data=json_payload, headers=headers)

        if response.status_code != 200:
            try:
                response_data = response.json()
            except ValueError:
                response_data = response.text

            raise Exception(
                f"Failed to send SMS. Status code: {response.status_code}, Response: {response_data}"
            )

