import turtle
def teste1(tartaruga, tamanho, cor, veloc):
    reliquia.speed(veloc)
    reliquia.color(cor)
    for _ in range(360):
        reliquia.forward(50)
        reliquia.left(1+ _ )
        

screen = turtle.Screen()
reliquia = turtle.Turtle()
reliquia.shape('turtle')

teste1(reliquia,200,'green',10)
screen.exitonclick()