from turtle import *
screen = Screen()
screen.setup(width=1200, height=800)
screen.screensize(2000, 1500)
screen.tracer(False)
tom = Turtle()
tom.speed(0)
tom.width(1)
tom.pu()
tom.goto(0,500)
tom.pd()

def square(c):
    tom.color(c)
    tom.begin_fill()
    for count in range(4):
        tom.forward(25)
        tom.left(90)
    tom.end_fill()

def jump(r):
    tom.pu()
    tom.fd(r)
    tom.pd()

for count in range(9):
    square('black')
    jump(25)
tom.right(90)
tom.fd(25)
tom.left(90)
for count in range(4):
    square('black')
    jump(25)
tom.pu()
tom.bk(25*4)
tom.pd()
tom.lt(90)
square('pink')
tom.fd(25)
tom.lt(90)
tom.fd(25)
square('pink')
for count in range(7):
    tom.fd(25)
    square('pink')

for count in range(2):
    jump(25)
    square('black')

tom.fd(25)
tom.lt(90)
jump(25)
tom.rt(90)
square('black')
jump(25)
square('black')
jump(25)
square('black')
tom.bk(25)
tom.bk(25)
tom.rt(180)
tom.rt(90)
tom.fd(25)
tom.lt(90)
square('pink')
for count in range(15):
    square('pink')
    jump(25)

for count in range(2):
    square('black')
    jump(25)

tom.rt(90)
jump(25)
tom.lt(90)
square('black')
for count in range(2):
    jump(25)
    square('black')

tom.bk(25+25)
tom.lt(90)
tom.fd(25)
tom.lt(90)
square('pink')
for count in range(20):
    square('pink')
    jump(25)

square('black')
tom.fd(25)
tom.lt(90)
tom.fd(25)
tom.rt(90)
square('black')
tom.fd(25)
square('black')
tom.bk(25)
tom.lt(180)
tom.fd(25)
tom.rt(180)
square('pink')
tom.lt(90)
tom.fd(25)
tom.rt(180)
tom.rt(90)
square('pink')

for count in range(22):
    jump(25)
    square('pink')

jump(25)
square('black')
jump(25)
square('black')
jump(25)
tom.lt(90)
tom.fd(25)
tom.rt(90)
square('black')
jump(25)
square('black')

for count in range(4):
    jump(25)
    square('black')

jump(25)
tom.rt(90)
square('black')
tom.rt(90)
square('pink')
tom.fd(25)
square('pink')
tom.fd(25)
square('pink')
tom.fd(25)
square('pink')
tom.fd(25)
square('pink')
tom.fd(25)
square('pink')
tom.fd(25)
tom.lt(90)
tom.fd(25)
tom.rt(90)
square('black')
tom.lt(90)
tom.fd(25)
tom.lt(90)
square('pink')

for count in range(6):
    square('pink')
    jump(25)

square('#efcde6')
tom.fd(25)
square('black')
tom.pu()
tom.bk(25*8)
tom.pd()
tom.lt(180)
tom.rt(90)
tom.fd(25)
tom.lt(90)
square('pink')
tom.fd(25)
square('pink')
tom.fd(25)
square('pink')
tom.fd(25)
square('pink')
tom.fd(25)
tom.lt(90)
tom.fd(25)
square('black')



tom.rt(90)
square('black')
tom.fd(25)
square('black')
tom.fd(25)
tom.lt(90)
square('black')
tom.fd(25)
square('black')
tom.fd(25)
square('black')
tom.fd(25)
square('black')
tom.fd(25)
square('black')
tom.fd(25)
tom.lt(90)
jump(25)
square('black')
tom.lt(90)
jump(25)
tom.rt(90)
square('black')
tom.rt(90)
jump(25)
jump(25)
tom.lt(90)
square('black')
tom.rt(90)
jump(25)
tom.lt(90)
square('black')
tom.rt(90)
jump(25)
tom.lt(90)
square('black')
jump(25)
tom.rt(90)
jump(25)
tom.lt(90)
square('black')
tom.rt(90)
jump(25)
tom.lt(90)
square('black')
tom.rt(90)
jump(25)
tom.lt(90)
jump(25)
square('black')
jump(25)
square('black')
jump(25)
tom.lt(90)
jump(25)
tom.rt(90)
square('black')
tom.lt(90)
jump(25)
tom.rt(90)
square('black')
tom.lt(90)
jump(25)
tom.rt(90)
square('black')
tom.lt(90)
jump(25)
tom.rt(90)
square('black')
tom.lt(90)
jump(25)
tom.rt(90)
square('black')
tom.lt(90)
jump(25)
tom.lt(90)
square('black')
tom.fd(25)
tom.rt(180)
square('black')
tom.lt(90)
tom.fd(25)
tom.rt(90)
square('black')

tom.lt(90)
tom.fd(25)
tom.pu()
tom.fd(25)
tom.pd()
tom.lt(90)
square('black')

