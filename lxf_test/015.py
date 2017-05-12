# -*- coding: utf-8 -*-
class Student(object):
    __slots__ = ('name', 'age')
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.print_score()
lisa.print_score()

def readImage(fp):
    if hasattr(fp, 'read'):
        return readData(fp)
    return None
