import smtplib
import ssl


#sending email function
def smail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("your-mail@gmail.com", "jarvisvision")
    server.sendmail("jarvis.your-mail@gmail.com", to, content)
    server.close()






