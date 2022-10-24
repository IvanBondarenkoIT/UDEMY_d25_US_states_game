import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
guess_count = 0
turtle.shape(image)

data_frame = pandas.read_csv("50_states.csv")
states_list = data_frame.state.to_list()
while states_list != []:
    answer_state = screen.textinput(title=f'Guess the State{guess_count}/50',
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        df = pandas.DataFrame(states_list)
        df.to_csv("states_to_learn.csv")
        break

    if answer_state in states_list:
        coords = data_frame.loc[data_frame['state'] == answer_state]
        writer = turtle.Turtle()
        writer.penup()
        writer.hideturtle()
        writer.color("black")
        writer.goto(int(coords.x), int(coords.y))
        writer.write(f"{answer_state}")
        del(states_list[states_list.index(answer_state)])
else:
    print("You win!")




screen.exitonclick()
