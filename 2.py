# нод

a = int(input('Введите а: '))
b = int(input('Введите в: '))
while a != b:
    if a > b:
        a = a - b
    else:
        b = b - a

print(a)