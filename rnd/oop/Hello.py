import datetime

class Student:
    def __init__(self,id,name):
       self.id = id
       self.name = name

    def nameWithId(self):
       return 'id is {} name is {}'.format(self.id,self.name)


student1 = Student(1,"shaiful")

print(type(student1))

k0=500
k1=60.95
k2="shaiful"
k3=True
print(type(k0))
print(type(k1))
print(type(k2))
print(type(k3))



def getTemparatureData( ):
   #this fn will get current temp
   return  51

maxTemparatuer=50
minTemparatuer=20

for i in range(1,10,1):
   if(getTemparatureData( ) < minTemparatuer  ):
      print("temp is low")
   if(getTemparatureData( ) > maxTemparatuer ):
      print("temp is high")


