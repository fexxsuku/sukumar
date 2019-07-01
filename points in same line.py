s,v=map(int,input().split())
s1,v1=map(int,input().split())
s2,v2=map(int,input().split())
if((v1-v)/(s1-s)==(v2-v)/(s2-s)):
    print("yes")
else:
    print("no")
