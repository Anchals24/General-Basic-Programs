S = input()
d = {}
print(d)
for c in S:
    print(d)
    if c in d:
        d[c] += 1
        print(d)
    else:
        d[c] = 1
        print(d)



