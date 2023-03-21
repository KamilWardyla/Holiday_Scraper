from twilio.rest import Client
from localsettings import account_SID_settings, auth_token_settings


def sms_sender(text, link):
    account_SID = account_SID_settings
    auth_token = auth_token_settings
    twilio_client = Client(account_SID, auth_token)

    message = twilio_client.messages.create(
        to="+48534990089",
        from_='+17579749883',
        body=f'Text: {text} , Link: {link}')

    print(message.sid)
