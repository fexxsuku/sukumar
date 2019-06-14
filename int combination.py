from itertools import permutations 
sv=input()
per=permutations(sv)
for x in list (per):
    print(''.join(x))
