from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'ACCOUNTID'
# auth_token = 'your_auth_token'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Man, I am super tired right now.",
                     from_='+1234568900',
                     to='+10098765432'
                 )

print(message.sid)