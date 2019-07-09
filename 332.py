a,b=map(int,input().split())
l=list(map(int,input().split()))
count=0
for x in range(len(l)):
    if(l[x]==b):
        count=count+1
        break
    else:
        count=0
if(count>0):
    print("yes")
else:
    print("no")
