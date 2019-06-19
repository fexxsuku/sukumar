s=input()
flag=0
for x in s:
    if(s.count(x)>1):
        flag=1
        break
if(flag==1):
    print("No")
else:
    print("Yes")
