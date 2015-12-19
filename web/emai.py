#-*- encoding: utf-8 -*-
import os, sys
import smtplib
from smtplib import SMTP_SSL
from email.header import Header
from email.mime.text import MIMEText
 
mailInfo = {
    "from": "xxx@qq.com",
    "to": "yyy@163.com",
    "hostname": "smtp.qq.com",
    "username": "2013986@qq.com",
    "password": "8561312t",
    "mailsubject": "this is test",
    "mailtext": "hello, this is send mail test.",
    "mailencoding": "utf-8"
}
         
if __name__ == '__main__':
    smtp = SMTP_SSL(mailInfo["hostname"])
    smtp.set_debuglevel(1)
    smtp.ehlo(mailInfo["hostname"])
    smtp.login(mailInfo["username"],mailInfo["password"])
     
    msg = MIMEText(mailInfo["mailtext"],"text",mailInfo["mailencoding"])
    msg["Subject"] = Header(mailInfo["mailsubject"],mailInfo["mailencoding"])
    msg["from"] = mailInfo["from"]
    msg["to"] = mailInfo["to"]
    smtp.sendmail(mailInfo["from"], mailInfo["to"], msg.as_string())
     
    smtp.quit()
