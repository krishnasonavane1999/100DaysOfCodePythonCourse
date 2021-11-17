# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = round((weight) / (height * height))

if bmi < 18.5:
  print(f"Your BMI is {bmi}. You are Underweight")

elif bmi < 25:
      print(f"Your BMI is {bmi}. You have normal bmi")

elif bmi < 30:
  print(f" Your BMI is {bmi} You are slightly overweight")

elif bmi < 35:
  print(f"Your BMI is {bmi}. You are Obese")

else:
  print(f"Your BMI is {bmi}. You are clinically obese. You need to take care buddy")







