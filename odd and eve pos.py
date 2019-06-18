l=input()
a=[]
b=[]
for x in range(0,len(l)):
    if(x%2==0):
        a.append(l[x])
    else:
        b.append(l[x])
print("".join(a),"".join(b))
