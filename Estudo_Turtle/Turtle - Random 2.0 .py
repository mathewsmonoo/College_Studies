import turtle
import random

#Functions:
#creates turtle
def createturtle(): 
    ttuga = turtle.Turtle()
    ttuga.speed(200)
    turtle.colormode(255)
    ttuga.color(random_color(),random_color(),random_color())
    ttuga.pencolor(random_color(),random_color(),random_color())
    shapelist=['arrow','turtle','circle','square','triangle','classic']
    ttuga.shape(random.choice(shapelist))
    return ttuga

#random turtle color and pencolor generator:
def random_color():
    random.seed()
    colorR = random.randint(0,255)
    return colorR

def gen_degree(): #random degree int
    grau1 = random.randint(0,90)
    return grau1

def gen_mov(): #random movement lenght int
    grau1 = random.randint(10,25)
    return grau1

#'Main'
ttuga = createturtle()
while(1):
    random.seed()
    turtle.reset()
    if ((random.randint(1,1000)%2) == 0):
        ttuga.right(gen_degree())
    else:
        ttuga.left(gen_degree())
    if ((random.randint(1,1000)%2) == 0):
        x, y = turtle.position()
        if (x > 400 or y > 600):
            turtle.undo()
            turtle.left(180)
        else:
            ttuga.forward(gen_mov())
    else:
        ttuga.back(gen_mov())
turtle.exitonclick()