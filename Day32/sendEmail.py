import smtplib

my_mail = "krishnasonavane8@gmail.com"
my_password = "Greatest"
# connection = smtplib.SMTP("smtp.gmail.com")
# connection.starttls()

# connection.login(user=my_mail, password=my_password)

# connection.sendmail(from_add=my_mail, to_add="nitasonavane8@gmail.com", msg="Subject: Hey, What's up? Hi This is Krishna Sonavane. Just checking out")
# connection.close()

with smtplib.SMTP("smtp.gmail.com") as connection:
	connection.starttls()
	connection.login(user=my_mail, password=my_password)
	connection.sendmail(
		from_add=my_mail,
		to_add="nitasonavane8@gmail.com", 
		msg="Subject: Hey, What's up? \n\nHi This is Krishna Sonavane. Just checking out")
	connection.close()