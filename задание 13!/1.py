# x^2 на отрезке x ∈ [−2; 2] с шагом 0.01, с шагом 0.1, с шагом 0.25;
# пример
import numpy as np
dt = 0.01
x = np. arange ( -2 , 2+ dt , dt )
n = np. square  ( x )
for i in range ( len ( x )):
    print ( x [ i ] , n [ i ])
dt = 0.1
x = np. arange ( -2 , 2+ dt , dt )
n = np. square  ( x )
for i in range ( len ( x )):
    print ( x [ i ] , n [ i ])
dt = 0.25
x = np. arange ( -2 , 2+ dt , dt )
n = np. square  ( x )
for i in range ( len ( x )):
    print ( x [ i ] , n [ i ])