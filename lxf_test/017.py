# -*- coding: utf-8 -*-
class Student(object):
    pass

def set_age(self, age):
    self.age=age

from types import MethodType
s = Student()
s.set_age = MethodType(set_age, s)
s.set_age(25) # 调用实例方法
print(s.age)
