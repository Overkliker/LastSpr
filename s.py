sum = 0.00

while True:
    inp = int(input())

    if inp != 0 and inp <= 2:
        sum += 0

    elif 2 < inp <= 12:
        sum += 14

    elif 12 < inp <= 65:
        sum += 23

    elif 65 < inp:
        sum += 18

    elif inp == 0:
        break

print(sum)