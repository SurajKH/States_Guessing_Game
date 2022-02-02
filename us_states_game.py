import turtle
import pandas

screen_object = turtle.Screen()
# we have basically set to the given title over here
screen_object.title("United States Game")

image_location = "us_states_img.gif"

# now we have added the map as the image over here
screen_object.addshape(image_location)
turtle.shape(image_location)

# we have the details of state along with its x and y points on the map in the form of a csv file
state_details = pandas.read_csv("50_states.csv")
# convert the given details to list over here
state_details_list = state_details.state.to_list()

guessed_states_list = []

while len(guessed_states_list) < 50:
    guessed_answer_state = screen_object.textinput(title=f"{len(guessed_states_list)}/50 guessed states are correct!!!",
                                                   prompt="Guess the states's name over here").title()
    # now we need to see whether the states exists in the csv file
    if guessed_answer_state == "Exit":
        missing_states_list = []
        # we have considered this list to basically
        for states in state_details_list:
            if states not in guessed_states_list:
                missing_states_list.append(states)
        new_data_list = pandas.DataFrame(missing_states_list)
        new_data_list.to_csv("missing_states.csv")
        # now we have stored the list of missing states onto the missing_states.csv file
        break

    if guessed_answer_state in state_details_list:
        guessed_states_list.append(guessed_answer_state)
        # we have appended the guessed states into the above list
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = state_details[state_details.state == guessed_answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(guessed_answer_state)


screen_object.exitonclick()
