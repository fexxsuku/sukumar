s=list(input())
a=len(s)
if(a%2!=0):
    s[a//2]="*"
else:
    b=a//2
    s[b]="*"
    s[b-1]="*"
for x in s:
    print(str(x),end="")
