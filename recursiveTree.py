import turtle as t
t.speed(0)
t.pensize(2)
t.left(90)
t.backward(100)
t.color("green")


def draw(l):
    if(1<10):
        return
    else:
        t.forward(l)
        t.color("red")
        t.circle(2)
        t.color("green")
        t.left(30)
        draw(3*1/4)
        t.right(60)
        draw(3*1/4)
        t.left(30)
        t.backward(1)


draw(100)
