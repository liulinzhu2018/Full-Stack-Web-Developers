from twilio.rest import TwilioRestClient
# TwilioRestClient ��twilio.rest �����class, ����ֱ��ʹ��TwilioRestClient
# from twilio import rest -->   rest.TwilioRestClient()


# Your Account SID from twilio.com/console
account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
# Your Auth Token from twilio.com/console
auth_token  = "your_auth_token"

client = TwilioRestClient(account_sid, auth_token)
message = client.sms.message.create(
    body = "xxx",
    to = "123",
    from_="23"
)

print(message.sid)
