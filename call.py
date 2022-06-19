# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client

contacts = {'krishna':"+919000683024", 'jyothi':"+919949418372"}
# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACc7df3cbbd2bf9a13174217041dc2a196'
auth_token = '0e0586de7930abf31ac7e2b3bd397c08'
client = Client(account_sid, auth_token)

call = client.calls.create(
                        twiml='<Response><Say>Ahoy, World!</Say></Response>',
                        to=contacts['krishna'],
                        from_='+12067361389'
                    )

print(call.sid)