tom.rt(90)
tom.pu()
tom.fd(25)
tom.pd()
tom.lt(90)
square('black')
tom.pu()
tom.goto(375,375)
tom.lt(90)
tom.fd(25)
tom.fd(25)
tom.fd(25)
tom.fd(25)
tom.fd(25)
tom.fd(25)
tom.fd(25)
tom.rt(90)
tom.bk(25)
tom.pd()
square('#00008B')
tom.bk(25)
square('black')
tom.bk(25)
square('black')
tom.lt(90)
tom.pu()
tom.fd(25)
tom.rt(90)
tom.fd(25)
tom.pd()
square('#00008B')
tom.bk(25)
square('#00008B')
tom.lt(90)
tom.pu()
tom.fd(25)
tom.rt(90)
tom.fd(25)
tom.pd()
square('#00008B')
tom.bk(25)
square('#00008B')
tom.pu()
tom.rt(90)
tom.fd(25)
tom.fd(25)
tom.fd(25)
tom.lt(90)
tom.fd(25)
tom.pd()
square('black')
tom.bk(25)
square('black')
tom.fd(50)
square('black')
tom.rt(90)
tom.fd(25)
tom.lt(90)
square('black')
tom.bk(25)
square('black')
tom.pu()
tom.goto(375,375)
tom.rt(90)
tom.fd(25)
tom.fd(1)
tom.lt(90)
tom.pd()
square('pink')

for count in range(10):
    tom.fd(25)
    square('pink')



for count in range(12):
    tom.fd(25)
    square('pink')

tom.pu()
tom.fd(25)
tom.pd()
square('black')


tom.pu()
tom.goto(125,401)
tom.lt(90)
tom.fd(25)
tom.rt(90)
tom.pd()
square('black')
tom.bk(25)
square('black')
tom.fd(25)
tom.fd(25)
tom.pu()
tom.lt(90)
tom.fd(25)
tom.rt(90)
square('black')

for count in range(4):
    tom.lt(90)
    tom.fd(25)
    tom.rt(90)
    square('black')

tom.bk(25)
tom.rt(90)
tom.fd(25)
tom.lt(90)
square('black')
tom.lt(90)
tom.fd(25)
tom.rt(90)
square('black')

for count in range(3):
    tom.lt(90)
    tom.fd(25)
    tom.rt(90)
    square('black')

tom.pu()
tom.rt(90)
tom.fd(1)
tom.lt(90)
tom.bk(25)
tom.pd()
square('#00008B')



tom.lt(90)
tom.fd(25)
tom.rt(90)
square('black')
tom.lt(90)
tom.fd(25)
tom.rt(90)
square('black')


tom.pu()
tom.bk(25)
tom.pd()
square('#00008B')
tom.bk(25)
square('#00008B')
tom.bk(25)
square('#00008B')

tom.pu()
tom.goto(150,127)
tom.pd()
tom.lt(90)
tom.pu()
tom.fd(25)
tom.pd()
tom.rt(90)
tom.bk(25)
square('black')
tom.bk(25)
square('black')
tom.bk(25)
square('black')
tom.pu()
tom.bk(25)
tom.rt(90)
tom.fd(25)
tom.lt(90)
tom.pd()
square('black')
tom.rt(90)
tom.fd(25)
tom.lt(90)
square('black')


tom.pu()
tom.fd(25)
tom.pd()
square('#00008B')
tom.fd(25)
square('#00008B')
tom.fd(25)
square('#00008B')
tom.pu()
tom.goto(250,152)
tom.pd()
tom.rt(90)
tom.fd(25)
tom.lt(90)
square('black')


tom.pu()
tom.fd(25)
tom.pd()
square('#00008B')

tom.fd(25)
square('black')
tom.fd(25)
square('black')

tom.pu()
tom.goto(250,177)
tom.pd()

tom.pu()
tom.fd(25)
tom.rt(90)
tom.fd(25)
tom.lt(90)
tom.pd()
square('black')
tom.fd(25)
square('black')
tom.fd(25)
square('black')
tom.fd(25)
square('black')
tom.bk(25)
tom.bk(25)
tom.bk(25)
tom.rt(90)
tom.fd(25)
tom.lt(90)
square('black')
tom.fd(25)
square('black')
tom.fd(25)
square('black')
tom.fd(25)
square('black')
tom.bk(25)
tom.bk(25)
tom.bk(25)

tom.rt(90)
tom.fd(25)
tom.lt(90)
square('black')
tom.fd(25)
square('black')
tom.bk(25)


tom.rt(90)
tom.fd(25)
tom.lt(90)
square('black')
tom.fd(25)
square('black')

tom.pu()
tom.rt(90)
tom.fd(25)
tom.lt(90)
tom.pd()
square('black')
tom.rt(90)
tom.fd(25)
tom.lt(90)
square('black')

tom.fd(25)
tom.rt(90)
tom.fd(25)
tom.lt(90)
square('black')

tom.pu()
tom.rt(90)
tom.fd(25)
tom.lt(90)
tom.pd()

square('pink')

print(tom.position())

for count in range(6):
    jump(-25)
    square('pink')

jump(-25*4)
tom.lt(90)
tom.fd(1)
tom.rt(90)

square('pink')
jump(-25)
square('pink')
jump(-25)
square('pink')
jump(-25)
square('pink')
jump(-25)
square('black')

for count in range(6):
    jump(-25)
    square('pink')

jump(-25)
square('#efcde6')
jump(-25)
square('black')


jump(-25)
tom.lt(90)
jump(25)
tom.rt(90)
square('black')

jump(25)
square('#efcde6')
jump(25)
square('#efcde6')

for count in range(5):
    jump(25)
    square('pink')

jump(25)
square('black')

jump(-25)
tom.lt(90)
jump(25)
tom.rt(90)
square('black')

for count in range(3):
    jump(-25)
    square('pink')

jump(-25)
square('#FF007F')

for count in range(2):
    jump(-25)
    square('#efcde6')

jump(-25)
square('black')

tom.lt(90)
jump(25)
tom.rt(90)

square('black')

for count in range(2):
    jump(25)
    square('#efcde6')

for count in range(2):
    jump(25)
    square('#FF007F')

jump(25)
square('pink')

