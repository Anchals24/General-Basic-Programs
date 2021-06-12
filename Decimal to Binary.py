Num = 1
N = int(input())
Ans = []
while Num <= N:
    B = []
    Number = Num
    while(Number != 0):
        R = Number % 2
        B.append(R)
        Number = Number//2
    B.reverse()
    Binary = ""
    for b in B:
        Binary += str(b)
    Ans.append(Binary)
    Num += 1
print(Ans)


        
        


























































    
