# e^−t * cos(2πt) на отрезке t ∈ [−10; 10] с шагом 1 и с шагом 0.25;
import numpy as np
dt = 1
t = np. arange ( -10 , 10+ dt , dt )
n=np.e**(-t)*np.cos(2*np.pi*t)
for i in range ( len ( t )):
    print ( t [ i ] , n [ i ])
dt = 0.25
t = np. arange ( -10 , 10+ dt , dt )
n=np.e**(-t)*np.cos(2*np.pi*t)
for i in range ( len ( t )):
    print ( t [ i ] , n [ i ])