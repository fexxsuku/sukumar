input_variable1,input_variable2=map(int,input().split())
temp=0;
var1=[int(a)for a in input().split()]
for i in range(0,len(var1)-1):
    for j in range(1,len(var1)):
        if var1[i]+var1[j]==input_variable2:
            temp=temp+1
            break
        break
if temp>=1:
    print("yes")
else:
    print("no")
