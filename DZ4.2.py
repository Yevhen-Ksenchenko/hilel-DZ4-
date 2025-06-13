elist = []
while True:
    value = input("enter a number (to stop - empty Enter): ")
    if value == "":
        break
    if not value.isdigit():
        print("only digits")
        continue
    value = int(value)
    elist.append(value)
if not elist:
    print(elist)
    print(0)
else:
    x = 0
    i = 0
    # y = len(elist)
    while i < len(elist):
        x += elist[i]
        i += 2
    print(elist)
    result = x * elist[-1]
    print(result)
