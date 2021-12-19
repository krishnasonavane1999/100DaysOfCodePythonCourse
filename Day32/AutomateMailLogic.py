##################### Normal Starting Project ######################
import random
import smtplib
import datetime as dt
import pandas as pd

# below code nd refactring - just written for demo purpose
receiver_details = pd.read_csv('birthdays.csv')
receivers_name = receiver_details["name"].to_list()
receivers_email = receiver_details["email"].to_list()
receivers_day = receiver_details["day"].to_list()
receivers_month = receiver_details["month"].to_list()

details_about_date = dt.datetime.now()

#
curent_day = details_about_date.day
current_month = details_about_date.month

def send_mail(letter):
    my_email = "EmailYouWantToSendemailFrom"
    my_pass = "Your Pass"

    connection = smtplib.SMTP("smtp.gmail.com", port=587)

    connection.starttls()  # encryption

    connection.login(user=my_email, password=my_pass)

    message_content = f"Subject: Wish You very happy birthday buddy\n\n{letter}"
    connection.sendmail(
        from_addr=my_email,
        to_addrs="EmailYouWantToSendEmailTO",
        msg=message_content)

    print("Letter Sent")


def wish_happy_birthday(birthday_person):
    letter_num = random.randint(0, 3)
    with open(f"letter_templates/letter_{letter_num}.txt") as letter:
        letter_content = letter.read()
        prepared_letter = letter_content.replace("[NAME]", birthday_person)
        send_mail(prepared_letter, )

for count in range(0, len(receivers_day) - 1):
    if receivers_day[count] == curent_day and receivers_month[count] == current_month:
        wish_happy_birthday(receivers_name[count])

