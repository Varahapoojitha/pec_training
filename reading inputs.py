''' **Reading inputs**
1. reading string
   - input()
2. reading integer
   - int(input())
3. reading float
   - float(input()) '''

#programming session
#calculator
a=int(input('Enter a:'))
b=int(input('Enter b:'))
c=input()
if c=='+':
  print(a,'+',b,'=',a+b)
elif c=='-':
  print(a,'-',b,'=',a-b)
elif c=='*':
  print(a,'*',b,'=',a*b)
elif c=='/':
  if b==0:
    print("Can't do division")
  else:
    print(a,'/',b,'=',a/b)
elif c=="//":
  print(a,'//',b,'=',a//b)
else:
  print(a,'%',b,'=',a%b)
   
