#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

# greeting
print("Welcome to The Tip Calculator")
print("-----------------------------")

#Input total bill amount
total_bill = input("Enter total bill amount $")

#input tip percentage
tip_percentage = input("Enter what tip percentage you want to give 10, 12, 15, 20? ")

# Input total people
total_people = input("How many people are there? ")

# calculate tip percentage according to total bill
tip_percentag_amount = ((int(total_bill) * int(tip_percentage)) / 100);

# add tip percenatage to original bill
final_bill = tip_percentag_amount + int(total_bill)

# divide final bill(after adding tp percentage) by total people
individual_bill_amount = round((int(final_bill) / int(total_people)), 2)

# give the final output to the user
print(f"Each person should pay $ {individual_bill_amount}")