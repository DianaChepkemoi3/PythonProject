import sys
import turtle

def main():

    screen = turtle.Screen()
    screen.bgcolor("orange")
    screen.title("Pentagon")

    pen=turtle.Turtle()
    pen.color("purple")
    pen.pensize(3)

    for _ in range(5):
        pen.forward(100)
        pen.right(72)

    screen.mainloop()

    return 0

if __name__ == "__main__":
    sys.exit(main())

