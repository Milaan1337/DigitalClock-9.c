from datetime import *
from turtle import *

class Clock:
    _t: datetime = datetime.now()
    _hourChangeEvent = 0
    _secondChangeEvent = 0
    _minuteChangeEvent = 0
    _scr: TurtleScreen
    _dsp_min: int = _t.min
    _dsp_sec: int = _t.second
    _dsp_hour: int = _t.hour
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
        self._scr.ontimer(fun=self._handleEvents, t=self.frequency)
        self._t = datetime.now()
        if self._dsp_sec != self._t.second:
            self._dsp_sec = self._t.second
            if self._secondChangeEvent != 0:
                self._secondChangeEvent()
        if self._dsp_min != self._t.min:
            self._dsp_min = self._t.min
            if self._minuteChangeEvent != 0:
                self._minuteChangeEvent()
        if self._dsp_hour != self._t.hour:
            self._dsp_hour = self._t.hour
            if self._hourChangeEvent != 0:
                self._hourChangeEvent()

    def leftNumber(self, num: int) -> int:
        return (num // 10) % 10

    def rightNumber(self, num: int) -> int:
        return num % 10