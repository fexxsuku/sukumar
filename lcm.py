def gcd(s,v):
    if(v==0):
        return s
    else:
        return gcd(v,s%v)
s1,v1=map(int,input().split())
LCM=(s1*v1)/gcd(s1,v1)
print(int(LCM))
