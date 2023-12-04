# массив-диапазон от −𝑒 до 𝑒 с шагом 𝑒 /50;
import numpy as np 
e = int (input('Введите е '))
e_1 = e * (-1)
t = e / 50
a = np.arange (e_1, e, t)
print (a)
np.savetxt ('6.txt', a)