# -*- coding: utf-8 -*-
import pickle
import json

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
        
    


def show():
    d = dict(name='Bob', age=20, score=88)
    pickle.dumps(d)
    f = open('dump.txt', 'wb')
    pickle.dump(d, f)
    f.close()
    f = open('dump.txt', 'rb')
    d = pickle.load(f)
    f.close()
    print(d)
    d = dict(name='Bob', age=20, score=88)
    json.dumps(d)
    json_str = '{"age": 20, "score": 88, "name": "Bob"}'
    d=json.loads(json_str)
    print(d)
    
def student2dict(std):
        return {
            'name': std.name,
            'age': std.age,
            'score': std.score
        }
    
def testJson():
    s = Student('Bob', 20, 88)
    print(json.dumps(s,default=lambda obj: obj.__dict__))

if __name__ == '__main__':
    testJson()

