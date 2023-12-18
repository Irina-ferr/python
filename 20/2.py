# Запишите в файл с помощью функции write() три столбца: в первый числа
# 𝑥 от 0 до 2𝜋 с маленьким шагом (например, 𝜋/24), во второй — значения
# sin(𝑥), в третий — значения cos(𝑥). Столбцы можно разделить табуляциями
# ’\t’ или пробелами ’␣’.
file = open("2.txt", "w")
file.write('x \t sin(x) \t cos(x) \n')   
import math

step = math.pi / 24
x = 0

while x <= 2 * math.pi:
    file.write(f'{str(x)} \t {str(math.sin(x))} \t {str(math.cos(x))} \n')
    x += step

file.close()