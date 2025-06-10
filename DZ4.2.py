elist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a, b, c, d, e, f, g, h, i, j = elist
z = (a + c + e + g + i) * elist[-1]
print(z)  # тобто так потрібно було? воно працює - але ж

elist = []
while True:
    value = input("enter a number: ")
    if value == "":
        break
    if not value.isdigit():
        print("only digits")
        continue
    value = int(value)
    elist.append(value)
x = 0
i = 0
y = len(elist)
while i < y:
    x += elist[i]
    i += 2
    print(elist)
result = x * elist[-1]
print(result)
