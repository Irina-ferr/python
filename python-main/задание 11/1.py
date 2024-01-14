# из нулей:одномерные длины 10 и 55, матрицу размерами 3×4, трёхмерный массив формы 2×4×5;
import numpy as np 
# массив одномерный 10 из нулей
a_1 = np.zeros (10)
print (a_1)
np.savetxt ('1_1.txt', a_1)
# массив однономерный 55 из нулей
a_2 = np.zeros (55)
print (a_2)
np.savetxt ('1_2.txt', a_2)
# матрица 3 на 4 из нулей
m_1 = np.zeros((3, 4))
print (m_1)
np.savetxt ('1_3.txt', m_1)
# трехмерный массив 2 4 5 
m_2 = np.zeros((2, 4, 5))
print (m_2)
np.savetxt ('1_4.txt', m_2)
