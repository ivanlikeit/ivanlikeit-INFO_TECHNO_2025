import itertools as iter
enumeration = list(iter.product("метро",repeat = 4))
counter = 0
vowel = ['е','о']
consonant = ['м','т','р']
for x in enumeration:
    x = ''.join(x)
    if x[0] in consonant and x[3] in vowel:
        counter +=1
print(counter)


