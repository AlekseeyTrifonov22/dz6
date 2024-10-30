x1 = int(input("Введите начало диапазона: "))
x2 = int(input("Введите конец диапазона: "))
for i in range(x1,x2 + 1,1):
    if i % 7 == 0:
        print(i )