# Файл Rat.wdq содержит бинарное представление записи с 4 отведений внутричерепной ЭЭГ крыс. 
# Отведения записаны последовательно. Числа знаковые двухбайтные. Создайте программу, выводящую информацию из одного
# из отведений с заданным номером в отдельный текстовый (.txt) файл. Запишите первые 100 измерений. Название текстового файла составьте из
# названия исходного файла без расширения ’.wdq’, номера отведения и расширения ’.txt’.
from struct import unpack
import os.path

NumberChannel = int(input('Номер отведения: '))
length = 100  # количество измерений
Rat = 'Rat.wdq'

with open(Rat, 'rb') as fr:
    fr.seek(NumberChannel * length * 2)  # к началу отведения
    buffer = fr.read(length * 2)  #данные отведения

mylist = unpack(length * 'h', buffer)  # h формат двухбайтных знаковых

file_name = os.path.splitext(Rat)[0] +'_'+ str(NumberChannel) + '.txt'
with open(file_name, 'w') as fw:
    for i in range(len(mylist)):
        fw.write(str(mylist[i]) + '\n')