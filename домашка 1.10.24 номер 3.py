import itertools as like

count = 0
enumeration = list(like.permutations('ярослав', r=5))

vowel = list(like.permutations("яоа", r=2))

for x in enumeration:

    x = ''.join(x)
    if (x.count("я") + x.count("о") + x.count("а")) < (x.count("р") + x.count("с") + x.count("л") + x.count("в")) \
            and ((x[0] + x[1] not in vowel) or (x[1] + x[2] not in vowel) or (x[2] + x[3] not in vowel) or (
            x[3] + x[4] not in vowel)):
        count += 1
print(count)