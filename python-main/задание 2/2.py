#Составьте арифметическое выражение и вычислите n-е нечётное число
#(первое — 1, второе — 3 и т.д.).
## Использовать формулу n-ого члена арифметической прогрессии,
##разность прогресси d=2, первый член прогрессии a1=1
###программа выводит что она делает, потом просит ввести номер чиcла n
print ('Программа выведет n-ное нечетное число')
n = int (input('Введите номер нечетного числа n= '))
d = 2
a_1 = 1
a_n = a_1 + d * (n - 1)
print ('a_n=', a_n)
