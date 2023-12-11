# для построенного в рамках задания 14 графика измените:
# • цвет линии;
# • тип линии и маркеров;
# • шаг выборки данных.
# Далее введите сетку. Сохраните полученный график в файл, опробуйте со-
# хранять файл в разных форматах: png, jpg, pdf, eps, svg, svgz.
import numpy as np
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 7))
plt . subplot (2 , 2 , 1)
x1 = np.arange(-2, 2, 0.5)
y1 = np.power(2, x1)
plt.plot(x1, y1, label='0.01', marker='*', color = 'red', linewidth = 1 )

plt.xlabel('x')
plt.ylabel('2^x')
plt . legend ( loc =  'best' )
plt . grid ( True )

plt . subplot (2 , 2 , 2)
x2 = np.arange(-2, 2, 0.15)
y2 = np.power(2, x2)
plt.plot(x2, y2, label='0.1', marker='+', color ='purple', linewidth = 1.5)

plt.xlabel('x')
plt.ylabel('2^x')
plt . legend ( loc =  'best' )
plt . grid ( True )

plt . subplot (2 , 2 , 3)
x3 = np.arange(-2, 2, 0.3)
y3 = np.power(2, x3)
plt.plot(x3, y3, label='0.25', marker='x', color ='orange', linewidth = 2)

plt.xlabel('x')
plt.ylabel('2^x')
plt . legend ( loc =  'best' )
plt . grid ( True )

plt . savefig ('1.png')
plt . savefig ('1.jpg')
plt . savefig ('1.pdf')
plt . savefig ('1.eps')
plt . savefig ('1.svg')
plt . savefig ('1.svgz')
plt.show()