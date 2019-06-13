n=int(input())
l=[]
array=list(map(int,input().split()))
for x in range(0,n):
    if(array[x]==x):
        l.append(x)
if(len(l)==0):
    print("-1")
l.sort()
for x in l:
    print(x,end=" ")
