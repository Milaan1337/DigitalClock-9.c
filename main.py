from turtle import *
from j_clock import Clock

class Kattintgato:

    scr = Screen()
    t = Turtle()
    t2 = Turtle()
    c = Clock(scr)

    def asd(self):
        xA = self.t.xcor()
        yA = self.t.ycor()
        rotA = self.t.heading()
        self.t.penup()
        self.t.forward(-9)
        self.t.right(90)
        self.t.forward(5)
        self.t.left(90)
        self.t.forward(80)
        self.t.pendown()
        self.t.left(135)
        self.t.forward(20)
        self.t.left(45)
        self.t.forward(60)
        self.t.left(45)
        self.t.forward(20)
        self.t.left(90)
        self.t.forward(20)
        self.t.left(45)
        self.t.forward(60)
        self.t.left(45)
        self.t.forward(20)
        self.t.penup()
        self.t.goto(xA, yA)
        self.t.pendown()
        self.t.setheading(rotA)

    def asdB(self):
        self.t.penup()
        self.t.forward(80)
        self.t.setheading(-90)
        self.t.forward(20)
        self.t.pendown()
        xB = self.t.xcor()
        yB = self.t.ycor()
        rotB = self.t.heading()
        self.t.penup()
        self.t.forward(80)
        self.t.pendown()
        self.t.left(135)
        self.t.forward(20)
        self.t.left(45)
        self.t.forward(60)
        self.t.left(45)
        self.t.forward(20)
        self.t.left(90)
        self.t.forward(20)
        self.t.left(45)
        self.t.forward(60)
        self.t.left(45)
        self.t.forward(20)
        self.t.penup()
        self.t.goto(xB, yB)
        self.t.pendown()
        self.t.setheading(rotB)

    def asdC(self):
        self.t.penup()
        self.t.forward(80)
        self.t.setheading(-90)
        self.t.forward(20)
        self.t.pendown()
        xC = self.t.xcor()
        yC = self.t.ycor()
        rotC = self.t.heading()
        self.t.penup()
        self.t.forward(80)
        self.t.pendown()
        self.t.left(135)
        self.t.forward(20)
        self.t.left(45)
        self.t.forward(60)
        self.t.left(45)
        self.t.forward(20)
        self.t.left(90)
        self.t.forward(20)
        self.t.left(45)
        self.t.forward(60)
        self.t.left(45)
        self.t.forward(20)
        self.t.penup()
        self.t.goto(xC, yC)
        self.t.pendown()
        self.t.setheading(rotC)

    def asdD(self):
        self.t.penup()
        self.t.forward(80)
        self.t.setheading(180)
        self.t.forward(20)
        self.t.pendown()
        xD = self.t.xcor()
        yD = self.t.ycor()
        rotD = self.t.heading()
        self.t.penup()
        self.t.forward(80)
        self.t.pendown()
        self.t.left(135)
        self.t.forward(20)
        self.t.left(45)
        self.t.forward(60)
        self.t.left(45)
        self.t.forward(20)
        self.t.left(90)
        self.t.forward(20)
        self.t.left(45)
        self.t.forward(60)
        self.t.left(45)
        self.t.forward(20)
        self.t.penup()
        self.t.goto(xD, yD)
        self.t.pendown()
        self.t.setheading(rotD)

    def asdE(self):
        self.t.penup()
        self.t.forward(80)
        self.t.forward(8)
        self.t.setheading(90)
        self.t.forward(12)
        self.t.pendown()
        xE = self.t.xcor()
        yE = self.t.ycor()
        rotE = self.t.heading()
        self.t.penup()
        self.t.forward(80)
        self.t.pendown()
        self.t.left(135)
        self.t.forward(20)
        self.t.left(45)
        self.t.forward(60)
        self.t.left(45)
        self.t.forward(20)
        self.t.left(90)
        self.t.forward(20)
        self.t.left(45)
        self.t.forward(60)
        self.t.left(45)
        self.t.forward(20)
        self.t.penup()
        self.t.goto(xE, yE)
        self.t.pendown()
        self.t.setheading(rotE)

    def asdF(self):
        self.t.penup()
        self.t.forward(80)
        self.t.setheading(90)
        self.t.forward(20)
        self.t.pendown()
        xF = self.t.xcor()
        yF = self.t.ycor()
        rotF = self.t.heading()
        self.t.penup()
        self.t.forward(80)
        self.t.pendown()
        self.t.left(135)
        self.t.forward(20)
        self.t.left(45)
        self.t.forward(60)
        self.t.left(45)
        self.t.forward(20)
        self.t.left(90)
        self.t.forward(20)
        self.t.left(45)
        self.t.forward(60)
        self.t.left(45)
        self.t.forward(20)
        self.t.penup()
        self.t.goto(xF, yF)
        self.t.pendown()
        self.t.setheading(rotF)

    def asdG(self):
        self.t.penup()
        self.t.setheading(0)
        self.t.forward(-2)
        self.t.setheading(-90)
        self.t.forward(15)
        self.t.setheading(0)
        self.t.forward(20)
        self.t.pendown()
        xF = self.t.xcor()
        yF = self.t.ycor()
        rotF = self.t.heading()
        self.t.penup()
        self.t.forward(80)
        self.t.pendown()
        self.t.left(135)
        self.t.forward(20)
        self.t.left(45)
        self.t.forward(60)
        self.t.left(45)
        self.t.forward(20)
        self.t.left(90)
        self.t.forward(20)
        self.t.left(45)
        self.t.forward(60)
        self.t.left(45)
        self.t.forward(20)
        self.t.penup()
        self.t.goto(xF, yF)
        self.t.pendown()
        self.t.setheading(rotF)


    def asd2(self):
        self.t2.fillcolor("green")
        self.t2.begin_fill()
        self.t2.penup()
        self.t2.forward(80)
        self.t2.pendown()
        self.t2.left(135)
        self.t2.forward(20)
        self.t2.left(45)
        self.t2.forward(60)
        self.t2.left(45)
        self.t2.forward(20)
        self.t2.left(90)
        self.t2.forward(20)
        self.t2.left(45)
        self.t2.forward(60)
        self.t2.left(45)
        self.t2.forward(20)
        self.t2.end_fill()

    #def asd2(self):
        #for i in range(3):
            #self.t.left(135)
            #self.t.forward(100)
            #self.t.left(90)

    #def asd3(self):
        #self.t.right(135)
        #self.asd()

    def nulla(self):
        x0 = self.t.xcor()
        y0 = self.t.ycor()
        heading0 = self.t.heading()
        self.t.right(90)
        self.asd()
        self.t.penup()
        self.t.right(45)
        self.t.forward(15)
        self.asd()
        self.t.penup()
        self.t.right(45)
        self.t.forward(10)
        self.t.left(90)
        self.t.forward(10)
        self.asd()
        self.t.penup()
        self.t.right(45)
        self.t.forward(2)
        self.t.left(90)
        self.t.forward(18)
        self.asd()
        self.t.penup()
        self.t.right(45)
        self.t.forward(15)
        self.asd()
        self.t.penup()
        self.t.right(45)
        self.t.forward(10)
        self.t.left(90)
        self.t.forward(10)
        self.asd()
        self.t.penup()
        self.t.goto(x0,y0)
        self.t.setheading(heading0)
        self.t.pendown()

    def nulla2(self):
        x0 = self.t2.xcor()
        y0 = self.t2.ycor()
        heading0 = self.t2.heading()
        self.t2.right(90)
        self.asd2()
        self.t2.penup()
        self.t2.right(45)
        self.t2.forward(15)
        self.asd2()
        self.t2.penup()
        self.t2.right(45)
        self.t2.forward(10)
        self.t2.left(90)
        self.t2.forward(10)
        self.asd2()
        self.t2.penup()
        self.t2.right(45)
        self.t2.forward(2)
        self.t2.left(90)
        self.t2.forward(18)
        self.asd2()
        self.t2.penup()
        self.t2.right(45)
        self.t2.forward(15)
        self.asd2()
        self.t2.penup()
        self.t2.right(45)
        self.t2.forward(10)
        self.t2.left(90)
        self.t2.forward(10)
        self.asd2()
        self.t2.penup()
        self.t2.goto(x0,y0)
        self.t2.setheading(heading0)
        self.t2.pendown()

    def egy(self):
        x = self.t.xcor()
        y = self.t.ycor()
        heading = self.t.heading()
        self.t.penup()
        self.t.forward(80)
        self.t.right(90)
        self.t.forward(15)
        self.asd()
        self.t.penup()
        self.t.right(45)
        self.t.forward(15)
        self.asd()
        self.t.penup()
        self.t.goto(x, y)
        self.t.pendown()
        self.t.setheading(heading)

    def egy2(self):
        x = self.t2.xcor()
        y = self.t2.ycor()
        heading = self.t2.heading()
        self.t2.penup()
        self.t2.forward(80)
        self.t2.right(90)
        self.t2.forward(15)
        self.asd2()
        self.t2.penup()
        self.t2.right(45)
        self.t2.forward(15)
        self.asd2()
        self.t2.penup()
        self.t2.goto(x, y)
        self.t2.pendown()
        self.t2.setheading(heading)

    def ketto(self):
        x2 = self.t.xcor()
        y2 = self.t.ycor()
        heading2 = self.t.heading()
        self.asd()
        for i in range(2):
            self.t.right(135)
            self.t.penup()
            self.t.forward(15)
            self.t.pendown()
            self.asd()
        for i in range(2):
            self.t.left(45)
            self.t.penup()
            self.t.forward(15)
            self.asd()
        self.t.penup()
        self.t.goto(x2,y2)
        self.t.pendown()
        self.t.setheading(heading2)

    def ketto2(self):
        x2 = self.t2.xcor()
        y2 = self.t2.ycor()
        heading2 = self.t2.heading()
        self.asd2()
        for i in range(2):
            self.t2.right(135)
            self.t2.penup()
            self.t2.forward(15)
            self.t2.pendown()
            self.asd2()
        for i in range(2):
            self.t2.left(45)
            self.t2.penup()
            self.t2.forward(15)
            self.asd2()
        self.t2.penup()
        self.t2.goto(x2,y2)
        self.t2.pendown()
        self.t2.setheading(heading2)

    def harom(self):
        x3 = self.t.xcor()
        y3 = self.t.ycor()
        heading3 = self.t.heading()
        self.asd()
        self.t.right(135)
        self.t.penup()
        self.t.forward(15)
        self.t.pendown()
        self.asd()
        self.t.right(45)
        self.t.penup()
        self.t.forward(15)
        self.asd()
        self.t.left(225)
        self.t.penup()
        self.t.forward(15)
        self.asd()
        self.t.right(130)
        self.t.penup()
        self.t.forward(90)
        self.t.right(95)
        self.t.penup()
        self.t.forward(16)
        self.asd()
        self.t.penup()
        self.t.goto(x3, y3)
        self.t.setheading(heading3)

    def harom2(self):
        x3 = self.t2.xcor()
        y3 = self.t2.ycor()
        heading3 = self.t2.heading()
        self.asd2()
        self.t2.right(135)
        self.t2.penup()
        self.t2.forward(15)
        self.t2.pendown()
        self.asd2()
        self.t2.right(45)
        self.t2.penup()
        self.t2.forward(15)
        self.asd2()
        self.t2.left(225)
        self.t2.penup()
        self.t2.forward(15)
        self.asd2()
        self.t2.right(130)
        self.t2.penup()
        self.t2.forward(90)
        self.t2.right(95)
        self.t2.penup()
        self.t2.forward(16)
        self.asd2()
        self.t2.penup()
        self.t2.goto(x3, y3)
        self.t2.setheading(heading3)

    def negy(self):
        x4 = self.t.xcor()
        y4 = self.t.ycor()
        heading4 = self.t.heading()
        self.t.penup()
        self.t.forward(80)
        self.t.right(90)
        self.t.forward(15)
        self.asd()
        self.t.penup()
        self.t.right(45)
        self.t.forward(15)
        self.asd()
        self.t.penup()
        self.t.right(45)
        self.t.backward(90)
        self.t.right(90)
        self.t.forward(15)
        self.asd()
        self.t.penup()
        self.t.right(135)
        self.t.forward(15)
        self.asd()
        self.t.penup()
        self.t.goto(x4, y4)
        self.t.pendown()
        self.t.setheading(heading4)

    def negy2(self):
        x4 = self.t2.xcor()
        y4 = self.t2.ycor()
        heading4 = self.t2.heading()
        self.t2.penup()
        self.t2.forward(80)
        self.t2.right(90)
        self.t2.forward(15)
        self.asd2()
        self.t2.penup()
        self.t2.right(45)
        self.t2.forward(15)
        self.asd2()
        self.t2.penup()
        self.t2.right(45)
        self.t2.backward(90)
        self.t2.right(90)
        self.t2.forward(15)
        self.asd2()
        self.t2.penup()
        self.t2.right(135)
        self.t2.forward(15)
        self.asd2()
        self.t2.penup()
        self.t2.goto(x4, y4)
        self.t2.pendown()
        self.t2.setheading(heading4)

    def ot(self):
        x5 = self.t.xcor()
        y5 = self.t.ycor()
        heading5 = self.t.heading()
        self.asd()
        self.t.penup()
        self.t.right(45)
        self.t.backward(94)
        self.t.left(180)
        self.t.penup()
        self.t.left(90)
        self.t.forward(15)
        self.asd()
        self.t.penup()
        self.t.left(45)
        self.t.forward(15)
        self.asd()
        self.t.penup()
        self.t.right(135)
        self.t.forward(15)
        self.asd()
        self.t.penup()
        self.t.right(135)
        self.t.forward(15)
        self.asd()
        self.t.penup()
        self.t.goto(x5, y5)
        self.t.pendown()
        self.t.setheading(heading5)

    def ot2(self):
        x5 = self.t2.xcor()
        y5 = self.t2.ycor()
        heading5 = self.t2.heading()
        self.asd2()
        self.t2.penup()
        self.t2.right(45)
        self.t2.backward(94)
        self.t2.left(180)
        self.t2.penup()
        self.t2.left(90)
        self.t2.forward(15)
        self.asd2()
        self.t2.penup()
        self.t2.left(45)
        self.t2.forward(15)
        self.asd2()
        self.t2.penup()
        self.t2.right(135)
        self.t2.forward(15)
        self.asd2()
        self.t2.penup()
        self.t2.right(135)
        self.t2.forward(15)
        self.asd2()
        self.t2.penup()
        self.t2.goto(x5, y5)
        self.t2.pendown()
        self.t2.setheading(heading5)

    def hat(self):
        x6 = self.t.xcor()
        y6 = self.t.ycor()
        heading6 = self.t.heading()
        self.asd()
        self.t.penup()
        self.t.goto(x6, y6)
        self.t.pendown()
        self.t.setheading(heading6)
        self.t.right(90)
        self.t.penup()
        self.t.forward(20)
        self.asd()
        self.t.right(45)
        self.t.penup()
        self.t.forward(15)
        self.t.pendown()
        self.asd()
        self.t.left(45)
        self.t.penup()
        self.t.forward(15)
        self.t.pendown()
        self.asd()
        self.t.left(45)
        self.t.penup()
        self.t.forward(15)
        self.t.pendown()
        self.asd()
        self.t.left(45)
        self.t.penup()
        self.t.forward(12)
        self.t.pendown()
        self.asd()
        self.t.penup()
        self.t.goto(x6, y6)
        self.t.pendown()
        self.t.setheading(heading6)

    def hat2(self):
        x6 = self.t2.xcor()
        y6 = self.t2.ycor()
        heading6 = self.t2.heading()
        self.asd2()
        self.t2.penup()
        self.t2.goto(x6, y6)
        self.t2.pendown()
        self.t2.setheading(heading6)
        self.t2.right(90)
        self.t2.penup()
        self.t2.forward(20)
        self.asd2()
        self.t2.right(45)
        self.t2.penup()
        self.t2.forward(15)
        self.t2.pendown()
        self.asd2()
        self.t2.left(45)
        self.t2.penup()
        self.t2.forward(15)
        self.t2.pendown()
        self.asd2()
        self.t2.left(45)
        self.t2.penup()
        self.t2.forward(15)
        self.t2.pendown()
        self.asd2()
        self.t2.left(45)
        self.t2.penup()
        self.t2.forward(12)
        self.t2.pendown()
        self.asd2()
        self.t2.penup()
        self.t2.goto(x6, y6)
        self.t2.pendown()
        self.t2.setheading(heading6)

    def het(self):
        x7 = self.t.xcor()
        y7 = self.t.ycor()
        heading7 = self.t.heading()
        self.asd()
        self.t.right(135)
        self.t.penup()
        self.t.forward(15)
        self.t.pendown()
        self.asd()
        self.t.right(45)
        self.t.penup()
        self.t.forward(15)
        self.asd()
        self.t.penup()
        self.t.goto(x7, y7)
        self.t.pendown()
        self.t.setheading(heading7)

    def het2(self):
        x7 = self.t2.xcor()
        y7 = self.t2.ycor()
        heading7 = self.t2.heading()
        self.asd2()
        self.t2.right(135)
        self.t2.penup()
        self.t2.forward(15)
        self.t2.pendown()
        self.asd2()
        self.t2.right(45)
        self.t2.penup()
        self.t2.forward(15)
        self.asd2()
        self.t2.penup()
        self.t2.goto(x7, y7)
        self.t2.pendown()
        self.t2.setheading(heading7)

    def nyolc(self):
        x8 = self.t.xcor()
        y8 = self.t.ycor()
        heading8 = self.t.heading()
        self.asd()
        for i in range(3):
            self.t.penup()
            self.t.left(45)
            self.t.forward(15)
            self.asd()
        self.t.penup()
        self.t.right(45)
        self.t.forward(15)
        self.asd()
        self.t.penup()
        self.t.left(45)
        self.t.forward(15)
        self.asd()
        self.t.penup()
        self.t.left(45)
        self.t.forward(12)
        self.asd()
        self.t.penup()
        self.t.goto(x8, y8)
        self.t.pendown()
        self.t.setheading(heading8)

    def nyolc2(self):
        x8 = self.t2.xcor()
        y8 = self.t2.ycor()
        heading8 = self.t2.heading()
        self.asd2()
        for i in range(3):
            self.t2.penup()
            self.t2.left(45)
            self.t2.forward(15)
            self.asd2()
        self.t2.penup()
        self.t2.right(45)
        self.t2.forward(15)
        self.asd2()
        self.t2.penup()
        self.t2.left(45)
        self.t2.forward(15)
        self.asd2()
        self.t2.penup()
        self.t2.left(45)
        self.t2.forward(12)
        self.asd2()
        self.t2.penup()
        self.t2.goto(x8, y8)
        self.t2.pendown()
        self.t2.setheading(heading8)

    def kilenc(self):
        x9 = self.t.xcor()
        y9 = self.t.ycor()
        heading9 = self.t.heading()
        self.t.left(180)
        self.asd()
        self.t.penup()
        self.t.left(45)
        self.t.forward(15)
        self.asd()
        self.t.penup()
        self.t.left(45)
        self.t.forward(15)
        self.asd()
        self.t.penup()
        self.t.right(45)
        self.t.left(90)
        self.t.forward(15)
        self.asd()
        self.t.penup()
        self.t.right(45)
        self.t.forward(-110)
        self.t.right(180)
        self.asd()
        self.t.penup()
        self.t.right(45)
        self.t.right(90)
        self.t.forward(15)
        self.asd()
        self.t.penup()
        self.t.goto(x9, y9)
        self.t.pendown()
        self.t.setheading(heading9)

    def kilenc2(self):
        x9 = self.t2.xcor()
        y9 = self.t2.ycor()
        heading9 = self.t2.heading()
        self.t2.left(180)
        self.asd2()
        self.t2.penup()
        self.t2.left(45)
        self.t2.forward(15)
        self.asd2()
        self.t2.penup()
        self.t2.left(45)
        self.t2.forward(15)
        self.asd2()
        self.t2.penup()
        self.t2.right(45)
        self.t2.left(90)
        self.t2.forward(15)
        self.asd2()
        self.t2.penup()
        self.t2.right(45)
        self.t2.forward(-110)
        self.t2.right(180)
        self.asd2()
        self.t2.penup()
        self.t2.right(45)
        self.t2.right(90)
        self.t2.forward(15)
        self.asd2()
        self.t2.penup()
        self.t2.goto(x9, y9)
        self.t2.pendown()
        self.t2.setheading(heading9)

    def secondright(self):
        if self.c.rightNumber(self.c.sec()) == 0:
            self.t2.clear()
            self.t2.penup()
            self.t2.goto(250, -150)
            self.t2.pendown()
            self.nulla2()
        if self.c.rightNumber(self.c.sec()) == 1:
            self.t2.clear()
            self.t2.penup()
            self.t2.goto(150, -50)
            self.t2.pendown()
            self.egy2()
        if self.c.rightNumber(self.c.sec()) == 2:
            self.t2.clear()
            self.t2.penup()
            self.t2.goto(150, -50)
            self.t2.pendown()
            self.ketto2()
        if self.c.rightNumber(self.c.sec()) == 3:
            self.t2.clear()
            self.t2.penup()
            self.t2.goto(150, -50)
            self.t2.pendown()
            self.harom2()
        if self.c.rightNumber(self.c.sec()) == 4:
            self.t2.clear()
            self.t2.penup()
            self.t2.goto(150, -50)
            self.t2.pendown()
            self.negy2()
        if self.c.rightNumber(self.c.sec()) == 5:
            self.t2.clear()
            self.t2.penup()
            self.t2.goto(150, -50)
            self.t2.pendown()
            self.ot2()
        if self.c.rightNumber(self.c.sec()) == 6:
            self.t2.clear()
            self.t2.penup()
            self.t2.goto(150, -50)
            self.t2.pendown()
            self.hat2()
        if self.c.rightNumber(self.c.sec()) == 7:
            self.t2.clear()
            self.t2.penup()
            self.t2.goto(150, -50)
            self.t2.pendown()
            self.het2()
        if self.c.rightNumber(self.c.sec()) == 8:
            self.t2.clear()
            self.t2.penup()
            self.t2.goto(150, -50)
            self.t2.pendown()
            self.nyolc2()
        if self.c.rightNumber(self.c.sec()) == 9:
            self.t2.clear()
            self.t2.penup()
            self.t2.goto(150, -50)
            self.t2.pendown()
            self.kilenc2()

    def secondleft(self):
        if self.c.leftNumber(self.c.sec()) == 0:
            self.t.clear()
            self.nulla()
        if self.c.leftNumber(self.c.sec()) == 1:
            self.t.clear()
            self.egy()
        if self.c.leftNumber(self.c.sec()) == 2:
            self.t.clear()
            self.ketto()
        if self.c.leftNumber(self.c.sec()) == 3:
            self.t.clear()
            self.harom()
        if self.c.leftNumber(self.c.sec()) == 4:
            self.t.clear()
            self.negy()
        if self.c.leftNumber(self.c.sec()) == 5:
            self.t.clear()
            self.ot()
        if self.c.leftNumber(self.c.sec()) == 6:
            self.t.clear()
            self.hat()
        if self.c.leftNumber(self.c.sec()) == 7:
            self.t.clear()
            self.het()
        if self.c.leftNumber(self.c.sec()) == 8:
            self.t.clear()
            self.nyolc()
        if self.c.leftNumber(self.c.sec()) == 9:
            self.t.clear()
            self.kilenc()

    def second(self):
        self.secondleft()
        self.secondright()


    def __init__(self):
        self.t.fillcolor("yellow")
        self.t._delay(0)
        self.t.speed(0)
        self.asd()
        self.asdB()
        self.asdC()
        self.asdD()
        self.asdE()
        self.asdF()
        self.asdG()
        self.scr.mainloop()


Kattintgato()