jump(25)
square('black')


tom.lt(90)
jump(25)
tom.rt(90)
square('black')

for count in range(3):
    jump(-25)
    square('#FF007F')

jump(-25)
square('#efcde6')
jump(-25)
square('#efcde6')
jump(-25)
square('black')

tom.lt(90)
jump(25)
tom.rt(90)
square('black')

for count in range(3):
    jump(25)
    square('#efcde6')

jump(25)
square('#FF007F')

jump(25)
square('black')

tom.lt(90)
jump(25)
tom.rt(90)
square('black')

jump(-25)
square('#FF007F')

for count in range(2):
    jump(-25)
    square('#efcde6')

jump(-25)
square('#efcde6')

tom.lt(90)
jump(25)
tom.rt(90)
square('black')

for count in range(2):
    jump(25)
    square('#efcde6')

jump(25)
square('black')

tom.lt(90)
jump(25)
tom.rt(90)

jump(-25)
square('black')

tom.lt(90)
jump(25)
tom.rt(90)
square('black')

jump(-25)
tom.rt(90)
jump(25)
tom.lt(90)
square('black')

jump(-25)
tom.rt(90)
jump(25)
jump(25)
tom.lt(90)
square('black')

jump(50)
tom.lt(90)
jump(25*2)
tom.rt(90)
square('#efcde6')

jump(25)
square('black')

tom.lt(90)
jump(25)
jump(25)
tom.rt(90)
jump(-25)
square('black')

tom.pu()
tom.goto(175,377)
tom.pd()
tom.color('white')

jump(25*3)
square('pink')


for count in range(12):
    jump(25)
    square('pink')

jump(25)
square('black')

tom.lt(90)
jump(25)
tom.rt(90)
square('#efcde6')
jump(25)
square('black')

jump(-25)

for count in range(12):
    jump(-25)
    square('pink')

jump(-25)
jump(-25)
jump(-25)
jump(-25)
jump(-25)

square('pink')
jump(-25)
square('pink')
jump(-25)
square('pink')
jump(-25)
square('pink')
jump(-25)
square('pink')
jump(-25)
square('pink')

for count in range(5):
    jump(-25)

square('pink')
jump(-25)
square('pink')
jump(-25)
square('pink')
jump(-25)
square('pink')

jump(-25)
tom.lt(90)
jump(25)
tom.rt(90)
square('pink')

jump(25)
square('pink')

jump(25)
square('pink')

jump(25)
square('pink')

jump(25)
square('pink')

jump(25*5)
square('pink')

jump(25)
square('pink')

jump(25)
square('pink')

jump(25)
square('pink')

jump(25)
square('pink')

for count in range(6):
    jump(25)


square('pink')

for count in range(12):
    jump(25)
    square('pink')


jump(25)
square('#efcde6')
jump(25)
square('black')

tom.lt(90)
jump(25)
tom.rt(90)
jump(25)
square('black')

jump(-25)
square('#efcde6')

for count in range(14):
    jump(-25)
    square('pink')

for count in range(6):
    jump(-25)

square('pink')

for count in range(4):
    jump(-25)
    square('pink')

for count in range(6):
    jump(-25)



tom.pu()
tom.lt(90)
tom.fd(1)
tom.rt(90)
tom.pd()

square('pink')

for count in range(4):
    jump(-25)
    square('pink')

tom.lt(90)
jump(25)
tom.rt(90)
square('pink')

for count in range(4):
    jump(25)
    square('pink')

for count in range(6):
    jump(25)

square('pink')

jump(25)
square('pink')

jump(25)
square('pink')

jump(25)
square('pink')

for count in range(7):
    jump(25)

square('pink')

for count in range(13):
    jump(25)
    square('pink')

jump(25)
square('#efcde6')

jump(25)
square('black')

tom.lt(90)
jump(25)
tom.rt(90)
jump(25)
square('black')
jump(-25)
square('#efcde6')

for count in range(16):
    jump(-25)
    square('pink')

for count in range(6):
    jump(-25)

square('pink')

jump(-25)
square('pink')
jump(-25)
square('pink')
jump(-25)
square('pink')
jump(-25)
square('pink')

for count in range(5):
    jump(-25)


jump(-25)
square('pink')

for count in range(4):
    jump(-25)
    square('pink')

tom.lt(90)
jump(25)
tom.rt(90)
square('pink')

for count in range(4):
    jump(25)
    square('pink')

for count in range(6):
    jump(25)

square('pink')

for count in range(4):
    jump(25)
    square('pink')

for count in range(6):
    jump(25)

square('pink')

for count in range(15):
    jump(25)
    square('pink')

jump(25)
square('#efcde6')

jump(25)
square('#efcde6')

jump(25)
square('black')

tom.lt(90)
jump(25)
tom.rt(90)
square('black')

jump(-25)
square('#efcde6')

jump(-25)
square('#efcde6')

jump(-25)
square('black')

jump(-25)
square('black')

for count in range(14):
    jump(-25)
    square('pink')

for count in range(6):
    jump(-25)

square('pink')

for count in range(4):
    jump(-25)
    square('pink')

for count in range(6):
    jump(-25)

square('pink')

for count in range(5):
    jump(-25)
    square('pink')

tom.lt(90)
jump(25)
tom.rt(90)

square('pink')

for count in range(4):
    jump(25)
    square('#FF007F')

jump(25)
square('pink')

for count in range(5):
    jump(25)

square('pink')

for count in range(4):
    jump(25)
    square('pink')

for count in range(7):
    jump(25)

square('pink')


for count in range(15):
    jump(25)
    square('pink')

