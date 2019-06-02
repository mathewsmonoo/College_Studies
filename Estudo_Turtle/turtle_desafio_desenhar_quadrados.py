import turtle as tt
import random

#turtle creator
def CreateTurtle(): 
    ttuga = tt.Turtle()
    ttuga.speed(200)
    tt.colormode(255)
    ttuga.color(random_color(),random_color(),random_color())
    ttuga.pencolor(random_color(),random_color(),random_color())

    return ttuga
#random turtle color and pencolor generator:
def random_color():
    random.seed()
    colorR = random.randint(0,255)
    return colorR

	
def draw_square(ttuga1,distance, x, y, repetitions, gap):
	if repetitions > 0:
		ttuga1.penup()
		ttuga1.setx(x)
		ttuga1.sety(y)
		ttuga1.pendown()
		for i in range(4):
			ttuga1.forward(distance)
			ttuga1.right(90)
		draw_square(ttuga1, distance - gap*2 , x+10 , y-10, repetitions -1, gap)



def main():
	ttuga1 = CreateTurtle()
	numberofsquares = int(input("Quantos quadrados deseja que a tartaruga faça?"))
	
	distanceSize = numberofsquares * 20 	#20x maior
	
	draw_square(ttuga1,distanceSize,60,60,numberofsquares,10)
	
	exit = input("enter para encerrar...")

main()
	

