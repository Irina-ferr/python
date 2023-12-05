# 2^x на отрезке x ∈ [−2; 2] с шагом 0.01, с шагом 0.1, с шагом 0.25;
import numpy as np
dt = 0.01
x = np. arange ( -2 , 2+ dt , dt )
n=2**x
for i in range ( len ( x )):
    print ( x [ i ] , n [ i ])
dt = 0.1
x = np. arange ( -2 , 2+ dt , dt )
n=2**x
for i in range ( len ( x )):
    print ( x [ i ] , n [ i ])
dt = 0.25
x = np. arange ( -2 , 2+ dt , dt )
n=2**x
for i in range ( len ( x )):
    print ( x [ i ] , n [ i ])
