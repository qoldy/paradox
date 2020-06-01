import numpy as np
from matplotlib import pyplot as plt

n, step, max_n = 80, 5, 160
students = 10000
numberArr, pointArr = [], []
gotCorel, lostCorel = [], []
for i in range(n, max_n+1, step):
    gotArrMath, lostArrMath = [], []
    gotArrRus, lostArrRus = [], []
    number = 0
    math = np.random.normal(60, 10, size=students)
    rus = np.random.normal(60, 10, size=students)
    points = math + rus
    for j in range(students):
        if points[j] >= i:
            number += 1
            gotArrMath.append(math[j])
            gotArrRus.append(rus[j])
        else:
            lostArrMath.append(math[j])
            lostArrRus.append(rus[j])
    pointArr.append(i)
    numberArr.append(number)
    gotCorel.append(np.corrcoef(np.array([gotArrMath, gotArrRus]))[0][1])
    lostCorel.append(np.corrcoef(np.array([lostArrMath, lostArrRus]))[0][1])
pointArr = np.array(pointArr)
numberArr = np.array(numberArr)
plt.plot(numberArr, pointArr)
plt.xlabel('Количество прошедших')
plt.ylabel('Балл')
plt.show()
gotCorel = np.array(gotCorel)
lostCorel = np.array(lostCorel)
plt.plot(gotCorel, pointArr)
plt.title("Корреляция прошли")
plt.xlabel('Коэффициент корреляции')
plt.ylabel('Балл')
plt.show()
plt.title("Корреляция не прошли")
plt.xlabel('Коэффициент корреляции')
plt.ylabel('Балл')
plt.plot(lostCorel, pointArr)
plt.show()
