s,x=map(int,input().split())
l=list(map(int,input().split()))
count=0
for i in l:
    if(x==i):
        count+=1
print(count)
