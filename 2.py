n = int(input('Введите число: '))
a = [1]
for i in range(2, n+1):
    a.append(i*a[-1])
print(*a)
