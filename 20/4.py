# Считайте текстовый файл «Зачёт.txt».
# Найдите в нём оценку любого учащегося
# (фамилия вводится с клавиатуры) и выведите её на экран.
familia = input("Введите фамилию ученика: ")

file = open("Зачёт.txt", "r")

for i in file:
    data = i.split()
    if data[0] == familia:
        grade = data[-1]
        print("Оценка ученика:", grade)
        break

file.close()