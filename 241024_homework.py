import itertools as iter
lisa = (iter.product("дракон", repeat = 8))
counter = 0
for x in lisa:
  if x.count("а") == 1 and x.count("о")== 1:
    counter +=1
print(counter)