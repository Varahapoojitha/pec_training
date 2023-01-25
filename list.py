''' **LIST**
1. list.append(element)
2. list.pop(index)
   - index is not mandatory
   - returns popped element
3. list.remove(element)
   - element is mandatory
   - returns None
4. list.insert(index,element)
  - at a certain index the element is added
  - return None
5. list1.extend(list2)
  - list2 elements extended to list1
6. list.count(element)
  - counts the frequency of element in the list
7. len(list)
  - returns the length of list
8. list2=list1.copy()
  - copies list1 elements into list2
9. list.reverse()
  - reverse the list
10. list.sort(reverse=True/False)
  - sorts the list in ascending order
  - reverse is optional
  - perform operation on same list
11. list2=sorted(list,reverse=True/False)
  - sort the list
  - perform the operations using the list elements and stores in another list
  - reverse is optional
12. list.clear()
  - clears the list elements '''

#list
l=[]
l1=[10,20]
l.append(1)
l.append([1,2,3])
l.append('hello')
l.append(5.26)
print('after using append',l)
l.insert(1,'hai')
print('after using insert',l)
l1.extend(l)
print('after extended',l1)
l2=l1.copy()
print('after copying',l2)
  