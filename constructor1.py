class Student:
    student_name=""
    def __init__(self,name): 
        print("obj created")
        print(name)
s1=Student("mukesh")

print("_______")
class Myname:
    myname="No name"
    def __init__(self,name):
        print("obj created")
        print(self.myname)#here by using self. we can access class variables in constructor
s3=Myname("muk")

print("_______")