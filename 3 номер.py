import itertools as iter
enumeration = list(iter.permutations('0123456789', r = 6))
numbers = list('13579')
count = 0
for x in enumeration:
    x = ''.join(x)
    if int(x) % 5 == 0 and x[0] != '0':
        for i in range(6): x = x.replace(x[i],'*') if x[i] in numbers else x.replace(x[i],'@')
        if '@@' not in x and '**' not in x:
            count +=1
print(count)