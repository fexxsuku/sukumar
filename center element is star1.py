sv=list(input())
a=len(sv)
if(a%2!=0):
    sv[a//2]="*"
else:
    b=a//2
    sv[b]="*"
    sv[b-1]="*"
for x in sv:
    print(str(x),end="")
