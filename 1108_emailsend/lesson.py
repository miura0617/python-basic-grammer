from email import message
import smtplib

import config

smtp_host = 'smtp.live.com'
smtp_port = 587

from_email = 'xxx@hotmail.com'
from_email = config.from_email
to_email = 'xxx@hotmail.com'
to_email = config.to_email
username = 'xxx@hotmail.com'
username = config.username
password = 'fasefasfasdfa'
password = config.password

msg = message.EmailMessage()
msg.set_content('test email') # emailの内容
msg['Subject'] = 7Test email Subject'
msg['From'] = from_email
msg['To'] = to_email

server = smtplib.SMTP(smtp_host, smtp_port)
server.ehlo() # 今からSMTPと会話する事前おまじない
server.starttls()
server.ehlo()
server.login(username, password)
server.send_message(msg)
server.quit()

