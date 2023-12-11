# Перестройте графики из задания каждый в своём окне. Сделайте так, чтобы
# эти графики автоматически сохранялись каждый в свой файл
import numpy as np
import matplotlib.pyplot as plt

r = ['yellow','red', 'blue','orange','purple', 'green','pink', 'gray']

plt.figure(figsize=(5, 5))
t = 1

x = np.linspace(-1, 1, 100)
for n in range(1, 7):
    plt.subplots_adjust(hspace=0.5, wspace=0.5 )
    y = x**n
    plt.ylim (-1,1)
    plt.plot(x, y, linewidth = 2, color = r [t])
    
    plt.grid(True)
    plt.xlabel('x', loc= 'right')
    plt.ylabel('y', loc= 'top')
    plt.title ('x^' + str(t))
    plt.savefig('x^' + str (t) + '.png')
    plt.show()
    t+=1
