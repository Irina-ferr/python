# Затем напишите вторую программу, которая переходит в папку Распределения,
# находит в ней все текстовые файлы, строит для них гистограммы распределений,
# сохраняет графики в файлы с таким же названием, как исходный текстовый
# файл, но другим расширением (.png, .jpg или .pdf).
import os
import numpy as np
import matplotlib.pyplot as plt

os.chdir("Распределения")
files = [file for file in os.listdir() if file.endswith(".txt")]

for file in files:
    # Загрузить данные из файла
    data = np.loadtxt(file)
    # region график
    plt.hist(data, bins=20,  ec='black', density=True, color='pink')
    plt.title(file)
    plt.savefig(file.replace(".txt", ".pdf"))
    plt.clf() 
    # endregion
   
   