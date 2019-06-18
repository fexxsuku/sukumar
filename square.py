n1,n2=list(map(int,input().split()))
f=n1*n2
for i in range(0,f+1):
  if(i**2==0):
    print("yes")
    break;
else:
  print("no")
  
