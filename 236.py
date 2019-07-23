a,b=map(str,input().split())
l=[]
count=0
for x in range(len(a)):
    l.append(a[x])
for y in range(len(l)):
    if(l[y]==b):
        count=count+1
print(count)
