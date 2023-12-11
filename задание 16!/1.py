# Постройте семейство функций на одном графике различными цветами:
# 1. степенные одночлены с целыми степенями от 1 до 6 на отрезке [−1; 1];
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1, 1, 100)

plt.figure(figsize=(10, 6))

for n in range(1, 7):
    y = x**n
    plt.plot(x, y, label=f'x^{n}', linewidth = 2,)

plt.xlabel('x')
plt.ylabel('y')
plt.title('степенные одночлены')
# plt . legend ( loc =  'best' )
# plt.grid(True)
plt.savefig('степенные_одночлены_с_целыми_степенями.png')
plt.show()