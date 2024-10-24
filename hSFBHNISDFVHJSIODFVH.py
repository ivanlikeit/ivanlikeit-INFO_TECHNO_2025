counter = 0
spisok = list('abcdefg')
def much(a):
    s = ''
    while a >0:
        l = str(a%17)
        if int(l) <=9:
            s = l+s
        if int(l) > 9:
            s = spisok[int(str(l)[1])] + s
        a=a//17
    return s

for i in range(1,1001):

    if much(i)[0] == '3' and much(i)[-1] == 'd':
        counter+=1
print(counter)
