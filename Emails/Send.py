# NOTE: Before sending an email PLS Make sure you have set up APP password for Gmail account

import smtplib
import getpass

smtp_object = smtplib.SMTP('smtp.gmail.com',587)
smtp_object.ehlo()
smtp_object.starttls()

email = input("Email: ")
password = getpass.getpass("Password: ")
print(smtp_object.login(email,password))

from_address = email
to_address = input("Send to whom: ")
subject = input("Give a title to your text: ")
message = input("Type your full message here: ")
msg = "Subject: "+subject + "\n" + message

smtp_object.sendmail(from_address,to_address,msg)
