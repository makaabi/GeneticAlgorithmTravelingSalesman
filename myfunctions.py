import matplotlib.pyplot as plt

# get cities info
def getCities(src):
    cities = []
    f = open(src)
    for i in f.readlines():
        node_city_val = i.split()
        cities.append(
            [node_city_val[0], float(node_city_val[1]), float(node_city_val[2])]
        )

    return cities

# draw cities and answer map
def showMap(city, solution):
    for j in city:
        plt.plot(j[1], j[2], "ro")
        plt.annotate(j[0], (j[1], j[2]))

    for i in range(len(solution[1])):
        try:
            first = solution[1][i]
            secend = solution[1][i + 1]

            plt.plot([first[1], secend[1]], [first[2], secend[2]], "gray")
        except:
            continue

    first = solution[1][0]
    secend = solution[1][-1]
    plt.plot([first[1], secend[1]], [first[2], secend[2]], "gray")
    plt.title('GA project 2023',loc='left')
    plt.title('Mohamed Amine Kaabi', loc='right')


    plt.show()
