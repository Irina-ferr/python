# Запишите в файл с помощью функции write() три столбца: в первый — 
# целые числа от 1 до 100, во второй — их квадраты, в третий — их кубы. 
# Столбцы можно разделить табуляциями ’\t’ или пробелами ’␣’.
with open('1.txt', 'w') as file:
    file.write('n \t n^2 \t n^3 \n')    
    for i in range(1, 101):
        file.write(f'{i}\t{i**2}\t{i**3}\n')
file.close