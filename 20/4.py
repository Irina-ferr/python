# Считайте текстовый файл «Зачёт.txt».
# Найдите в нём оценку любого учащегося
# (фамилия вводится с клавиатуры) и выведите её на экран.
last_name = input("Введите фамилию ученика: ")

file = open("Зачёт.txt", "r")

for line in file:
    data = line.split()
    if data[0] == last_name:
        grade = data[-1]
        print("Оценка ученика:", grade)
        break

file.close()