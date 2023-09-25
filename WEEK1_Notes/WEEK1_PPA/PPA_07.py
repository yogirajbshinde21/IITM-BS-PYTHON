number = input()
number = int(number)
d1 = number // 10000
d2 = (number // 1000) % 10
d3 = (number // 100) % 10
d4 = (number // 10) % 10
d5 = (number // 1) % 10

print(d1+d2+d3+d4+d5)