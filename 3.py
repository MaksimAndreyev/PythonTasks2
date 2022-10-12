n = int(input('Введите число n: '))
a = []
for i in range(1, n+1):
    a.append((1 + 1/i) ** i)
print(sum(a))
