lim=int(input())
v1=0
v2=1
for i in range(0,lim):
    print(v2,end=" ")
    sum=v1+v2
    v1=v2
    v2=sum
