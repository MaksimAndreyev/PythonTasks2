with open('file.txt') as f:
    n = int(input('Введите число n: '))
    a = []
    multiply = 1
    for i in range(-n, n+1):
        a.append(i)
    for i in f:
        multiply *= a[int(i)]
    print(multiply)
