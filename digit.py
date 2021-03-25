from turtle import *
from turtle import Screen
from j_clock import Clock

class Digit:

    def __init__(self):
        self.scr = Screen()
        self.t = Turtle()
        self.asd()
        self.asd2()
        self.asd3()
        self.asd2()
        self.scr.mainloop()

    def asd(self):
        self.t.fillcolor("green")
        self.t.begin_fill()
        self.t.forward(100)
        self.t.left(135)
        self.t.forward(30)
        self.t.left(45)
        self.t.forward(60)
        self.t.left(45)
        self.t.forward(29)
        self.t.end_fill()


    def asd2(self):
        for i in range(3):
            self.t.left(135)
            self.t.forward(100)
            self.t.left(90)
            self.asd()

    def asd3(self):
        self.t.right(135)
        self.asd()


Digit()


