#2_Dimensional_Array
#How to access the elements of a 2D Matrix?

M = [[1,2] , [2,3,4] , [2,3,2]]
for m in M:
    for c in m:
        print(c, end= " ")
    print()

#Complexity : O(M*m) 

#How to take a 2D Array as an input?

#row 14 means n = number of rows.

n = int(input()) 
ans = []  
for i in range(n):
    rows = input()
    rows = rows.split()
    r = []
    for x in rows:
        r.append(int(x))
    ans.append(r)
print(ans)

