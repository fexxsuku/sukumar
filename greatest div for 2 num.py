s,v=map(int,(input().split()))
a=0
for x in range(2,v):
        if(s%x==0 and v%x==0):
            a=x
print(a)

