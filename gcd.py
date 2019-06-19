def gcd(s,v):
    if(v==0):
        return s
    else:
        return gcd(v,s%v)

s1,v1=map(int,input().split())
print(gcd(s1,v1))