jump(25)
square('black')
jump(25)
square('black')

tom.lt(90)
jump(25)
tom.rt(90)
jump(25)
jump(25)
square('black')
jump(-25)
square('black')

for count in range(19):
    jump(-25)
    square('pink')

for count in range(6):
    jump(-25)

square('pink')

for count in range(4):
    jump(-25)
    square('pink')

for count in range(5):
    jump(-25)


square('#FF007F')

for count in range(5):
    jump(-25)
    square('#FF007F')

jump(-25)
square('pink')

tom.lt(90)
jump(25)
tom.rt(90)

square('pink')

jump(25)
square('pink')

for count in range(5):
    jump(25)
    square('#FF007F')

jump(25)
square('pink')

for count in range(3):
    jump(25)


square('pink')

for count in range(5):
    jump(25)
    square('pink')

for count in range(6):
    jump(25)

square('pink')

for count in range(6):
    jump(25)
    square('#FF007F')

for count in range(14):
    jump(25)
    square('pink')

jump(25)
square('black')
tom.lt(90)
jump(25)
tom.rt(90)
square('black')

for count in range(14):
    jump(-25)
    square('pink')

jump(-25)
square('#FF007F')

for count in range(5):
    jump(-25)
    square('#FF007F')

jump(-25)
square('pink')
jump(-25)
square('pink')

for count in range(4):
    jump(-25)

square('pink')

for count in range(5):
    jump(-25)
    square('pink')


jump(-25)
square('black')

for count in range(4):
    jump(-25)
    square('pink')

jump(-25)
square('#FF007F')
jump(-25)
square('#FF007F')

jump(-25)
square('pink')
jump(-25)
square('pink')
jump(-25)
square('pink')
jump(-25)
square('pink')

jump(-25)
square('#efcde6')
jump(-25)
square('black')

tom.lt(90)
jump(25)
tom.rt(90)
square('black')

jump(25)
square('#efcde6')

for count in range(10):
    jump(25)
    square('pink')

jump(25)
square('black')
jump(25)
square('black')
jump(25)
square('black')
jump(25)
square('black')
jump(25)
square('black')

for count in range(7):
    jump(25)
    square('pink')


jump(25)
square('#FF007F')

for count in range(5):
    jump(25)
    square('#FF007F')

for count in range(15):
    jump(25)
    square('pink')

jump(25)
square('black')

jump(25)
tom.lt(90)
jump(25)
tom.rt(90)
square('black')

for count in range(17):
    jump(-25)
    square('pink')

jump(-25)
square('#FF007F')
jump(-25)
square('#FF007F')
jump(-25)
square('#FF007F')
jump(-25)
square('#FF007F')

for count in range(9):
    jump(-25)
    square('pink')

jump(-25)
square('black')
jump(-25)
square('black')

jump(-25)
square('pink')
jump(-25)
square('pink')

for count in range(10):
    jump(-25)
    square('pink')

jump(-25)
square('#efcde6')

jump(-25)
square('black')

tom.lt(90)
jump(25)
tom.rt(90)
square('black')
jump(25)
square('#efcde6')
jump(25)
square('#efcde6')

jump(25)
square('#FF007F')

for count in range(29):
    jump(25)
    square('pink')

for count in range(2):
    jump(25)
    square('#FF007F')

for count in range(11):
    jump(25)
    square('pink')

jump(25)
square('#efcde6')

jump(25)
square('black')

tom.lt(90)
jump(25)
tom.rt(90)
square('black')

jump(-25)
square('#efcde6')

for count in range(11):
    jump(-25)
    square('pink')

jump(-25)
square('#FF007F')
jump(-25)
square('#FF007F')

jump(-25)
square('pink')
jump(-25)
square('pink')
jump(-25)
square('pink')
jump(-25)
square('pink')
jump(-25)
square('pink')
jump(-25)
square('pink')
jump(-25)
square('pink')
jump(-25)
square('pink')
jump(-25)
square('pink')
jump(-25)
square('pink')

jump(-25)
square('black')
jump(-25)
square('black')
jump(-25)
square('black')
jump(-25)
square('black')
jump(-25)
square('black')
jump(-25)
square('black')



for count in range(14):
    jump(-25)
    square('pink')

jump(-1)
jump(-25)
square('#FF007F')

jump(-25)
square('#efcde6')
jump(-25)
square('#efcde6')
jump(-25)
square('black')

tom.lt(90)
jump(25)
tom.rt(90)
square('black')

for count in range(2):
    jump(25)
    square('#efcde6')

jump(25)
square('#FF007F')

jump(25)
square('pink')
jump(25)
square('pink')
jump(25)
square('pink')
jump(25)
square('pink')
jump(25)
square('pink')
jump(25)
square('pink')
jump(25)
square('pink')
jump(25)
square('pink')
jump(25)
square('pink')
jump(25)
square('pink')
jump(25)
square('pink')

jump(25)
square('black')
jump(25)
square('black')
jump(25)
square('black')

jump(25)
square('#d90258')
jump(25)
square('#d90258')
jump(25)
square('#d90258')
jump(25)
square('#d90258')
jump(25)
square('#d90258')


jump(25)
square('black')
jump(25)
square('black')
jump(25)
square('black')

jump(25)
square('pink')
jump(25)
square('pink')
jump(25)
square('pink')
jump(25)
square('pink')
jump(25)
square('pink')
jump(25)
square('pink')


jump(25)
square('#FF007F')
jump(25)
square('#FF007F')
jump(25)
square('#FF007F')
jump(25)
square('#FF007F')
jump(25)
square('#FF007F')

