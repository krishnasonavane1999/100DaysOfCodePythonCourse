import random

personalities = {

  "Rahul": ["Famous footballer, from India", 1000],
  "Ramesh": ["Doctor, from India", 5000],
  "Kevin": ["Businessman, from USA", 2000],
  "Chandler": ["Great fictional character, from California", 3000],
  "Joey": ["Great fictional character, FRIENDS from Canada", 500],
  "Monica": ["Great fictional character, from New York", 2000],
  "Rachel": ["Great fictional character, FRIENDS, from New Jersey", 1000],
  "Phoebe": ["Great fictional character, FRIENDS, from New Jersey", 4000],
  "Mattew": ["Very famous actor, from USA", 6000],
  

}

logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""

print(logo)
names = []

for name in personalities:
  names.append(name)

def give_random_name():
  name = names[random.randint(0, 8)]

  return name


keep_going = True
first_name = give_random_name() 
second_name = give_random_name() 

if first_name == second_name:
  while first_name == second_name:
    second_name = give_random_name()

score = 0

while keep_going:
  print(f"Compare A: {first_name }, {personalities[first_name][0]}")
  print(vs)
  print(f"Against B: {second_name }, {personalities[second_name][0]}")

  user_choice = input("Who has more followers? 'A' or 'B' ")

  followers_of_A = personalities[first_name][1]
  followers_of_B = personalities[second_name][1]

  if user_choice == 'A' and followers_of_A > followers_of_B:
    score += 1
    print(f"You are right. Your score is {score}")

  elif user_choice == 'A' and followers_of_A < followers_of_B:
    print(f"You are wrong. Your score is {score}")
    keep_going = False
  
  elif user_choice == 'B' and followers_of_B > followers_of_A:
    score += 1
    print(f"You are right!. Your score is {score}")
 
  elif user_choice == 'B' and followers_of_B < followers_of_A:
    print(f"You are wrong. Your score is {score}")
    keep_going = False
  
  first_name = second_name
  second_name = give_random_name()
  if first_name == second_name:
    while first_name == second_name:
      second_name = give_random_name()


