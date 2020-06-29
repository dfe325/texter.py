#! python3

#https://askubuntu.com/questions/408611/how-to-remove-or-delete-single-cron-job-using-linux-command
#15 5 * * 3 cd Desktop && /Library/Frameworks/Python.framework/Versions/3.8/bin/python3 texter.py >> test.out

accountSID = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
authToken =  'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
H_Number = 'XXXXXXXXXXX'
D_Number = 'XXXXXXXXXXX'

from twilio.rest import Client

twilioNumber = 'XXXXXXXXXXX'

def text_H(message):
    twilioCli = Client(accountSID, authToken)
    twilioCli.messages.create(body=message, from_=twilioNumber, to=H_Number)

def text_D(message):
    twilioCli = Client(accountSID, authToken)
    twilioCli.messages.create(body=message, from_=twilioNumber, to=D_Number)

#text_H("TAKE OUT THE COMPOST TOMORROW.")
text_D("TAKE OUT THE COMPOST TOMORROW.")

print("Message sent.")
