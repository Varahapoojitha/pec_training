#Inheritance: This mechanism allows the new objects to take on the properties of existing objects.
#Types: single,Multilevel,Hierarchial,Multiple
#Multiple inheritance is acheived only using python and java does not support multiple Inheritance
#Sub Class or Derived Class or Child Class
#Base Class or Super class or Parent Class
'''Single Inheritance'''


class A:
  name = "Mukhesh"
  age = 36


class B(A):
  age = 10


obj = B()
obj.name = "Ramesh"
print(obj.age)
print(obj.name)
