x,z=map(int,input().split())
l=list(map(int,input().split()))
l.sort(reverse=True)
print(l[z-1])
