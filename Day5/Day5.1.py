# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split(',')
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

total_students = 0
sum = 0

for student in student_heights:
  sum += student
  total_students += 1

print(round(sum / total_students))




