#square of numbers
n=int(input('Enter the number:'))
s=str(n)
l=list(s)
l=list(map(int,l))
for i in l:
  print(i*i)
