s,v=map(int,input().split())
l=list(map(int,input().split()))
l1=[]
for x in range(0,len(l)):
    if(l[x]%2!=0):
        l1.append(l[x])
print(l1[v-1])


