from turtle import*
pensize(3)
pencolor("black")
i=1
while(i<=160):
    seth(90)
    fd(i)
    seth(180)
    fd(i+1)
    seth(-90)
    fd(i+3)
    seth(0)
    fd(i+5)
    i=i+8
seth(90)
fd(161)
seth(180)
fd(162)
seth(-90)
fd(163)
seth(0)
fd(0)
turtle.done()
