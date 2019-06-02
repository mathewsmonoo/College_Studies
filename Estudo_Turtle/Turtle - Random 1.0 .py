import turtle
import random

def r_n(num1):
    random.seed()
    int1 = random.randint(0,num1+1)
    return int1

def create_turtle():
    ttuga = turtle.Turtle()
    shapelist=['arrow','turtle','circle','square','triangle','classic']
    ttuga.shape(random.choice(shapelist))
    ttuga.speed(200)
    turtle.colormode(255)
    ttuga.color((r_n(255)),(r_n(255)),(r_n(255)))
    return ttuga

def gen_degree(): #random degree int
    grau1 = r_n(90)
    return grau1

def gen_mov(): #random movement lenght int
    mov1 = r_n(35)
    return mov1
    
def primeiromov(ttuga):
    if ((r_n(1000)%2) == 0):
        deg1 = int(gen_degree())
        ttuga.right(deg1)
        ttuga.forward(gen_mov())
    else:
        deg2 = int(gen_degree())
        ttuga.left(deg2)
        ttuga.forward(gen_mov())
    return

def segundomov(ttuga):
    ttuga.left(deg1)
    ttuga.forward(gen_mov())
    ttuga.right(deg1)
    ttuga.forward(gen_mov())
    
#go
ttuga = create_turtle()
repetitions = r_n(250)
for _ in range(repetitions):
    primeiromov(ttuga)
ttuga.home()
for _ in range(repetitions):
    segundomov(ttuga)
ttuga.home()
turtle.exitonclick()




