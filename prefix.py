a=input()
b=len(a)
count=0
l=list(map(str,input().split()))
for x in range(0,len(l)):
   if(l[x][0:b]==a):
       count=count+1
print(count)
