import os
import numpy as np
import matplotlib.pyplot as plt

# Перейти в папку "Распределения"
os.chdir("Распределения")

# Найти все текстовые файлы в папке
files = [file for file in os.listdir() if file.endswith(".txt")]

# Построить гистограммы распределений для каждого файла
for file in files:
    # Загрузить данные из файла
    data = np.loadtxt(file)

    # Построить гистограмму
    plt.hist(data, bins=20)

    # Установить заголовок графика
    plt.title(file)

    # Сохранить график в файл с таким же названием, но с расширением .png
    plt.savefig(file.replace(".txt", ".png"))

    # Очистить текущую фигуру перед построением следующей гистограммы
    plt.clf()