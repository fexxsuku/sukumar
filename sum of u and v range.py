a,b=map(int ,input().split())
l=list(map(int,input().split()))
for x in range(b):
    c=[]
    u,v=map(int,input().split())
    for y in range(u-1,v):
        c.append(l[y])
    a=sum(c)
    print(a)
    
