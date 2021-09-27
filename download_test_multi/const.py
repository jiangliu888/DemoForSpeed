# -*- coding: UTF-8 -*-
from enum import Enum

class CalcType(Enum):
    SingleThread = 0
    MultiThread = 1
    MultiPorcess = 2
    PyCoroutine = 3