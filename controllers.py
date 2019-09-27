import smtplib 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# smtp server setup happens here
s = smtplib.SMTP(host='smtp.gmail.com', port=587)
s.starttls()
s.login('servicedesk.transcend@gmail.com', 'Alupo.Agatha&Edmond@2019')

def checkSend(variable):
    # msg composition happens here
    message = variable
    msg = MIMEMultipart()

    msg['From']='servicedesk.transcend@gmail.com'
    msg['To']= 'codespeisdocs@gmail.com'
    msg['Subject']= "BackUp mailing Function"

    msg.attach(MIMEText(message, 'plain'))
    try:
        s.send_message(msg)
        return ('Message sent')
    except Exception as expt:
        return (expt)

    del msg