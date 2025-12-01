import smtplib
import ssl


def send_email(message):
    host = 'smtp.gmail.com'
    port = 465
    user_name = "private.1984@gmail.com"
    password = "vgdzqjkmngawbldm"
    reciever = "private.1984@gmail.com"

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(user_name, password)
        server.sendmail(user_name, reciever, message)
