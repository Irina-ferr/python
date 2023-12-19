# Постройте закрашенную контурную диаграмму и трёхмерный график для
# следующих функций двух переменных, определённых в прямоугольной области
# 𝑥 ∈ [−3; 3], 𝑦 ∈ [−3; 3]:
#  𝑧 = tg(𝑥𝑦),
# Построенные графики сохраните в файлы с расширением png.
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
x = np . arange ( -3 , 3 , 0.01)
y = np . arange ( -3 , 3 , 0.01)
X , Y = np . meshgrid (x , y )
Z = np.tan(X * Y)
plt . contourf (X , Y , Z )
plt . savefig ( 'a.png')

fig = plt.figure ()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')
plt . savefig ( 'b.png')
plt . show ()

