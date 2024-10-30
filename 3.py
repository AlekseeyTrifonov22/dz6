x1 = int(input("Введите начало диапазона: "))
x2 = int(input("Введите конец диапазона: "))
for i in range(x1,x2 + 1,1):
    if i % 5 == 0 and i % 3 == 0:
        print("Fizz Buzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 != 0 and i % 3 != 0:
        print(i)




