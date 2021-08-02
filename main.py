import colorgram as c
import turtle as t
colors = c.extract("colorgram.jpeg", 10)
tim = t.Turtle()
t.colormode(255)
tim.pensize(5)
color_list = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    tup = (r, g, b)
    color_list.append(tup)

for i in range(10):
    n = i + 1
    for j in range(10):
        tim.pencolor(color_list[j])
        tim.dot()
        if j < 9:
            tim.forward(20)
    if n % 2 == 1:
        tim.left(90)
        tim.penup()
        tim.forward(20)
        tim.left(90)
        tim.pendown()
    else:
        tim.right(90)
        tim.penup()
        tim.forward(20)
        tim.right(90)
        tim.pendown()
