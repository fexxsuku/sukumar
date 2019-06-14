s=int(input())
flag=1
for x in range(2,s//2):
    if(s%x==0):
        flag=1
        break
    else:
        flag=0
if(flag==0 or s==2):
        print("yes")
else:
    print("no")
