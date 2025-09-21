import turtle
import sys
import math


side_length = 150

pen_size = 3
outline_color = "black"
fill_color = "skyblue"
label_vertices = True


screen = turtle.Screen()
screen.title("Regular Pentagon")
t = turtle.Turtle()
t.hideturtle()
t.speed(5)
t.pensize(pen_size)


n = 5
turn_angle = 360 / n


R = side_length / (2 * math.sin(math.pi / n))

t.penup()
t.setheading(90)

t.forward(R)

t.right(180 - (turn_angle / 2))

t.pendown()

t.color(outline_color,fill_color)
t.begin_fill()
vertices = []
for i in range(n):
    x,y = t.position()
    vertices.append((x,y))
    t.forward(side_length)
    t.right(turn_angle)
t.end_fill()

if label_vertices:
    t.penup()
    t.color("black")
    for idx, (x,y) in enumerate(vertices,start=1):
        t.goto(x,y)
        t.dot(6)
        t.goto(x+10,y+5)
        t.write(f"V{idx}",font=("Arial",12,"normal"))
        t.home()

t.penup()
t.goto(0,-R-30)
t.write("Regular pentagon (n=5)",align="center",font=("Arial",14,"bold"))
t.hideturtle()
screen.mainloop()

def main():
    """Main function to run the program."""
    draw_Pentagon

    if __name__ == "__main__":
    sys.exit(main())
