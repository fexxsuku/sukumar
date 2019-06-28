    
ak1=list(map(int,input().split()))
bk1=list(map(int,input().split()))
for i in range(0,ak1[1]):
  bk1=[bk1[-1]] + bk1[:-1]
print(*bk1,end=' ')
