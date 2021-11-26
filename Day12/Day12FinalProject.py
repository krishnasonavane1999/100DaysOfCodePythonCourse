logo = '''._._.   ________                              ___________.__              _______               ___.                  ._._.
| | |  /  _____/ __ __   ____   ______ ______ \__    ___/|  |__   ____    \      \  __ __  _____\_ |__   ___________  | | |
| | | /   \  ___|  |  \_/ __ \ /  ___//  ___/   |    |   |  |  \_/ __ \   /   |   \|  |  \/     \| __ \_/ __ \_  __ \ | | |
 \|\| \    \_\  \  |  /\  ___/ \___ \ \___ \    |    |   |   Y  \  ___/  /    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/  \|\|
 ____  \______  /____/  \___  >____  >____  >   |____|   |___|  /\___  > \____|__  /____/|__|_|  /___  /\___  >__|     ____
 \/\/         \/            \/     \/     \/                  \/     \/          \/            \/    \/     \/         \/\/'''

you_won = '''_____.___.               __      __            ._._.
\__  |   | ____  __ __  /  \    /  \____   ____| | |
 /   |   |/  _ \|  |  \ \   \/\/   /  _ \ /    \ | |
 \____   (  <_> )  |  /  \        (  <_> )   |  \|\|
 / ______|\____/|____/    \__/\  / \____/|___|  /___
 \/                            \/             \/\/\/'''

you_lose = '''_____.___.              .____                         
\__  |   | ____  __ __  |    |    ____  ______ ____   
 /   |   |/  _ \|  |  \ |    |   /  _ \/  ___// __ \  
 \____   (  <_> )  |  / |    |__(  <_> )___ \\  ___/  
 / ______|\____/|____/  |_______ \____/____  >\___  > 
 \/                             \/         \/     \/  '''

import random
user_choice = ""

print(logo)
def show_initial_info(no_of_guess):
  if no_of_guess == 10:
    print(f"You have chosen easy level. You have {no_of_guess} guess in total")
  elif no_of_guess == 5:
    print(f"You have chosen hard level. You have {no_of_guess} guess in total")


def guess_the_number(no_of_guess):
  show_initial_info(no_of_guess)
  random_no = random.randint(1, 100)
  while no_of_guess:
    print(f"You have {no_of_guess} guess left.")
    user_guess = int(input("Enter Your Guess: "))

    print(f" user guess: {user_guess}  random: {random_no}")
    if user_guess > random_no:
      print(f"user guess {user_guess} ")
      print("Too high")
    elif user_guess < random_no:
      print("Too low")
    else:
      print("You guessed it")
      print(you_won)
      return
    no_of_guess -= 1

  print("You used all the available guesses!!")
  print(you_lose)

def play_game():
  user_choice = input("Which level you want to play? 'easy' / 'hard'(Type it): ")

  if user_choice == "easy":
    no_of_guess = 10
  else:
    no_of_guess = 5

  guess_the_number(no_of_guess)

play_game()
play_again_choice = input("Do you want to play again? 'y' or 'n' ")

while play_again_choice == 'y':
  play_game()
  play_again_choice = input("Do you want to play again? 'y' or 'n' ")




    