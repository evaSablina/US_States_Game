import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# функция позволяет кликнуть на картинку и получить координаты
# def get_mouse_click_cor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_cor)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
states_guessed_list = []

score = 0

while len(states_guessed_list) < 50:

    answer_state = screen.textinput(title=f"{score}/50 Guess The State",
                                    prompt=f"What's another state's name?").title()

    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in states_guessed_list:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        new_state_list = states_guessed_list.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        score += 1