jump(25)
square('pink')
jump(25)
square('pink')
jump(25)
square('pink')
jump(25)
square('pink')
jump(25)
square('pink')
jump(25)
square('pink')
jump(25)
square('pink')
jump(25)
square('pink')
jump(25)
square('pink')

jump(25)
square('#efcde6')
jump(25)
square('#efcde6')
jump(25)
square('black')

tom.lt(90)
jump(25)
tom.rt(90)
square('black')

jump(-25)
square('#efcde6')
jump(-25)
square('#efcde6')

jump(-25)
square('#FF007F')

jump(-25)
square('pink')
jump(-25)
square('pink')
jump(-25)
square('pink')
jump(-25)
square('pink')
jump(-25)
square('pink')
jump(-25)
square('pink')
jump(-25)
square('pink')

jump(-25)
square('#FF007F')
jump(-25)
square('#FF007F')
jump(-25)
square('#FF007F')
jump(-25)
square('#FF007F')
jump(-25)
square('#FF007F')
jump(-25)
square('#FF007F')
jump(-25)
square('#FF007F')
jump(-25)
square('#FF007F')

jump(-25)
square('pink')
jump(-25)
square('pink')

jump(-25)
square('black')
jump(-25)
square('black')

jump(-25)
square('#d90258')

jump(-25)
square('#f46e7c')
jump(-25)
square('#f46e7c')
jump(-25)
square('#f46e7c')
jump(-25)
square('#f46e7c')

jump(-25)
square('#d90258')
jump(-25)
square('#d90258')
jump(-25)
square('#d90258')

jump(-25)
square('#8a043b')
jump(-25)
square('#8a043b')
jump(-25)
square('#8a043b')

jump(-25)
square('black')

jump(-25)
square('pink')
jump(-25)
square('pink')
jump(-25)
square('pink')
jump(-25)
square('pink')
jump(-25)
square('pink')
jump(-25)
square('pink')
jump(-25)
square('pink')
jump(-25)
square('pink')
jump(-25)
square('pink')

jump(-1)
jump(-25)
square('#FF007F')
jump(-25)
square('#FF007F')

jump(-25)
square('#efcde6')
jump(-25)
square('#efcde6')

jump(-25)
square('black')

jump(25)
tom.lt(90)
jump(25)
tom.rt(90)
square('black')

jump(25)
square('#efcde6')
jump(25)
square('#efcde6')

jump(25)
square('#FF007F')
jump(25)
square('#FF007F')
jump(25)
square('#FF007F')

jump(25)
square('pink')
jump(25)
square('pink')
jump(25)
square('pink')
jump(25)
square('pink')
jump(25)
square('pink')
jump(25)
square('pink')

jump(25)
square('black')

jump(25)
square('#8a043b')
jump(25)
square('#8a043b')
jump(25)
square('#8a043b')
jump(25)
square('#8a043b')
jump(25)
square('#8a043b')
jump(25)
square('#8a043b')
jump(25)
square('#8a043b')

jump(0.5)
jump(25)
square('#d90258')

jump(1)

jump(25)
square('#f46e7c')
jump(25)
square('#f46e7c')
jump(25)
square('#f46e7c')



jump(25)
square('#d90258')
jump(25)
square('#d90258')
jump(25)
square('#d90258')

jump(25)
square('black')
jump(25)
square('black')

jump(25)
square('#FF007F')
jump(25)
square('#FF007F')
jump(25)
square('#FF007F')
jump(25)
square('#FF007F')
jump(25)
square('#FF007F')
jump(25)
square('#FF007F')
jump(25)
square('#FF007F')
jump(25)
square('#FF007F')
jump(25)
square('#FF007F')
jump(25)
square('#FF007F')
jump(25)
square('#FF007F')
jump(25)
square('#FF007F')
jump(25)
square('#FF007F')
jump(25)
square('#FF007F')
jump(25)
square('#FF007F')
jump(25)
square('#FF007F')

jump(25)
square('#efcde6')
jump(25)
square('#efcde6')
jump(25)
square('black')

tom.lt(90)
jump(25)
tom.rt(90)
jump(-25)
jump(-2.5)
square('black')

jump(-25)
square('#efcde6')
jump(-25)
square('#efcde6')


jump(-25)
square('#FF007F')
jump(-25)
square('#FF007F')
jump(-25)
square('#FF007F')
jump(-25)
square('#FF007F')
jump(-25)
square('#FF007F')
jump(-25)
square('#FF007F')
jump(-25)
square('#FF007F')
jump(-25)
square('#FF007F')
jump(-25)
square('#FF007F')
jump(-25)
square('#FF007F')
jump(-25)
square('#FF007F')
jump(-25)
square('#FF007F')
jump(-25)
square('#FF007F')
jump(-25)
square('#FF007F')


jump(-25)
square('black')

for count in range(7):
    jump(-25)
    square('#d90258')

for count in range(9):
    jump(-25)
    square('#8a043b')

jump(-25)
square('black')

jump(-25)
square('pink')
jump(-25)
square('pink')
jump(-25)
square('pink')
jump(-25)
square('pink')

jump(-25)
square('#FF007F')
jump(-25)
square('#FF007F')
jump(-25)
square('#FF007F')
jump(-25)
square('#FF007F')

jump(-25)
square('#efcde6')
jump(-25)
square('#efcde6')

jump(-25)
square('#efcde6')

jump(-25)
square('black')

tom.lt(90)
jump(25)
tom.rt(90)
square('black')

jump(25)
square('black')
jump(25)
square('#efcde6')
jump(25)
square('#efcde6')

