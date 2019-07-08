s1,s2,s3=map(str,input().split())
a=int(s3)
count=0
for x in range(0,len(s1)):
    if(s1[x]!=s2[x]):
        count=count+1
if(count==a):
    print("yes")
else:
    print("no")
