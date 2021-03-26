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

    def asd3(self):
        self.t.right(135)
        self.asd()




    def __init__(self):
        self.t.fillcolor("yellow")
        self.t2.fillcolor("yellow")
        self.asd()
        self.t._delay(0)
        self.t2.speed(0)
        self.t2._delay(0)
        self.t.speed(0)

        self.scr.mainloop()


Kattintgato()