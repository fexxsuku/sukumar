sv1,sv2,sv3=svap(int,input().split())
sv4=0
for i in range(1,sv3+1):
  sv4+=sv1+(i-1)*sv2
print(sv4)
