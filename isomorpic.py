str1,str2=map(str,input().split())
if(len(set(str1))==len(set(str2))):
    print("yes")
else:
    print("no")
