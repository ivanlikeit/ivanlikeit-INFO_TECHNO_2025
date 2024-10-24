counter = 0
def trey(a):
    s = ''
    while a >0:
        l = str(a%3)
        s = l+s
        a=a//3
    return s
def five(a):
    s = ''
    while a >0:
        l = str(a % 5)
        s = l + s
        a = a // 5
    return s

for i in range(1,96):
    if trey(i)[::-1][:2][::-1] == '21' and five(i)[0] == "3":
        counter += i
print(counter)