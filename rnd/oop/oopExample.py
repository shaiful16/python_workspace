
class Student:
    def __init__(self,id,name):
       self.id = id
       self.name = name

    def nameWithId(self):
       return 'id is {} name is {}'.format(self.id,self.name)


student1 = Student(1,"shaiful")
student2 = Student(2,"ferdous")

print(student1.id)
print(student1.name)
print(student2.id)
print(student2.name)

print(student1.nameWithId())
print(student2.nameWithId())
