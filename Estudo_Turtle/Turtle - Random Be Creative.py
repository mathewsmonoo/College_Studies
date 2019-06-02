# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 12:35:20 2019

@author: Mathews
"""
import turtle
import random
from datetime import datetime

#Functions:
def createturtle(): #creates turtle
    ttuga = turtle.Turtle()
    ttuga.speed(random.randint(1,5+1))
    
    #random turtle shape:
    shapelist=['arrow','turtle','circle','square','triangle','classic']
    ttuga.shape(random.choice(shapelist))
    
    #random turtle color and pencolor:
    colorR = random.randint(0,255+1)
    colorG = random.randint(0,255+1)
    colorB = random.randint(0,255+1)
    turtle.colormode(255)
    ttuga.color(colorR,colorG,colorB)
    ttuga.pencolor(colorR,colorG,colorB)
    return ttuga

def gen_degree(): #random degree int
    random.seed(datetime.now())
    grau1 = random.randint(0,90+1)
    return grau1

def gen_mov(): #random movement lenght int
    random.seed(datetime.now())
    grau1 = random.randint(10,50+1)
    return grau1

#'Main'
ttuga = createturtle()
creative = str(input("Be creative!:...."))
newseed = 0
for each in creative:
	newseed = int((ord(each) + newseed)/2)
	for _ in range(newseed):
		ttuga.right(gen_degree())
		ttuga.forward(gen_mov())


