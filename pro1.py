s=int(input())
m=[]
for i in range(0,s):
    l=input()
    m.append(l)
text =m[0][0]
for y in range(0,len(m)):
    for x in range(0,len(m[y])):
        result=m[y].startswith(text)
if(result==True):
    text=m[0][0:x+1]
    print(text)
