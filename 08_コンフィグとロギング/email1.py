""" pythonでoutlook当てに, emaliを送信する方法 """
from email import message
import smtplib

smtp_host = 'smtp.live.com'
smtp_port = 587
from_email = 'your_email@outlook.jp'
to_email = 'your_email@outlook.jp'
username = 'your_email@outlook.jp'
password = 'your_email_password'

msg = message.EmailMessage()
msg.set_content('Test email')
msg['Subject'] = 'Test email sub'
msg['From'] = from_email
msg['To'] = to_email

server = smtplib.SMTP(smtp_host, smtp_port)
server.ehlo() # serverに問い合わせる
server.starttls()
server.ehlo()
server.login(username, password)
server.send_message(msg)
server.quit()
