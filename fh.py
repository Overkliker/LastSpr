from tabulate import tabulate


last = [4.95, 9.95, 14.95, 19.95, 24.95]
sale = [float('{:.3f}'.format((i / 100) * 60)) for i in last]
tab = [["last price $", *last], ["sale price $", *sale]]

print(tabulate(tab))
