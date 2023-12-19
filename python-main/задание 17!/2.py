# Перестройте графики так, чтобы каждая кривая располагалась на одном графике с по-
# мощью команды subplot, легенду уберите, а её текст переместите в название
# соответствующего графика. Графики расположите на полотне:
# • в один столбец;
# • в два столбца;
# • в 3 столбца;
# • в одну строку.
# Перестройте графики из задания каждый в своём окне. Сделайте так, чтобы
# эти графики автоматически сохранялись каждый в свой файл

import numpy as np
import matplotlib.pyplot as plt

r = ['yellow','red', 'blue','orange','purple', 'green','pink', 'gray']

plt.figure(figsize=(15, 15))
plt.title('в одну строку')
t = 1

x = np.linspace(-1, 1, 100)
for n in range(1, 7):
    plt . subplot (6 , 1 , t) #в один столбец
    plt.subplots_adjust(hspace=0.5, wspace=0.5 )
    y = x**n
    plt.ylim (-1,1)
    plt.plot(x, y, linewidth = 2, color = r [t])
    
    plt.grid(True)
    plt.xlabel('x', loc= 'right')
    plt.ylabel('y', loc= 'top')
    plt.title ('x^' + str(t))

    t+=1
plt.savefig('в один столбец.png')
plt.show()

plt.figure(figsize=(15, 15))
t = 1

x = np.linspace(-1, 1, 100)
for n in range(1, 7):
    plt . subplot (3 , 2 , t) #в два столбца
    plt.subplots_adjust(hspace=0.5, wspace=0.5 )
    y = x**n
    plt.ylim (-1,1)
    plt.plot(x, y, linewidth = 2, color = r [t])
    plt.grid(True)
    plt.xlabel('x', loc= 'right')
    plt.ylabel('y', loc= 'top')
    plt.title ('x^' + str(t))

    t+=1
plt.savefig('в два столбца.png')
plt.show()

plt.figure(figsize=(15, 15))
t = 1
# plt.ylim (-1,1)
x = np.linspace(-1, 1, 100)
for n in range(1, 7):
    plt . subplot (2 , 3 , t) #в 3 столбца
    plt.subplots_adjust(hspace=0.5, wspace=0.5 )
    y = x**n
    plt.ylim (-1,1)
    plt.plot(x, y, linewidth = 2, color = r [t])
    plt.grid(True)
    plt.xlabel('x', loc= 'right')
    plt.ylabel('y', loc= 'top')
    plt.title ('x^' + str(t))

    t+=1
plt.savefig('в 3 столбца.png')
plt.show()

plt.figure(figsize=(15, 15))
t = 1
# plt.ylim (-1,1)
x = np.linspace(-1, 1, 100)
for n in range(1, 7):
    plt . subplot (1 , 6 , t) #в одну строку
    plt.subplots_adjust(hspace=0.5, wspace=0.5 )
    y = x**n
    plt.ylim (-1,1)
    plt.plot(x, y, linewidth = 2, color = r [t])
    plt.grid(True)
    plt.xlabel('x', loc= 'right')
    plt.ylabel('y', loc= 'top')
    plt.title ('x^' + str(t))

    t+=1
plt.savefig('в одну строку.png')

plt.show()