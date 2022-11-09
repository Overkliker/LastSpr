inp = input()
l1 = []

for i in inp:
    if inp.index(i) % 2 == 0:
        l1.append(i.lower())

    else:
        l1.append(i.upper())

print("".join(l1))

