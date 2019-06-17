s=int(input())
flag=1
for x in range(2,s//2):
    if(s%x==0):
        flag=0
        break
    else:
        flag=1
if(flag==0 or s==1):
        print("yes")
else:
    print("no")
