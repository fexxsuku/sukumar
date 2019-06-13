sv=input()
j=1
for i in range(len(sv)-1):
    s=sv[i]+sv[i+1]
    p=int(s)
    if p<=26 and sv[i]!="0":
        j+=1
if j==3:
    print(j)
else:
    print(j+(j-1)//2)
