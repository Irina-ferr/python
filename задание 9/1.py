# Напишите программу, вычисляющую сумму всех чётных чисел в диапазоне
# от 1 до 90 включительно.
n = 0 
k = 0
for n in range (0, 91):
    if ((n % 2) == 0):
        k = k + n
print ('сумма всех чётных чисел в диапазоне от 1 до 90 ', k)