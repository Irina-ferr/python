# Постройте графики следующих функций, используя шаг выборки данных по
# абсциссе из задания 13:
# 2^x на отрезке x ∈ [−2; 2];
import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 7))

x1 = np.arange(-2, 2, 0.01)
y1 = np.power(2, x1)
plt.plot(x1, y1, label='0.01', marker='.')

x2 = np.arange(-2, 2, 0.1)
y2 = np.power(2, x2)
plt.plot(x2, y2, label='0.1', marker='*')

x3 = np.arange(-2, 2, 0.25)
y3 = np.power(2, x3)
plt.plot(x3, y3, label='0.25', marker='|',)

plt . title ( 'график 2^х')
plt.xlabel('x')
plt.ylabel('2^x')
plt . legend ( loc =  'best' )

plt.show()