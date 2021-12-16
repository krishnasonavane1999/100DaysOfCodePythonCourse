try:
	with open("demoFile.txt", "w") as file:
		file.write("Hello")

	#type error
	name = "krishna"
	name += "ddd"

	#keyerror
	data = {"key": 10}

	# keyerror
	print(data["key"])

	# index error
	name = [1, 2, 3]
	print(name[4])

except FileNotFoundError as error_message:
	with open("demoFile.txt", "w") as file:
		file.write("Hello")

except TypeError as error_message:
	print(error_message)

except IndexError as error_message:
	print(error_message)

except KeyError as error_message:
	print(error_message)
else:
	print("Something")

finally:
	# no matter what this will run
	file.close()
	print("File closed")