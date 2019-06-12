v=input()
v=list(v)
v[::2],v[1::2]=v[1::2],v[::2]
print(*v,sep="")
