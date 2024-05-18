import smtplib
from email.message import EmailMessage
def sendmail(to,subject,body):
    server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login('214209p@pbsiddhartha.ac.in','rwhu bnoy dzdf tfax')
    msg=EmailMessage()
    msg['FROM']='your email'
    msg['TO']=to
    msg['SUBJECT']=subject
    msg.set_content(body)
    server.send_message(msg)
    server.close()
    