jump(25)
square('#efcde6')
jump(25)
square('#FF007F')
jump(25)
square('#FF007F')
jump(25)
square('#FF007F')

jump(25)
square('#FF007F')
jump(25)
square('pink')
jump(25)
square('pink')
jump(25)
square('pink')

jump(25)
square('pink')

jump(25)
square('black')
jump(25)
square('#8a043b')
jump(25)
square('#8a043b')
jump(25)
square('#8a043b')
jump(25)
square('#8a043b')
jump(25)
square('#8a043b')
jump(25)
square('#8a043b')
jump(25)
square('#8a043b')
jump(25)
square('#8a043b')
jump(25)
square('#8a043b')

jump(25)
square('#8a043b')
jump(25)
square('#d90258')
jump(25)
square('#d90258')
jump(25)
square('#d90258')
jump(25)
square('#d90258')
jump(25)
square('#d90258')
jump(25)
square('#d90258')


jump(25)
square('black')
jump(25)
square('#FF007F')

jump(25)
square('#FF007F')

jump(25)
square('black')
jump(25)
square('#FF007F')
jump(25)
square('#FF007F')
jump(25)
square('#FF007F')
jump(25)
square('#FF007F')
jump(25)
square('#FF007F')
jump(25)
square('#FF007F')
jump(25)
square('#FF007F')
jump(25)
square('#FF007F')
jump(25)
square('#FF007F')

jump(25)
square('#efcde6')
jump(25)
square('#efcde6')

jump(25)
square('black')

tom.lt(90)
jump(25)
tom.rt(90)
jump(-25)
square('black')

jump(-25)
square('#efcde6')
jump(-25)
square('#efcde6')
jump(-25)
square('#efcde6')
jump(-25)
square('#efcde6')
jump(-25)
square('#efcde6')
jump(-25)
square('#efcde6')
jump(-25)
square('#efcde6')

jump(-25)
square('#FF007F')

jump(-25)
square('black')
jump(-25)
square('black')
jump(-25)
square('black')

jump(-25)
square('#FF007F')

jump(-25)
square('black')

jump(-25)
square('#d90258')
jump(-25)
square('#d90258')
jump(-25)
square('#d90258')
jump(-25)
square('#d90258')
jump(-25)
square('#d90258')
jump(-25)
square('#d90258')

jump(-25)
square('#8a043b')
jump(-25)
square('#8a043b')
jump(-25)
square('#8a043b')
jump(-25)
square('#8a043b')
jump(-25)
square('#8a043b')
jump(-25)
square('#8a043b')
jump(-25)
square('#8a043b')
jump(-25)
square('#8a043b')
jump(-25)
square('#8a043b')
jump(-25)
square('#8a043b')
jump(-25)
square('#8a043b')

jump(-25)
square('black')


jump(-25)
square('pink')
jump(-25)
square('pink')

jump(-25)
square('#FF007F')
jump(-25)
square('#FF007F')
jump(-25)
square('#FF007F')
jump(-25)
square('#FF007F')
jump(-25)
square('#FF007F')
jump(-25)
square('#FF007F')

jump(-25)
square('#FF007F')
jump(-25)
square('#efcde6')
jump(-25)
square('#efcde6')

jump(-25)
square('black')

tom.lt(90)
jump(25)
tom.rt(90)
square('black')



jump(25)
square('#efcde6')
jump(25)
square('#efcde6')

jump(25)
square('#FF007F')
jump(25)
square('#FF007F')
jump(25)
square('#FF007F')
jump(25)
square('#FF007F')
jump(25)
square('#FF007F')
jump(25)
square('#FF007F')
jump(25)
square('#FF007F')
jump(25)
square('#FF007F')
jump(25)
square('#FF007F')

jump(25)
square('black')

jump(25)
square('#8a043b')
jump(25)
square('#8a043b')
jump(25)
square('#8a043b')
jump(25)
square('#8a043b')
jump(25)
square('#8a043b')
jump(25)
square('#8a043b')
jump(25)
square('#8a043b')
jump(25)
square('#8a043b')
jump(25)
square('#8a043b')
jump(25)
square('#8a043b')
jump(25)
square('#8a043b')
jump(25)
square('#8a043b')

jump(25)
square('#d90258')
jump(25)
square('#d90258')
jump(25)
square('#d90258')
jump(25)
square('#d90258')
jump(25)
square('#d90258')
jump(25)
square('#d90258')

jump(25)
square('black')

jump(25)
square('#FF007F')
jump(25)
square('#FF007F')
jump(25)
square('#FF007F')

jump(25)
square('black')
jump(25)
square('black')
jump(25)
square('black')
jump(25)
square('black')
jump(25)
square('black')
jump(25)
square('black')
jump(25)
square('black')
jump(25)
square('black')

tom.lt(90)
jump(25)
tom.rt(90)
jump(-25)
jump(-25)


square('black')

jump(-25)
square('#efcde6')
jump(-25)
square('#efcde6')

jump(-25)
square('#FF007F')
jump(-25)
square('#FF007F')
jump(-25)
square('#FF007F')
jump(-25)
square('#FF007F')
jump(-25)
square('#FF007F')

jump(-25)
square('black')

jump(-25)
square('#d90258')
jump(-25)
square('#d90258')
jump(-25)
square('#d90258')
jump(-25)
square('#d90258')
jump(-25)
square('#d90258')
jump(-25)
square('#d90258')

jump(-25)
square('#97023f')
jump(-25)
square('#97023f')
jump(-25)
square('#97023f')
jump(-25)
square('#97023f')
jump(-25)
square('#97023f')

