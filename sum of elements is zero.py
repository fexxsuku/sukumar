e=int(input())
x=list(map(int,input().split()))
l=max(x)
e,f=0,0
for i in range(0,len(x)):
  for j in range(i+1,len(x)):
    if abs(x[i]+x[j])<l:
      e,f=x[i],x[j]
      l=abs(e+f)
print(e,f)
