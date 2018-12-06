""" emailに添付ファイルをつけてoutlookに送信 """
from email.mime import multipart
from email.mime import text
import smtplib

smtp_host = 'smtp.live.com'
smtp_port = 587
from_email = 'your_email@outlook.jp'
to_email = 'your_email@outlook.jp'
username = 'your_email@outlook.jp'
password = 'your_password'

msg = multipart.MIMEMultipart()
msg['Subject'] = 'Test email sub'
msg['From'] = from_email
msg['To'] = to_email
msg.attach(text.MIMEText('Test email', 'plain'))

with open('email2.py', 'r') as f:
    attachment = text.MIMEText(f.read(), 'plain')
    attachment.add_header(
        'Content-Disposition', 'attachment', filename='lesson.txt'
    )
    msg.attach(attachment)

server = smtplib.SMTP(smtp_host, smtp_port)
server.ehlo() # serverに問い合わせる
server.starttls()
server.ehlo()
server.login(username, password)
server.send_message(msg)
server.quit()
