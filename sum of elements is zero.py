sn=int(input())
sl=list(map(int,input().split()))
for i in range(0,sn-2):
    for j in range(i+1,sn-1):
        for k in range(j+1,sn):
            if(sl[i]+sl[j]==0):
                print(sl[i],sl[j])
