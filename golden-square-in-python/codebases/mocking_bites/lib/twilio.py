from twilio.rest import TwilioRestClient

# replace the placeholder strings in the following code line with 
# your Twilio Account SID and Auth Token from the Twilio Console
client = TwilioRestClient("ACxxxxxxxxxxxxxx", "zzzzzzzzzzzzz")

# change the "from_" number to your Twilio number and the "to" number
# to any phone number you want to send the message to 
client.messages.create(to="+19732644152", from_="+12023358536", 
                       body="Hello from Python!")