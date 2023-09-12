import math
a = int(input("сторона а: "))
b = int(input("сторона б: "))
c = int(input("сторона г: "))
p = (a+b+c) / 2
s = math.sqrt(p*(p-a)*(p-b)*(p-c))
print(s)