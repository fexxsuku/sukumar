import math
count=0
a,b=map(int,input().split())
for x in range(a+1,b):
    if(math.sqrt(x)*math.sqrt(x)==x):
        count=count+1
print(count)
