"""
Reversing a list:
Various methods of reversing a list :
- by creating another list.
- by updating the existing list.

"""

# Method1: using range function(iterating towards backward) property:
#>> does not update the existing list

L1 = [1,2,3,4]
Reverselist = []
leng = len(L1)-1
for i in range(leng , -1 , -1):
    Reverselist.append(L1[i])
print(Reverselist)

#Method2: using simple "while loop"
#>> does not update the existing list

L2 = [2,3,41,65]
Reverselist1 = []
lengg = len(L2) -1 
while lengg != -1:
    Reverselist1.append(L2[lengg])
    lengg -=1
print(Reverselist1)

#Method3 : Swapping the numbers (len(N//2))
#>> update the existing list
"""MOST EFFICIENT APPRAOCH"""

List = [23 , 12, 11, 10 , 76]
mid = len(List) // 2
initial = 0
last = -1
while (mid-1) > -1:
    temp = List[initial]
    List[initial] = List[last]
    List[last] = temp
    mid -= 1
    last -=1 
    initial += 1
print(List)

#Method4 : Using the reverse() 
# >> update the existing list

L3 = [1 ,2,3,4]
L3.reverse()
print(L3)

#Method5 : Using the reversed()
#>> does not update the existing list.
# create a reverse iterator for an existing list or sequence object.

mylist = [11 ,2 , 233, 4]
myreversedlist = []
for i in reversed(mylist):
    myreversedlist.append(i)
print(myreversedlist)

        #or

L4 = [22 , 12, 12, 123]
Reversedlist = list(reversed(L4))
print(Reversedlist)

#Method6 : using "slicing" concept

mylist2 = [2 , 12, 4 , 15 , 16]
print(mylist2[::-1])

#>>> Demerits : Reversing a list this way takes up a more memory compared to an in-place reversal
# because it creates a (shallow) copy of the list. 
# And creating the copy requires allocating enough space to hold all of the existing elements.
# The biggest downside to reversing a list with the slicing syntax is that 
# it uses a more advanced Python feature that some people would say is “arcane.” 
# “[::-1]” slicing syntax does not communicate clearly enough that it creates a reversed copy of the original list.

