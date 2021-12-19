# SMTP - Simple Mail Transfer Protocol
import smtplib
my_email = "EmailYouWantToSendEmailFrom"
my_pass = "YourPassword"

connection = smtplib.SMTP("smtp.gmail.com", port=587)

connection.starttls() # encryption

connection.login(user=my_email, password=my_pass)

connection.sendmail(
    from_addr=my_email,
    to_addrs="EmailYouWantToSendEmailTO",
    msg="Subject: Hey, How yu doinn?n \n\nHey, It's Joey here.")

