x = str(input('введите '))
d = len(x)  # длина строки
print(x[2])
print(x[d-2])
print(x[0:5])
print(x[0:-2])
print(x[0:d:2])
print(x[1:d:2])
print('?')  # не понимаю почему не работает x[0:d:-1]
print('?')  # не понимаю почему не работает x[0:d:-2]
print(d)