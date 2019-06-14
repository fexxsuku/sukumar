str=input().split()
l=[]
for i in str:
    l.append(i[::-1])
print(*l)
