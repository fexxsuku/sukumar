sv=input()
flag=0
for x in sv:
    if(x.isdigit()):
        flag=1
        break
    else:
        flag=0
if(flag==1):
    print("Yes")
else:
    print("No")
