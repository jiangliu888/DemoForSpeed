# -*- encoding=utf-8 -*-


from enum import Enum


class CalcType(Enum):
    """计算类型
    """
    SingleThread = 0
    MultiThread = 1
    MultiProcess = 2
    PyCoroutine = 3