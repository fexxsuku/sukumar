a=str(input())
l=[]
for x in range(0,len(a),3):
    l.append(a[x])
for y in range(len(l)):
    print(l[y],end="")
