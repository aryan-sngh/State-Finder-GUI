import turtle

import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)



import pandas as pd
data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

# def get_mouse_click_coor(x,y):
#     print(x,y)
#
# turtle.onscreenclick(get_mouse_click_coor)


while len(guessed_states) < 50:
    answer_states = screen.textinput(title=f"{len(guessed_states)}/50",prompt="What's another state name?  ").title()
    if answer_states == "Exit":
        missing_states = [new_item for state in all_states if state not in guessed_states]
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_states in all_states:
        guessed_states.append(answer_states)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_states]
        t.goto(state_data.x.item(),state_data.y.item())
        t.write(state_data.state.item())







#if answer_state is one of the states in all the states of the 50_states

# for i in data['state']:
#
#     if answer_states == i:
#         guess_state = answer_states
#
#
#
# coordinate = data[data.state == guess_state]
#
# x_cor = coordinate.x
# y_cor = coordinate.y





# turtle.mainloop()



