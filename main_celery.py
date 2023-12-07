import smtplib
import ssl
import time

from celery import Celery

app = Celery('hello', broker='pyamqp://guest@localhost/')

port = 465
smtplib_server = "smtp.gmail.com"
from_email = "najmiddinovavaz2208@gmail.com"
reciever_email = input("Email kiriting : ").split()
password = "whckoljcgseigqxs "
message = "Hello guys !!!"


@app.task
def hello():
    for i in reciever_email:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtplib_server, port, context=context) as server:
            server.login(from_email, password)
            time.sleep(10)
            return server.sendmail(from_email, i, message)
