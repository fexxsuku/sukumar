a = int(input())
sv = [int(x) for x in input().split()]
for i in range(len(sv)-1):
  if(sv[i]>sv[i+1]):
    print(i)
