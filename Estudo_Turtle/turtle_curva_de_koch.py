import turtle

def koch(ttuga, n, tamanho):
    if n==0:
        ttuga.fd(tamanho)
    else:
        koch(ttuga,n-1,tamanho/3)
        ttuga.lt(60)
        koch(ttuga,n-1,tamanho/3)
        ttuga.rt(120)
        koch(ttuga,n-1,tamanho/3)
        ttuga.lt(60)
        koch(ttuga,n-1,tamanho/3)

if __name__ == "__main__":
    screen = turtle.Screen()
    t = turtle.Turtle()
    t.shape('turtle')
    t.speed('fastest')
    tamanho = 140
    n = 4
    t.up()
    t.back(tamanho*2.25)
    t.down()
    t.pensize(2)
    
    for i in range(n):
        koch(t,i,tamanho)
        t.up()
        t.fd(20)
        t.down()
    t.hideturtle()
    screen.exitonclick()

main()