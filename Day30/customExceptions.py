number = int(input("Enter divisor: "))

try:
	if number == 0:
		raise ValueError("You cannnot divide number zero")

except:
	print("I think you are trying to  divide number by zero")

else:
	print(10 / number)
	