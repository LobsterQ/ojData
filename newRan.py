
import random

a = []
a.append(2)
a.append(1000)
a.append(10000)
for i in range (13):
    a.append(random.randint(5, 1000))

for i in range(14):
    a.append(random.randint(1000, 10000))
b = []
a.sort()
for i in range(len(a)):
    b.append(random.randint(0, min(a[i] * (a[i] - 1) / 2, 1000)))

print(a)
print(b)