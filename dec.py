lim=int(input())
li=list(map(int,input().split()))
li.sort(reverse=True)
for x in li:
    print(x,end="")
