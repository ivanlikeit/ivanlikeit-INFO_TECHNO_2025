import itertools as like

count = 0
enumeration = list(like.product('полина', repeat=4))

vowel = list(like.product('оиа', repeat=2))
consonant = list(like.product('плн', repeat=2))

for x in enumeration:
    x = ''.join(x)
    if ((x[0:2] not in vowel) or (x[0:2] not in consonant)) and ((x[1:3] not in vowel) or (x[1:3] not in consonant)) and ((x[2:4] not in vowel) or (x[2:4] not in consonant)):
        count +=1

print(count)



