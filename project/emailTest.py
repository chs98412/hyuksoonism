import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication

email_add=input()
recipients = [email_add]

message = MIMEMultipart()
message['Subject'] = 'hyuksoonism'
message['From'] = "cs_7410@naver.com"
message['To'] = ",".join(recipients)

content = """
    <html>
    <body>
        <h2>{title}</h2>
    <p>{add}</p>
    </body>
    </html>
""".format(
title = 'hyuksoonism',
add='http://192.168.35.165:8000/api/project/'+email_add+'/'
)

mimetext = MIMEText(content,'html')
message.attach(mimetext)

email_id = 'cs_7410'
email_pw = 'us7530'

server = smtplib.SMTP('smtp.naver.com',587)
server.ehlo()
server.starttls()
server.login(email_id,email_pw)
server.sendmail(message['From'],recipients,message.as_string())
server.quit()