import smtplib#protocol of communication for emails
from email.message import EmailMessage
email=EmailMessage()
email['from']='Rojan Upreti'
email['to']='pnirajan.np@gmail.com'
email['subject']='You won 2 rs'

email.set_content('I am Rojan Upreti')
with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login('rojanupreti99@gmail.com','')
	smtp.send_message(email)
	print('All good roja')


import smtplib
from email.message import EmailMessage
from string import Template


from pathlib import Path
html=Template(Path('index.html').read_text())
email=EmailMessage()
email['from']='Rojan Upreti'
email['to']='pnirajan.np@gmail.com'
email['subject']='you won rs. 2'

email.set_content(html.substitute ({'name'='Tintin'}),'html')
