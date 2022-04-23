import turtle
import pandas

# create screen and add title

screen = turtle.Screen()
screen.title("U.S State Game")

# add image as shape
image = "blank_states_img.gif"
screen.addshape(image)
# set turtle shape to the newly added image
turtle.shape(image)

pointer = turtle.Turtle()
pointer.hideturtle()

############################################################
# try getting location points on the map . may not need since we already have a file
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()
###########################################################

# read csv file
data = pandas.read_csv("50_states.csv")
data_dict = data.to_dict()
count = 0
while count < 50:
    user_answer = screen.textinput(title=f"{count}/50 States guessed", prompt="Whats another state's name")

    # new_data = pandas.DataFrame([state for state in data_dict["state"] if state not in guessed_state])
    for key, value in data_dict["state"].items():
        if value.lower() == user_answer.lower():
            x_value = data_dict["x"][key]
            y_value = data_dict["y"][key]
            pointer.penup()
            pointer.goto(x_value, y_value)
            pointer.write(arg=f"{value}", align="center", font=('Arial', 10, 'normal'))
            count += 1
            break

screen.exitonclick()
