# матрицу размера 5×5, где в первом столбце стоят единицы, во втором двойки, в третьем тройки и т.д.
import numpy as np 
m = np.zeros((5, 5))
for i in range (5):
    for t in range (5):
        m [i, t] = i + 1
print (m)
np.savetxt ('11.txt', m)

