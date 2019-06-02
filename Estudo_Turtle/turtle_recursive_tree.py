import turtle
def tree(t,galho):
    if galho > 5:
        t.fd(galho)
        t.rt(20)
        tree(t,galho-10)
        t.lt(40)
        tree(t,galho-10)
        t.rt(20)
        t.bk(galho)
        t.color('brown')
    else:
        t.color('green')

if __name__ == "__main__":
    screen = turtle.Screen()
    t = turtle.Turtle()
    t.speed('fastest')
    t.shape('turtle')
    #turtle.delay(0)
    t.lt(90)
    t.up
    t.bk(300)
    t.down()
    t.pensize(2)
    t.color('brown')
    
    tree(t,100)
    t.color('black')
    screen.exitonclick()