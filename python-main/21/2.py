# Файл rat_01_02ml.wdq содержит реальные данные от крысы генетической
# линии WAG/Rij, страдающей эпилепсией. Файл организован следующим
# образом: первые 5296 байт — служебная информация, которую при считывании можно пропустить методом seek, затем записаны целые двухбайтные
# знаковые числа, каждые 4 последовательных числа (8 байт) представляют
# собою записи 4 каналов за один и тот же момент времени. Считайте файл до
# конца, пропустив служебную информацию. Раскодируйте данные, используя модуль struct, функцию unpack. Чтобы декодировать большие объёмы
# данных полезно использовать умножение числа на символ. Постройте графики для всех четырёх каналов один под другим. Чтобы выбрать один канал полезно использовать срезы списков с шагом. По оси абсцисс отложите
# время: интервал между последовательными значениями времени составляет для данного файла 0.00195 с, время можно сгенерировать с помощью
# функций arange или linspace из модуля numpy.
import struct
import numpy as np
import matplotlib.pyplot as plt

with open("rat_01_02ml.wdq", "rb") as input_file:
    input_file.seek(5296) #служебная
    data = input_file.read()
decoded_data = struct.unpack('h' * (len(data) // 2), data)#раскодировать из  бинарного

time = np.linspace(0, len(decoded_data) * 0.00195, len(decoded_data) )#генерация времени

#region разделить на каналы
channel1 = decoded_data[::4]
channel2 = decoded_data[1::4]
channel3 = decoded_data[2::4]
channel4 = decoded_data[3::4]
# endregion

#region графики
plt.subplot(4, 1, 1)
plt.plot(time [:307200], channel1)
plt.title("Channel 1")

plt.subplot(4, 1, 2)
plt.plot(time [:307200], channel2)
plt.title("Channel 2")

plt.subplot(4, 1, 3)
plt.plot(time [:307200], channel3)
plt.title("Channel 3")

plt.subplot(4, 1, 4)
plt.plot(time [:307200], channel4)
plt.title("Channel 4")

#endregion
plt.tight_layout()
plt.show()