p,q=map(int,input().split())
li=list()
for x in range(p,q+1):
    cnt=0
    for i in range(1,x+1):
        if x%i==0:
            cnt+=1
    if cnt==2:
        li.append(x)
print(len(li))
