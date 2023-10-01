from koodoLogin import get_text_content
from send_message import send_message

def lambda_handler(event, context):
    # Retrieve the text_content from the webpage
    text_content, days_content = get_text_content()

    # Send the message
    send_message(text_content, days_content)

    # Return a response (opztional)
    return {
        'statusCode': 200,
        'body': 'Data successfully scraped and sent'
    }
