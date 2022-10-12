n = input('Введите число: ')
s = 0
for i in n:
    if i == ',' or i == '.':
        continue
    s += int(i)
print(s)
