import turtle 
import pandas
screen = turtle.Screen()
screen.title("U.S States Game Project")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)




data = pandas.read_csv("50_states.csv")

states = []
x_coor = []
y_coor = []

for state in data.state:
	states.append(state.lower())

for x in data.x:
	x_coor.append(x)

for y in data.y:
	y_coor.append(y)

guessed_states = []
no_of_states = 5
while no_of_states:
	error_message = turtle.Turtle()
	error_message.hideturtle()
	error_message.color("green")
	error_message.penup()
	
	user_answer = screen.textinput(title="Guess the state", prompt="What is your guess?")

	if user_answer.lower() == "exit":
		break

	try:
		user_answer = user_answer.lower()
		state_idx = states.index(user_answer)
		guessed_states.append(user_answer)
		error_message.goto(x_coor[state_idx], y_coor[state_idx])		
		error_message.write(states[state_idx], move=False, align="center", font=("Arial", 10, "normal"))

	except:
		print("Please Enter Valid Input!!")
		# error_message.goto(0, 0)
		# error_message.color("red")
		# error_message.write("Please Enter Valid Input", move=False, align="center", font=("Arial", 15, "normal"))
		# error_message.clear()
		
	no_of_states -= 1



	# error_message.clear()


remained_states = []
for state in states:
	if state not in guessed_states:
		remained_states.append(state)

print(remained_states)

data_dict = {
	"missed states": remained_states
}
data_frame = pandas.DataFrame(data_dict)

data_frame.to_csv("missedGuesses.csv")