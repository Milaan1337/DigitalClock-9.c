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
    frequency: int = 100

    def __init__(self, scr: TurtleScreen):
        self._scr = scr
        self._handleEvents()

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
        fun()

    def setOnMinuteChangeListener(self, fun):
        self._minuteChangeEvent = fun
        fun()

    def setOnHourChangeListener(self, fun):
        self._hourChangeEvent = fun
        fun()

    def _handleEvents(self):
        self._t = datetime.now()
        self._scr.ontimer(fun=self._handleEvents, t=self.frequency)

        dwn: int = 0
        for t in self._scr.turtles():
            if (t.isdown()):
                dwn = dwn + 1

        if self._dsp_sec != self.sec():
            print("SecondChange")
            self._dsp_sec = self.sec()
            if self._secondChangeEvent != 0:
                if dwn > 0:
                    print("_secondChangeEvent: Jelenleg " + str(
                        dwn) + " teknős van pendown állapotban. Használja a teknős penup() metódusát, mielőtt az eseményt meghívná. Az esemény addig zárolva marad, míg az összes teknős penup állapotba nem kerül.")
                else:
                    self._secondChangeEvent()

        if self._dsp_min != self.min():
            print("MinuteChange")
            self._dsp_min = self.min()
            if self._minuteChangeEvent != 0:
                if dwn > 0:
                    print("_minuteChangeEvent: Jelenleg " + str(
                        dwn) + " teknős van pendown állapotban. Használja a teknős penup() metódusát, mielőtt az eseményt meghívná. Az esemény addig zárolva marad, míg az összes teknős penup állapotba nem kerül.")
                else:
                    self._minuteChangeEvent()

        if self._dsp_hour != self.hour24():
            print("HourChange")
            self._dsp_hour = self.hour24()
            if self._hourChangeEvent != 0:
                if dwn > 0:
                    print("_hourChangeEvent: Jelenleg " + str(
                        dwn) + " teknős van pendown állapotban. Használja a teknős penup() metódusát, mielőtt az eseményt meghívná. Az esemény addig zárolva marad, míg az összes teknős penup állapotba nem kerül.")
                else:
                    self._hourChangeEvent()


    def leftNumber(self, num: int) -> int:
        return (num // 10) % 10

    def rightNumber(self, num: int) -> int:
        return num % 10