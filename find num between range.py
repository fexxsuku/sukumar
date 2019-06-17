s=int(input())
sv1,sv2=map(int,input().split())
flag=0
for sv in range (sv1+1,sv2-1):
    if(s==sv):
        flag=1
        break
    else:
        flag=0
        
if(flag==1):
    print("yes")
else:
    print("no")
