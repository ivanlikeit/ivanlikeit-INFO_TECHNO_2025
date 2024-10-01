import itertools as iter
enumeration = list(iter.product("012345678",repeat = 5))
counter = 0
numbers = [str(i) for i in range(1,9,2)]

for x in enumeration:
    x = ''.join(x)
    fife = x.find('5')
    if x.count("5") == 1:
        if fife == 0:
            if x[fife+1] not in numbers:
                counter +=1
                continue
        if fife == 4:
            if x[fife-1] not in numbers:
                counter +=1
                continue
        elif fife > 0 and fife < 4:
            if (x[fife -1] not in numbers) and (x[fife +1] not in numbers):
                counter +=1
                continue
        elif fife == (-1):
            pass


print(counter)