jump(-25)
square('#8a043b')
jump(-25)
square('#8a043b')
jump(-25)
square('#8a043b')
jump(-25)
square('#8a043b')
jump(-25)
square('#8a043b')
jump(-25)
square('#8a043b')
jump(-25)
square('#8a043b')
jump(-25)
square('#8a043b')

jump(-25)
square('black')


jump(-25)
square('#FF007F')
jump(-25)
square('#FF007F')
jump(-25)
square('#FF007F')
jump(-25)
square('#FF007F')
jump(-25)
square('#FF007F')
jump(-25)
square('#FF007F')
jump(-25)
square('#FF007F')

jump(-25)
square('#efcde6')
jump(-25)
square('#efcde6')

jump(-25)
square('black')
jump(-25)
square('black')

jump(25)
tom.lt(90)
jump(25)
tom.rt(90)
jump(25)

square('black')

jump(25)
square('#efcde6')
jump(25)
square('#efcde6')


jump(25)
square('#FF007F')
jump(25)
square('#FF007F')
jump(25)
square('#FF007F')
jump(25)
square('#FF007F')
jump(25)
square('#FF007F')
jump(25)
square('#FF007F')

jump(25)
square('black')

jump(25)
square('#8a043b')
jump(25)
square('#8a043b')
jump(25)
square('#8a043b')


jump(25)
square('#97023f')
jump(25)
square('#97023f')
jump(25)
square('#97023f')
jump(25)
square('#97023f')
jump(25)
square('#97023f')
jump(25)
square('#97023f')
jump(25)
square('#97023f')
jump(25)
square('#97023f')
jump(25)
square('#97023f')
jump(25)
square('#97023f')
jump(25)
square('#97023f')

jump(25)
square('#d90258')
jump(25)
square('#d90258')
jump(25)
square('#d90258')

jump(25)
square('#97023f')

jump(25)
square('#d90258')

jump(25)
square('black')

jump(25)
square('#FF007F')
jump(25)
square('#FF007F')
jump(25)
square('#FF007F')
jump(25)
square('#FF007F')

jump(25)
square('#efcde6')
jump(25)
square('#efcde6')

jump(25)
square('black')


tom.lt(90)
jump(25)
tom.rt(90)
jump(-25)


square('black')

jump(-25)
square('#efcde6')
jump(-25)
square('#efcde6')

jump(-25)
square('#FF007F')
jump(-25)
square('#FF007F')

jump(-25)
square('black')

jump(-25)
square('#d90258')

jump(-25)
square('#97023f')

jump(-25)
square('#d90258')
jump(-25)
square('#d90258')
jump(-25)
square('#d90258')

jump(-25)
square('#97023f')
jump(-25)
square('#97023f')
jump(-25)
square('#97023f')
jump(-25)
square('#97023f')
jump(-25)
square('#97023f')
jump(-25)
square('#97023f')
jump(-25)
square('#97023f')
jump(-25)
square('#97023f')
jump(-25)
square('#97023f')
jump(-25)
square('#97023f')
jump(-25)
square('#97023f')
jump(-25)
square('#97023f')
jump(-25)
square('#97023f')

jump(-25)
square('#8a043b')
jump(-25)
square('#8a043b')

jump(-25)
square('black')


jump(-25)
square('#FF007F')
jump(-25)
square('#FF007F')
jump(-25)
square('#FF007F')
jump(-25)
square('#FF007F')
jump(-25)
square('#FF007F')


jump(-25)
square('#efcde6')
jump(-25)
square('#efcde6')

jump(-25)
square('black')

tom.lt(90)
jump(25)
tom.rt(90)
square('black')

jump(25)
square('#efcde6')
jump(25)
square('#efcde6')
jump(25)
square('#efcde6')

for count in range(5):
    jump(25)
    square('#FF007F')


jump(25)
square('black')

for count in range(15):
    jump(25)
    square('#97023f')

jump(25)
square('#d90258')
jump(25)
square('#d90258')

jump(25)
square('#97023f')

jump(25)
square('#d90258')

jump(25)
square('black')

jump(25)
square('#FF007F')

jump(25)
square('#efcde6')
jump(25)
square('#efcde6')
jump(25)
square('black')

jump(-25)
tom.lt(90)
jump(25)
tom.rt(90)
square('black')

jump(-25)
square('#efcde6')

jump(-25)
square('#efcde6')

jump(-25)
square('black')

jump(-25)
square('#d90258')

jump(-25)
square('#97023f')
jump(-25)
square('#97023f')

jump(-25)
square('#d90258')

for count in range(15):
    jump(-25)
    square('#97023f')

jump(-25)
square('black')

jump(-25)
square('#FF007F')
jump(-25)
square('#FF007F')
jump(-25)
square('#FF007F')
jump(-25)
square('#FF007F')

jump(-25)
square('#efcde6')

jump(-25)
square('#efcde6')

jump(-25)
square('#efcde6')

jump(-25)
square('black')

tom.lt(90)
jump(25)
tom.rt(90)
jump(25)
square('black')

jump(25)
square('black')

jump(25)
square('#efcde6')
jump(25)
square('#efcde6')

jump(25)
square('#FF007F')
jump(25)
square('#FF007F')
jump(25)
square('#FF007F')
jump(25)
square('#FF007F')

jump(25)
square("black")

for count in range(18):
    jump(25)
    square('#97023f')



jump(25)
square('#d90258')

for count in range(2):
    jump(25)
    square('black')

jump(-25)
tom.lt(90)
jump(25)
tom.rt(90)

square('black')

