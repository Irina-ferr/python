#a) Создайте два кортежа: один из чисел в диапазоне (1, количество учеников в группе) с шагом 1,
#второй — из фамилий учеников вашей группы. Пусть они соответствуют друг другу;
#b) Посмотрите, какая фамилия у студента с номером 5.
#c) А теперь посмотрите, что записано во второй кортеж под номером 5.
#d) Объедините два кортежа в один, присвоив результат новой переменной. Выведите получившийся список на экран.
#e) Возьмите срез из соединенного кортежа так, чтобы туда попали некоторые части обоих первых кортежей. Срез свяжите с очередной новой
#переменной. Выведите значение этой переменной.
group_1 = tuple ( range (1 , 12 , 1))
group_2 = ('Alieva', 'Babushkin', 'Baraulya', 'Gnusarkov', 'Golubeva', 'Znaharenko', 'Kryakin', 'Martyishova', 'Saharova', 'Chumachenko', 'Ferafontova')
print('ФАМИЛИЯ СТУДЕНТА С НОМЕРОМ 5 ', 'Golubeva')
print('ФАМИЛИЯ СТУДЕНТА С НОМЕРОМ 5 В КОРТЕЖЕ ', group_2 [5])
group_3 = group_1 + group_2
print ('КОРТЕЖИ ПОСЛЕ СОЕДИНЕНИЯ', group_3)
t = len(group_3)
group_4 =group_3 [t//4 : -(t//4)]
print ('СРЕЗ ИЗ КОРТЕЖЕЙ ПОСЛЕ СОЕДИНЕНИЯ', group_4)