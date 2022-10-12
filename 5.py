from random import shuffle, randint
a = list(map(int, input('Введите список через пробел: ').split()))
#Первый вариант
shuffle(a)
print(*a)
#Второй вариант
for i in range(len(a)):
    x = randint(0, len(a)-1)
    y = randint(0, len(a)-1)
    a[x], a[y] = a[y], a[x]
print(*a)
