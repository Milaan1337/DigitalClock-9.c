from datetime import *
from turtle import *

class Clock:
    _t: datetime = datetime.now()
    _hourChangeEvent = 0
    _secondChangeEvent = 0
    _minuteChangeEvent = 0
    _scr: TurtleScreen
    _dsp_min: int = -1
    _dsp_sec: int = -1
    _dsp_hour: int = -1
    frequency: int = 400
    _enabled: int = 257

    def __init__(self, scr: TurtleScreen):
        self._scr = scr
        #self._scr.ontimer(fun=self._handleEvents, t=self.frequency)

    def UTC(self) -> str:
        return str(self._t.utcnow())

    def pm(self) -> bool:
        return self._t.hour.real >= 12

    def am(self) -> bool:
        return self._t.hour.real < 12

    def hour24(self) -> int:
        return int(self._t.hour.real)

    def hour12(self) -> int:
        if self.am() and self.hour24() == 0:
            return 12
        if self.pm() and self.hour24() == 12:
            return 12
        return int(self._t.hour.real % 12)

    def min(self) -> int:
        return int(self._t.minute.real)

    def sec(self) -> int:
        return int(self._t.second.real)

    def setOnSecondChangeListener(self, fun):
        self._secondChangeEvent = fun
        if self._enabled == 257:
            self._enabled = 256
            self._scr.ontimer(fun=self._handleEvents, t=1000)

    def setOnMinuteChangeListener(self, fun):
        self._minuteChangeEvent = fun
        if self._enabled == 257:
            self._enabled = 256
            self._scr.ontimer(fun=self._handleEvents, t=1000)

    def setOnHourChangeListener(self, fun):
        self._hourChangeEvent = fun
        if self._enabled == 257:
            self._enabled = 256
            self._scr.ontimer(fun=self._handleEvents, t=1000)

    def _handleEvents(self):
        print(self._enabled)
        print("---")

        self._t = datetime.now()

        if self._enabled == 256:
            if self._hourChangeEvent != 0:
                self._hourChangeEvent()
            if self._minuteChangeEvent != 0:
                self._minuteChangeEvent()
            if self._secondChangeEvent != 0:
                self._secondChangeEvent()
            self._scr.ontimer(fun=self._handleEvents, t=self.frequency)
            self._dsp_hour = self.hour24()
            self._dsp_min = self.min()
            self._dsp_sec = self.sec()
            self._enabled = 0
            return

        if self._enabled != 0:
            return

        if self._dsp_hour != self.hour24():
            print("HourChange")
            self._dsp_hour = self.hour24()
            if self._hourChangeEvent != 0:
                self._enabled = self._enabled + 1
                self._hourChangeEvent()
                self._enabled = self._enabled - 1

        self._t = datetime.now()
        if self._dsp_min != self.min():
            print("MinuteChange")
            self._dsp_min = self.min()
            if self._minuteChangeEvent != 0:
                self._enabled = self._enabled + 2
                self._minuteChangeEvent()
                self._enabled = self._enabled - 2

        self._t = datetime.now()
        if self._dsp_sec != self.sec():
            print("SecondChange")
            self._dsp_sec = self.sec()
            if self._secondChangeEvent != 0:
                self._enabled = self._enabled + 4
                print("Star")
                self._secondChangeEvent()
                print("Stop")
                self._enabled = self._enabled - 4

        self._scr.ontimer(fun=self._handleEvents, t=self.frequency)



    def leftNumber(self, num: int) -> int:
        return (num // 10) % 10

    def rightNumber(self, num: int) -> int:
        return num % 10