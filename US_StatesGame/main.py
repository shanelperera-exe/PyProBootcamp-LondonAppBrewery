import turtle
import pandas

def main():
    screen = turtle.Screen()
    screen.setup(width=730, height=496)
    screen.title("U.S. States Game")
    image = "blank_states_img.gif"
    screen.addshape(image)
    turtle.shape(image)

    data = pandas.read_csv("50_states.csv")
    all_states = data["state"].tolist()
    guessed_states = []

    while len(guessed_states) < 50:
        answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="Enter a state: (or enter 'Exit' to exit the game.)").title().strip()
        if answer_state == "Exit":
            missing_states = [state for state in all_states if state not in guessed_states]
            new_data =  pandas.DataFrame(missing_states)
            new_data.to_csv("states_to_learn.csv")
            break

        if answer_state in all_states and answer_state not in guessed_states:
            guessed_states.append(answer_state)
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            state_data = data[data["state"] == answer_state]
            t.goto(x=state_data["x"].item(), y=state_data["y"].item())
            t.write(state_data.state.item(), align='center', font=('Courier', 8, 'bold'))

    screen.exitonclick()

if __name__ == "__main__":
    main()
