import random
value = random.randint(3, 10)
elist = [random.randint(1, 100) for _ in range(value)]
elist1 = [elist[0], elist[2], elist[-2]]
print(elist)
print(elist1)
