sv=int(input())
l=list(map(int,input().split()))
flag=1
l1=[]
for x in range (len(l)):
    for i in range(x+1,len(l)):
        if(l[x]<l[i]):
            flag=0
            break
        else:
            flag=1
    if (flag==1):
        l1.append(l[x])
print(*l1)
print(max(l))
