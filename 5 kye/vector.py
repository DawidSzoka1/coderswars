import math


class Vector:
    def __init__(self, vec):
        self.vec = vec

    def check_leng(self, cls):
        return True if len(self.vec) == len(cls.vec) else False

    def add(self, cls):
        if not self.check_leng(cls):
            raise Exception("exepction")
        num = []
        for i in range(len(self.vec)):
            num.append(cls.vec[i] + self.vec[i])
        return Vector(num)

    def subtract(self, cls):
        if not self.check_leng(cls):
            raise Exception("exepction")
        num = []
        for i in range(len(self.vec)):
            num.append(self.vec[i] - cls.vec[i])
        return Vector(num)

    def dot(self, cls):
        if not self.check_leng(cls):
            raise Exception("exepction")
        num = 0
        for i in range(len(self.vec)):
            num += cls.vec[i] * self.vec[i]
        return num

    def norm(self):
        sqr = 0
        for i in range(len(self.vec)):
            sqr += self.vec[i] ** 2
        return math.sqrt(sqr)

    def equals(self, cls):
        return self.vec == cls.vec

    def __str__(self):
        return str(self.vec).replace('[', '(').replace(']', ')').replace(' ', '')
