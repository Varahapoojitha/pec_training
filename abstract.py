#same methods diff signatures :method overloading 
#spring framework in industries nowadays.it includes many annotations
#same methods same sig diff classes : method overriding
#abstract class will contain abs method with func def without bodies and these bodies are defined in their child classes.
#abc : stands for Abstract base class (package)
#ABC : is a class
#abstraction is a process of hiding data using abstrast classes

from abc import ABC,abstractmethod

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
ob.calculate_area()