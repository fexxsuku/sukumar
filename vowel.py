sv1=input()
flag=0
for sv in sv1:
    if(sv=='a' or sv=='e' or sv=='i' or sv=='o' or sv=='u' or sv=='A' or sv=='E' or sv=='I' or sv=='O' or sv=='U'):
        flag=1
    else:
        flag=0
if(flag==1):
    print("yes")
else:
    print("no")
