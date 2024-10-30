x1 = int(input("Введите начало диапазона: "))
x2 = int(input("Введите конец диапазона: "))
for i in range(x1,x2 + 1,1):
    print(f"{i}", end=" ")
print("\b")
for i in range(x2,x1 -1, -1):
    print(f"{i}", end=" ")
print("\b")
for i in range(x1,x2 + 1,1):
    if i % 7 == 0:
        print(f"{i}", end=" ")
print("\b")
counter = 0
for i in range(x1,x2 + 1,1):
    if i % 5 == 0:
        counter+=1
print(counter)