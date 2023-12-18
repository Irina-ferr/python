import os
import numpy as np

# Создать папку "Распределения", если она не существует
if not os.path.exists("Распределения"):
    os.makedirs("Распределения")

# Записать последовательность величин, распределенных по равномерному закону, в файл "uniform.txt"
uniform_data = np.random.uniform(size=1000)
np.savetxt("Распределения/uniform.txt", uniform_data)

# Записать последовательность величин, распределенных по нормальному закону, в файл "normal.txt"
normal_data = np.random.normal(size=1000)
np.savetxt("Распределения/normal.txt", normal_data)

# Записать последовательность величин, распределенных по закону x^2 с 5 степенями свободы, в файл "chi_squared.txt"
chi_squared_data = np.random.chisquare(df=5, size=1000)
np.savetxt("Распределения/chi_squared.txt", chi_squared_data)