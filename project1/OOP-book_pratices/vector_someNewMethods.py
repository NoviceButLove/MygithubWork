"""
一些笔记
_score  单下划线用于警示该变量不要轻易调用
        但可以调用

__score 表示该方法(或性质property)已被python用特定方法隐藏，一般
        情况无法调用， change ! -->  __<name>
        to -->  _<className>__<name>

第三种，加如下标签

@property
def <methodName>(self):
    ...             这是getter


@<methodName>.setter
def <methodName>(self, <parameters>):
    ...             这是setter
"""
import math


class Vector():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, oOther):  # +
        return Vector(self.x + oOther.x, self.y + oOther.y)
        # 因为这里是内部的方法
        # 所以加号 + 还没有被转义成方法，还是函数

    def __sub__(self, oOther):  # -
        return Vector(self.x - oOther.x, self.y - oOther.y)

    def __mul__(self, oOther):  # *
        if isinstance(oOther, Vector):
            return Vector((self.x * oOther.x), (self.y * oOther.y))
        elif isinstance(oOther, (int, float)):
            return Vector((self.x * oOther), (self.y * oOther))
        else:
            raise TypeError('Second value must be a vector or scalar')
    """每一个都应该如上，判断二元运算符右侧的参数类型"""
    def __abs__(self):  # |x|
        return math.sqrt((self.x ** 2) + (self.y ** 2))

    def __eq__(self, oOther):  # ==
        return (self.x == oOther.x) and (self.y == oOther.y)

    def __ne__(self, oOther):  # !=
        return not (self == oOther)
