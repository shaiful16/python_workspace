from flask import json

class Student:
    def __init__(self,id,name):
       self.id = id
       self.name = name

    def nameWithId(self):
       return 'id is {} name is {}'.format(self.id,self.name)

student1 = Student(1,"shaiful")

print(json.dumps(student1.__dict__))