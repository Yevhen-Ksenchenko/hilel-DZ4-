elist = []
while True:
    value = input("Enter value (press enter without value for the end): ")
    if value == "":
        break
    if not value.isdigit():
        print("only digits")
        continue
    elist.append(int(value)) # три дні мучав я цей код))) доки не знайшов помилку - треба int добавити
print(elist)
zero = elist.count(0)
print("your have a", zero, "zeros")

x = 0
y = len(elist)
while x < y:
    if elist[x] == 0:
        z = elist.pop(x)
        y -= 1
        elist.append(z)
    else:
        x += 1

print(elist)
