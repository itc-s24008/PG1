prefectures = ['Hokkaido', 'Hokkaido', 'Tokyo', 'Kanagawa']
cities = ['Sapporo', 'Hakodate', 'Minato', 'Yokohama']
populations = [100, 200, 300, 400]
population_dict = {(state,city): population for state, city, population in zip(prefectures, cities, populations)}
print(population_dict)

multiplicated_xy_setdict = {frozenset([x, y]): x*y for x in range(2) for y in range(2)}
print(multiplicated_xy_setdict)

print({0: {0: 0, 1: 0, 2:0}, 1: {0: 0, 1: 1, 2: 2}, 2: {0: 0, 1: 2, 2: 4}})

multiplicated_xy_setdict = {}
I = 3
J = 3
for i in range(I):
    multiplicated_xy_setdict[i] = {}
    for j in range(J):
        multiplicated_xy_setdict[i][j] = i*j
print(multiplicated_xy_setdict)

multiplicated_xy_setdict = {i:{j:(i*j) for j in range(J)}for i in range(I)}
print(multiplicated_xy_setdict)
