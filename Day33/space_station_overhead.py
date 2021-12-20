import requests
import datetime 
import smtplib
MY_LAT = 18.520430
MY_LONG = 73.856743

def is_iss_on_my_head():
	response = requests.get("http://api.open-notify.org/iss-now.json")

	response.raise_for_status()

	data = response.json()

	iss_latitude = data["iss_position"]["latitude"]
	iss_longitude = data["iss_position"]["longitude"]

	iss_position = (longitude, latitude)

	# if your position is -5 or +5 degree of the iss position
	if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 or  MY_LONG - 5 <= iss_latitude <= MY_LONG + 5:
		return True


def is_night_time():

	parameters = {
		"lat": MY_LAT,
		"lng": MY_LONG,
		"formatted": 0
	}

	response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
	response.raise_for_status()

	data = response.json()



	sunrise = int(data["results"]["sunrise"].split('T')[1].split(':')[0])
	sunset = int(data["results"]["sunset"].split('T')[1].split(':')[0])

	current_time = datetime.datetime.now().hour
	
	if current_time >= sunset or current_time <= sunrise:
		return True

# keep this function running by using while loop and time frame
def notify_me_to_look_up():
	if is_iss_on_my_head() and is_night_time():
		# send mail
		import smtplib

	my_mail = "EmailYouWantToSendFrom"
	my_password = "YourPassWord"

	with smtplib.SMTP("smtp.gmail.com") as connection:
		connection.starttls()
		connection.login(user=my_mail, password=my_password)
		connection.sendmail(
			from_add=my_mail,
			to_add="EmailYouWantToSendTo", 
			msg="Subject: Hey, Look in the sky \n\nInternational Space Station is on your head now. Try to find it.")
		connection.close()




# if iss is overhead and it's officialy night time then it's time to loop up
notify_me_to_look_up()