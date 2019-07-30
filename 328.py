mylist=input()
mylist=list(dict.fromkeys(mylist))
for x in range (len(mylist)):
    print(mylist[x],end="")

