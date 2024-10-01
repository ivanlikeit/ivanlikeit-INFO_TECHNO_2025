import itertools as iter
enumeration = list(iter.product('векно',repeat = 5))
counter = 0

for x in enumeration:
    x =''.join(x)
    counter +=1
    if x[0] == 'о':
        print(counter)
        break