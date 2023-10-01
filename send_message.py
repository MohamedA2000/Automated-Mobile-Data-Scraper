from twilio.rest import Client
import os

def send_message(text_content,days_content):
    # Your Twilio account SID and auth token
    account_sid = os.environ.get('twilioAccountSID')
    auth_token = os.environ.get('twilioAuthToken')

    # Create a Twilio client
    client = Client(account_sid, auth_token)

    # The phone number to send the message from (provided by Twilio)
    twilio_number = os.environ.get('twilioNum')

    # The phone number to send the message to
    recipient_number = os.environ.get('myNum')

    # Construct the message content
    message_content = f"Hello, your data usage is at {text_content}/20 GB. You have {days_content}. Remember, it resets on the 29th of every month! habla"

    # Send the message using Twilio
    message = client.messages.create(
        body=message_content,
        from_=twilio_number,
        to=recipient_number
    )

    # Print the message SID
    print("Message sent. SID:", message.sid)
