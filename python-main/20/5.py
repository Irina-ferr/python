# Файл EEG.txt (возьмите у преподавателя) содержит запись ЭЭГ (электроэнцефалограммы) человека, 
# включающую сигналы с 16 электродов (отведений). Каждому отведению соответствует столбец чисел. 
# Столбцы разделены символом табуляции. Создайте программу, выделяющую в отдельный
# текстовый файл отведение с заданным номером. Название текстового файла составьте из названия исходного 
# файла без расширения, номера отведения и расширения ’.txt’.
input_f = open("EEG.txt", "r")

NumberChannel = int (input("Введите номер отведения: "))
output_f = open(f"EEG_{NumberChannel}.txt", "w")
for line in input_f:
    mylist = line.split("\t")
    electrode_mylist = mylist[int(NumberChannel) - 1]
    output_f.write(electrode_mylist + "\n")

input_f.close()
output_f.close()