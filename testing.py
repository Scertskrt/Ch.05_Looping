import turtle
x=0
while x <= 2:
    x=int(input("How many sides do you want me to draw? "))
    if x <= 2:
        print("Not acceptable!")
pencil=turtle
pencil.penup()
pencil.goto(0,-300)
pencil.pendown()
for i in range(x):
    pencil.left(360/x)
    pencil.forward(20)
turtle.exitonclick()

