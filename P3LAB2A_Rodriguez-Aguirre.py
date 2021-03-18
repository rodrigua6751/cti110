import turtle
wn = turtle.Screen()
allan = turtle.Turtle()

for i in [0, 1, 2, 3]:
    allan.forward(50)
    allan.left(90)

dan = turtle.Turtle()

counter = 0
while counter < 3:
    dan.forward(80)
    dan.left(120)
    counter = counter + 1

wn.mainloop()
