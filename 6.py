a = list(map(int, input('Введите первый список через пробел: ').split()))
b = list(map(int, input('Введите второй список через пробел: ').split()))
cross = []
for i in a:
    if i in b:
        cross.append(i)
        b.pop(b.index(i))
print(*cross)
