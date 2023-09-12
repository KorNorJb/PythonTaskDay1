a = int(input("число: "))
sum = 0
while a>0:
    d = a % 10
    sum += d
    a //= 10
print(sum)