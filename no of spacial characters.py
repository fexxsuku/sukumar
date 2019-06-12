n=input()
sum=0
for x in n:
    if(x.isdigit() or x.isalpha()!=True or x==" "):
        sum+=1
print(sum)
