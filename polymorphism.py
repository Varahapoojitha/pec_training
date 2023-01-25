class A:
    def method_1(self,a,b):
        print("sum of 2 nums:",a+b)
class B(A):
    def method_1(self,a,b):
        print("mul of 2 nums:",a*b)
obj=B()
obj.method_1(10,20)
class A:
    def method_1(self,a,b):
        print("sum of 2 nums:",a+b)
class B(A):
    def method_1(self,a,b):
        print("diff of 2 nums:",a-b)
    def method_1(self,abc): #here method 1 is being updated
        print("value is",abc)
obj=B()
obj.method_1(10) #method with 1 arg

"""from abc import ABC,abstractmethod

class Area(ABC):
    @abstractmethod #annotation: always starts with '@' symbol
    def calculate_area(self):
        pass
    
class Square(Area):
    def calculate_area(self):
        print("in Square method")
      
class Rectangle(Area):
    pass

ob = Square()
ob.calculate_area()"""