s,x=map(int,input().split())
l=list(map(int,input().split()))
flag=0
for i in l:
    if(x==i):
        flag=1
if(flag==1):        
    print("yes")
else:
     print("no")
