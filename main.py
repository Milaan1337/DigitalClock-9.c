from turtle import *
from j_clock import Clock

class Kattintgato:

    scr = Screen()
    t = Turtle()
    t2 = Turtle()
    c = Clock(scr)

    def asd(self):
        self.t.fillcolor("green")
        self.t.begin_fill()
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
        self.t.end_fill()

    def asd2(self):
        for i in range(3):
            self.t.left(135)
            self.t.forward(100)
            self.t.left(90)

    def asd3(self):
        self.t.right(135)
        self.asd()

    def nulla(self):
        self.t.left(90)
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



    def egy(self):
        self.t.left(90)
        self.asd()
        self.t.right(45)
        self.t.penup()
        self.t.forward(15)
        self.t.pendown()
        self.asd()

    def ketto(self):
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

    def harom(self):
        self.asd()
        for i in range(2):
            self.t.right(135)
            self.t.penup()
            self.t.forward(15)
            self.t.pendown()
            self.asd()
        for i in range(2):
            self.t.right(45)
            self.t.penup()
            self.t.forward(15)
            self.asd()

    def negy(self):
        self.t.left(90)
        self.asd()
        self.t.right(45)
        self.t.penup()
        self.t.forward(10)
        self.t.left(90)
        self.t.forward(10)
        self.t.pendown()
        self.asd()
        self.t.right(135)
        self.t.penup()
        self.t.forward(10)
        self.t.forward(10)
        self.t.pendown()
        self.asd()
        self.t.right(135)
        self.t.penup()
        self.t.forward(90)
        self.t.right(90)
        self.t.forward(10)
        self.asd()

    def ot(self):
        self.t.left(90)
        self.asd()
        self.t.right(45)
        self.t.penup()
        self.t.forward(10)
        self.t.left(90)
        self.t.forward(10)
        self.t.pendown()
        self.asd()
        self.t.right(135)
        self.t.penup()
        self.t.forward(10)
        self.t.forward(10)
        self.t.pendown()
        self.asd()
        self.t.right(45)
        self.t.forward()



    def __init__(self):
        self.t.fillcolor("yellow")
        self.t2.fillcolor("yellow")
        self.ot()

        self.t._delay(0)
        self.t.speed(100000000000)

        self.scr.mainloop()


Kattintgato()