n=int(input())
l=list(map(int,input().split()))
for i in range(0,len(l)):
    if(l[i]%2==0 and i%2!=0):
            print(l[i],end=" ")
    elif(l[i]%2!=0 and i%2==0):
            print(l[i],end=" ")
