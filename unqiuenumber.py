a=int(input())
n=list(map(int,input().split()))
l=[]
for x in range(a):
    for i in range(x+1,len(n)):
        if(n[i]==n[x]):
          l.append(n[x])
l.sort
l_set=set(l)
for x in l_set:
    print(x,end=" ")
