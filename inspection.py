import numpy as np
from matplotlib import pyplot as plt
N = 10000
day = 720


def analyze(intervals):
    number_in_day, buses_in_day, buf = [], [], []
    sum, bus = 0, 1
    max=0
    inter = np.asarray(intervals)
    for i in range(N):
        sum += inter[i]
        bus += 1
        buf.append(inter[i])
        if sum >= day:
            number_in_day.append(bus)
            buses_in_day.append(buf)
            if bus > max:
                max = bus
            sum, bus = 0, 1
            buf = list()
    number_in_day = np.array(number_in_day)
    plt.hist(number_in_day)
    plt.title("Гистограмма количества автобусов в день")
    plt.xlabel("Количество автобусов за день")
    plt.ylabel("Количество дней")
    plt.show()

    bus = np.random.randint(1, max)
    print("Выбранный автобус:", bus)
    people_in_bus = []
    for i in range(len(buses_in_day)):
        if bus < len(buses_in_day[i]):
            people_in_bus.append(buses_in_day[i][bus])
    people_in_bus = np.array(people_in_bus)
    plt.hist(people_in_bus)
    plt.title("Гистограмма случайный выбор автобуса")
    plt.xlabel('Количество человек в автобусе')
    plt.ylabel("Количество дней")
    plt.show()
    print("Мат ожидание:", people_in_bus.mean())
    print("Дисперсия:", people_in_bus.var())

    plt.title("Гистограмма случайный выбор времени")
    people_in_bus = list()
    minute = np.random.randint(0, 721)
    print("Выбранная минута:", minute)
    for i in range(len(buses_in_day)):
        sum = 0
        for j in range(len(buses_in_day[i])):
            sum += buses_in_day[i][j]
            if sum >= minute:
                people_in_bus.append(buses_in_day[i][j])
                break
    people_in_bus = np.array(people_in_bus)
    plt.hist(people_in_bus)
    plt.xlabel('Количество человек в автобусе')
    plt.ylabel("Количество дней")
    plt.show()
    print("Мат ожидание:", people_in_bus.mean())
    print("Дисперсия:", people_in_bus.var())


analyze(np.random.randint(1, 3, N)*5)
analyze(np.random.exponential(10, N))
