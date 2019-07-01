s=int(input())
li=list(map(str,input().split()))
li.sort(reverse=True)

for x in range(0,len(li)):
    print(li[x],end=" ")
