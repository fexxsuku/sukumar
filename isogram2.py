sb=input()
flagb=0

for x in sb:
    if(sb.count(x)>1):
        flagb=1
        break

if(flagb==1):
    print("No")
else:
    print("Yes")
