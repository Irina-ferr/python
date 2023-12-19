# Первую программу, которая создаёт папку Распределения, если она ещё не создана. 
# Далее записывает в неё три текстовых файла .txt, содержащих 
# последовательность величин, распределённых по равномерному закону, 
# нормальному закону и закону 𝜒^2 с 5 степенями
# свободы.
import os
import numpy as np

if not os.path.exists("Распределения"):
    os.makedirs("Распределения")

# region по равномерному закону
uniform_data = np.random.uniform(size=1000)
np.savetxt("Распределения/uniform.txt", uniform_data)
# endregion
# region по нормальному закону
normal_data = np.random.normal(size=1000)
np.savetxt("Распределения/normal.txt", normal_data)
# endregion
# region по закону x^2 с 5 степенями свободы
chi_squared_data = np.random.chisquare(df=5, size=1000)
np.savetxt("Распределения/chi_squared.txt", chi_squared_data)
# endregion