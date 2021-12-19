import random
import smtplib
import datetime as dt
my_email = "EmailYouWantToSendEmailFrom"
my_pass = "YourPassWord"

with open("quotes.txt", "r") as quotes_data:
    data = quotes_data.read()
    quotes_list = data.split('\n')

random_quote = random.randint(0, 3)

connection = smtplib.SMTP("smtp.gmail.com", port=587)

connection.starttls() # encryption

connection.login(user=my_email, password=my_pass)

now = dt.datetime.now()

day = now.weekday()

connection.sendmail(
    from_addr=my_email,
    to_addrs="EmailYouWantToSendEmailTO",
    msg=f"Subject: Monday Motivation - Don't hate Mondays \n\n {quotes_list[random_quote]} {quotes_list[random_quote]}")
