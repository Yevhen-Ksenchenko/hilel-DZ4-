# ось так теж можна)) всі умови виконані)) - ще куча домашок попереду
elist = input("Enter from 3 to 10 numders: ")
if not elist.isdigit():
    print("Only numbers")
elif len(elist) < 3:
    print("more")
elif len(elist) > 10:
    print("less")
    elist = str(elist)
else:

    elist1 = [elist[0], elist[2], elist[-2]]
    print('[', *elist, ']', sep=" ")
    print(elist1)
