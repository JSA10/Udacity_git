from twilio.rest import TwilioRestClient
# can also use >  from twilio import rest
# then would need to change client entry below to > client = rest.TwilioRestClient(etc)

account_sid = "ACb2d5623987439fe5e5877be8028ef364" # Your Account SID from www.twilio.com/console
auth_token  = "e4ea72217b6673565e01a2178343332c"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Sex Panther; 60 % of the time, works every time",
    to="+447815121684",    # Replace with your phone number
    from_="+441368908033") # Replace with your Twilio number

print(message.sid)
## this code works in the terminal where twilio was installed - not in IDLE
# run file using - python send_text.py
