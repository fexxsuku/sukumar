s,v=map(int,input().split())
s1,v1=map(int,input().split())
s2,v2=map(int,input().split())
if(s==s1 and s1==s2 and s2==s1 or v==v1 and v1==v2 and v2==v1):
    print("yes")
else:
    print("no")
