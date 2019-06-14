s=input()
flag=0
for x in s:
    if(x=="1" or x=="0"):
        flag=1
    else:
        flag=0
        break
if(flag==1):
    print("yes")
else:
    print("no")  