jump(-25)
square('#d90258')

for count in range(18):
    jump(-25)
    square('#97023f')

jump(-25)
square('black')

jump(-25)
square('#FF007F')
jump(-25)
square('#FF007F')


jump(-25)
square('#efcde6')
jump(-25)
square('#efcde6')

jump(-25)
square('black')
jump(-25)
square('black')

jump(-25)
square('#c70251')

jump(-25)
square('black')

jump(25)
tom.lt(90)
jump(25)
tom.rt(90)
square('black')

jump(25)
square('#c70251')
jump(25)
square('#c70251')

jump(25)
square('black')
jump(25)
square('black')

jump(25)
square('#efcde6')
jump(25)
square('#efcde6')

jump(25)
square('#FF007F')

jump(25)
square('black')

for count in range(17):
    jump(25)
    square('#97023f')


jump(25)
square('black')

tom.lt(90)
jump(25)
tom.rt(90)
square('black')

for count in range(16):
    jump(-25)
    square('#97023f')

jump(-25)
square('black')

jump(-25)
square('#efcde6')
jump(-25)
square('#efcde6')

jump(-25)
square('black')
jump(-25)
square('black')

for count in range(4):
    jump(-25)
    square('#c70251')

jump(-25)
square('black')

jump(25)
tom.lt(90)
jump(25)
tom.rt(90)
square('black')

for count in range(5):
    jump(25)
    square('#c70251')

for count in range(4):
    jump(25)
    square('black')

jump(25)
square('#97023f')
jump(25)
square('#97023f')

for count in range(6):
    jump(25)
    square('#ba0e4e')


jump(25)
square('#97023f')
jump(25)
square('#97023f')
jump(25)
square('#97023f')
jump(25)
square('#97023f')
jump(25)
square('#97023f')
jump(25)
square('#97023f')
jump(25)
square('black')


tom.lt(90)
jump(25)
tom.rt(90)
square('black')

jump(-25)
square('#97023f')
jump(-25)
square('#97023f')
jump(-25)
square('#97023f')
jump(-25)
square('#97023f')

for count in range(9):
    jump(-25)
    square('#ba0e4e')

jump(-25)
square('black')

for count in range(9):
    jump(-25)
    square('#c70251')


jump(-25)
square('black')




jump(25)
tom.lt(90)
jump(25)
tom.rt(90)
square('black')

for count in range(9):
    jump(25)
    square('#c70251')


jump(25)
square("black")
jump(25)
square('black')

jump(25)
square('#ba0e4e')
jump(25)
square('#ba0e4e')
jump(25)
square('#ba0e4e')
jump(25)
square('#ba0e4e')
jump(25)
square('#ba0e4e')
jump(25)
square('#ba0e4e')
jump(25)
square('#ba0e4e')
jump(25)
square('#ba0e4e')

jump(25)
square('#97023f')
jump(25)
square('#97023f')

jump(25)
square('black')

jump(-25)
tom.lt(90)
jump(25)
tom.rt(90)
square('black')

jump(-25)
square('black')

for count in range(6):
    jump(-25)
    square('#ba0e4e')

jump(-25)
square('black')
jump(-25)
square("black")

jump(-25)
square('#d90258')
jump(-25)
square('#d90258')

for count in range(8):
    jump(-25)
    square('#c70251')

jump(-25)
square('black')

tom.lt(90)
jump(25)
tom.rt(90)
square('black')

jump(25)
square('#d90258')

jump(25)
square('#d90258')

jump(25)
square('#c70251')
jump(25)
square('#c70251')
jump(25)
square('#c70251')
jump(25)
square('#c70251')

for count in range(6):
    jump(25)
    square('#d90258')


for count in range(6):
    jump(25)
    square('black')

jump(-25)
tom.lt(90)
jump(25)
tom.rt(90)
square('black')

for count in range(11):
    jump(-25)
    square('#d90258')

jump(-25)
square('#c70251')
jump(-25)
square('#c70251')

jump(-25)
square('#d90258')
jump(-25)
square('#d90258')

jump(-25)
square('black')

tom.lt(90)
jump(25)
tom.rt(90)
jump(25)
square('black')

for count in range(14):
    jump(25)
    square('#d90258')

jump(25)
square('black')

jump(-25)
tom.lt(90)
jump(25)
tom.rt(90)
square('black')

for count in range(6):
    jump(-25)
    square('#d90258')


for count in range(3):
    jump(-25)
    square('#f46e7c')

jump(-25)
square('#d90258')

jump(-25)
square('#d90258')

jump(-25)
square('black')
jump(-25)
square('black')

jump(25)
jump(25)
tom.lt(90)
jump(25)
tom.rt(90)
square("black")

jump(25)
square('#d90258')
jump(25)
square('#d90258')

jump(25)
square('#f46e7c')

jump(25)
square('#f46e7c')

for count in range(6):
    jump(25)
    square('#d90258')

jump(25)
square('black')

jump(-25)
tom.lt(90)
jump(25)
tom.rt(90)
square('black')

for count in range(8):
    jump(-25)
    square('#d90258')


jump(-25)
square('black')

jump(25)
tom.lt(90)
jump(25)
tom.rt(90)
square('black')

jump(25)
square("black")

for count in range(6):
    jump(25)
    square('#d90258')

jump(25)
square('black')

jump(-25)
tom.lt(90)
jump(25)
tom.rt(90)
square('black')

jump(-25)
square('black')
jump(-25)
square('black')
jump(-25)
square('black')
jump(-25)
square('black')
jump(-25)
square('black')


screen.tracer(True)

done()
