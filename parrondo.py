import random

import numpy as np
from matplotlib import pyplot as plt
N, n = 10000, 1000

def casinoA(cash):
    buf = random.choices([1, -1], weights=[0.49, 0.59], k=1)
    if buf[0] < 0:
        return cash-1
    else:
        return cash+1


def casinoB(cash):
    if cash%3 == 0:
        buf = random.choices([1, -1], weights=[0.09, 0.91], k=1)
    else:
        buf = random.choices([1, -1], weights=[0.74, 0.26], k=1)
    if buf[0] < 0:
        return cash-1
    else:
        return cash+1


athosArr = []
partosArr = []
aramisArr = []
for i in range(N):
    athos = 1000
    partos = 1000
    aramis = 1000
    currentAthos = []
    currentPartos = []
    currentAramis = []
    for j in range(n):
        athos = casinoA(athos)
        currentAthos.append(athos)
        partos = casinoB(partos)
        currentPartos.append(partos)
        rand = np.random.randint(0, 2)
        if rand == 0:
            aramis = casinoA(aramis)
        else:
            aramis = casinoB(aramis)
        currentAramis.append(aramis)
    athosArr.append(currentAthos)
    partosArr.append(currentPartos)
    aramisArr.append(currentAramis)

averageAthos = np.array(athosArr).mean(axis=0)
for i in range(10):
    athosIndex = np.random.randint(0, N+1)
    currentAthos = np.array(athosArr[athosIndex])
    plt.plot(currentAthos, linewidth=1)
plt.plot(averageAthos, linewidth=2, color='black', label='Среднее')
plt.title('Атос')
plt.ylabel('Богатство')
plt.xlabel('Игра')
plt.legend()
plt.show()

averagePartos = np.array(partosArr).mean(axis=0)
for i in range(10):
    partosIndex = np.random.randint(0, N)
    currentPartos = np.array(partosArr[partosIndex])
    plt.plot(currentPartos, linewidth=1)
plt.plot(averagePartos, linewidth=2, color='black', label='Среднее')
plt.title('Партос')
plt.ylabel('Богатство')
plt.xlabel('Игра')
plt.legend()
plt.show()

averageAramis = np.array(aramisArr).mean(axis=0)
for i in range(10):
    aramisIndex = np.random.randint(0, N)
    currentAramis = np.array(aramisArr[aramisIndex])
    plt.plot(currentAramis, linewidth=1)
plt.plot(averageAramis, linewidth=2, color='black', label='Среднее')
plt.title('Арамис')
plt.ylabel('Богатство')
plt.xlabel('Игра')
plt.legend()
plt.show()