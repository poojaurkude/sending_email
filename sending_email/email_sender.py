import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Path('index.html')
email = EmailMessage()
email['from'] = 'Pooja Urkude'
email['to'] = 'Pooja11urkude@gmail.com'
email['subject'] = 'You won 1,000,000 dollars!'

email.set_content(html.substitute({'name': 'TinTin'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('poojaurkude11@gmail.com', 'password')
    smtp.send_message(email)
    print('all good boss!')