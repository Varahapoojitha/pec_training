''' **Type Casting**
**The string characters must be numbers for converting the type of string into int and float**
1. string-int
   - int(string)
2. string-float
   - float(string)
3. int-string
   - str(integer)
4. string-list
   - list(string)
5. list type conversion
   - str-int
     - list(map(int,list))
   - str-float
     - list(map(float,list))
   - int-str
     - list(map(str,list)) '''

a=['0','1']
l=list(map(int,a))
print(l)
    
    