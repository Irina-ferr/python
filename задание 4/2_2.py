#Y или (X и не Y или Z)
print ('  x  ','   ', '  y  ','   ', '  z  ','   ', 'значение')

#сделать чтобы печатало табличку истинности ?
for x in (False,True):
    for y in (False,True):
        for z in (False,True):
            t = y or (x and not y or z)
            print (x,'   ', y,'   ', z, '   ', t)

