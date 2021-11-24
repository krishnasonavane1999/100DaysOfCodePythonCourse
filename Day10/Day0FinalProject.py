logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""


print(logo)

# basic calculator functions
def add(num1, num2):
  return num1 + num2

def substract(num1, num2):
  return num1 - num2

def multiply(num1, num2):
  return num1 * num2

def divide(num1, num2):
  return num1 / num2

  
operations = {
  "+": add,
  "-": substract,
  "*": multiply,
  "/": divide
}

continue_operation = False
number1 = 0
number2 = 0

def calculator():
  number1 = float(input("Input first number: "))
  for operation in operations:
    print(operation)
  continue_operation = True

  while continue_operation:
    operation_choice = input("What operation you want to perform? ")

    number2 = float(input("Input second number: "))

    calculation = operations[operation_choice]

    answer = calculation(number1, number2)

    print(f"{number1} {operation_choice} {number2} = {answer}")

    process_answer = input("Do you want to take this answer as first number and perform some other operations on it? Type 'yes' or 'no'")

    if process_answer == 'yes':
      for operation in operations:
        print(operation)
      number1 = answer
    else:
      continue_operation = False
      calculator()


calculator()



