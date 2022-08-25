# номер 4
n = int(input('введите'))
s = 0
for x in range(1, n+1):
    s = s+x
for y in range(n-1):
    a = int(input())
    s = s - a
print(s)