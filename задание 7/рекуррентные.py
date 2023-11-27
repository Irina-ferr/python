# Придумайте рекуррентное соотношение, задающее следующие числовые последовательности:
# a) 1, 2, 3, 4, . . .
Е = [1]
e = 1
n = 5
i = 0
summ = 0
while i <= n:
    summ = e + 1
    Е.append (summ)
    e = summ
    i = i + 1
print (Е)   
# b) 0, 5, 10, 15, . . .
Е = [0]
e = 0
n = 5
i = 0
summ = 0
while i <= n:
    summ = e + 5
    Е.append (summ)
    e = summ
    i = i + 1
print (Е)  
# c) 1, 1, 1, 1, . . .
Е = [1]
e = 1
n = 5
i = 0
while i <= n:
    Е.append (e)
    i = i + 1
print (Е) 
# d) 1, −1, 1, −1, . . .
Е = [1]
e = 1
n = 5
i = 0
summ = 0
while i <= n:
    summ = e * (-1)
    Е.append (summ)
    e = summ
    i = i + 1
print (Е)  
# e) 1, −2, 3, −4, 5, −6 . . .
Е = []
e = 1
ee = -2
Е.append (e)
Е.append (ee)
n = 5
i = 0
summ = 0
summee = 0
while i <= n:
    summ = e + 2
    summee = ee - 2
    Е.append (summ)
    Е.append (summee)
    e = summ
    ee = summee
    i = i + 1
print (Е)  
# f) 2, 4, 8, 16, . . .
Е = [2]
e = 2
n = 5
i = 0
summ = 0
while i <= n:
    summ = e * 2
    Е.append (summ)
    e = summ
    i = i + 1
print (Е) 
# g) 2, 4, 16, 256, . . .
Е = [2]
e = 2
n = 5
i = 0
summ = 0
while i <= n:
    summ = e **2
    Е.append (summ)
    e = summ
    i = i + 1
print (Е) 
# h) 0, 1, 2, 3, 0, 1, 2, 3, 0, . . .
Е = []
e = 0
ee = 1
Е.append (e)
Е.append (ee)
a = -2
n = 5
i = 0
summ = 0
summee = 0 
while i <= n:
    t = a * (-1)
    summ = e + t
    summee = ee + t
    Е.append (summ)
    Е.append (summee)
    e = summ
    ee = summee
    i = i + 1
    a = t
print (Е) 
# i) 1!, 3!, 5!, 7!, . . .
Е = []
e = 1
Е.append (str(e)+'!')
n = 5
i = 0
summ = 0
while i <= n:
    summ = e + 2
    Е.append (str(summ) +'!')
    e = summ
    i = i + 1
print (Е) 
