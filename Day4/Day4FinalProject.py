rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

draw = '''
----xxx-D-xxx----
----xxx-R-xxx----
----xxx-A-xxx----
----xxx-W-xxx----
'''
#Write your code below this line 👇

# TODO: check for all the cases

import random 

logos = [rock, paper, scissors, draw]

user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")

user_choice = int(user_choice)

comp_choice = random.randint(0, 2)

row1 = ['x', 1, 0]
row2 = [1, 'x', 2]
row3 = [0, 2, 'x']

ans = [row1, row2, row3]

ans_idx = ans[user_choice - 1][comp_choice - 1]


# print("User: ", user_choice)
# print("Comp: ", comp_choice)
# print("ans_idx: ", ans_idx)

# print(logos[user_choice])
# print(logos[comp_choice])
if ans_idx == 'x':
  print(logos[user_choice])
  print(logos[comp_choice])
  print(logos[3])

  print("It's draw")

elif ans_idx == user_choice:
  print(logos[user_choice])
  print("\n")
  print(logos[comp_choice])
  print("You Won")

elif ans_idx == comp_choice:
  print(logos[user_choice])
  print("\n")
  print("Computer Chose: ")
  print(logos[comp_choice])
  print("You lose")

