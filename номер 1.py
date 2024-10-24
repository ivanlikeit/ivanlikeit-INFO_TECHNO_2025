import itertools as iter
enumeration = list(iter.product('аекнрс', repeat = 10))
bukva = list('кнрс')
counter = 0
globalCounter = 0
for x in enumeration:
    x = ''.join(x)
    counter +=1
    if counter % 3 == 0 and x[0] in bukva and x.count('р') == 1:
        globalCounter +=1
print(globalCounter)
