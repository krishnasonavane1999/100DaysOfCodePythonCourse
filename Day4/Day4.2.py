# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random

total_persons = len(names)

person_index = random.randint(0, total_persons - 1)

print(person_index)
print(f"{names[person_index]} is going to buy the meal today!")



