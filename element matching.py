n1=int(input())
l1=list(map(int,input().split()))
n2=int(input())
l2=list(map(int,input().split()))
flag=0
if (all(x in l1 for x in l2)):
    flag=1
if(flag==0):
    print("NO")
else:
    print("YES")
