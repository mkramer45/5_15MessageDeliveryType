# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'AC9b35d0f731d55b40837d58c7029f1c9e'
auth_token = '8ea852ad93611021ab3ac94f6dff6606'
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body="Eskettttit",
                              from_="+18572144683",
                              to="+17812648275"
                          )

print(message.sid)


# this script is straightforward, send body to explicit number from explicit number
# moving forward, we need to do the following logic:
# 	-- funny texts --
#	-- body_funny = random msg from funny table
#	-- to_funny = users who have RadioB = 'Funny'

