""" Find out all the possible substrings of a string.......

substring is a sequence of characters within another string 
for example :

String : abc
Possible Substrings : "a" , "b" , "c" , "ab" , "bc" , "abc"

"""


S = input()
Ans = []
leng = len(S)
k = 1
while k <= leng:
    for s in range(leng):
        Substrings = ""
        if s + k <= leng:
            Substrings = Substrings.join(S[s:s+k])
            Ans.append(Substrings)
    k += 1
print(Ans)
