a=int(input("enter a:"))
b=int(input("enter b:"))

try:
   print(a/b)
except:
    print("b cannot be 0")
print("after the error")

print("____")