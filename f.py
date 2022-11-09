l1 = []

inp = int(input())

if inp == 0:
    print("Вы ввели 0")
    exit()

l1.append(inp)
while inp != 0:
    inp = int(input())
    l1.append(inp)

print(sum(l1[:-1]) / len(l1[:-1]))
