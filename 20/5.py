electrode_number = input("Введите номер отведения: ")

input_file = open("EEG.txt", "r")
output_file = open(f"Отведение_{electrode_number}.txt", "w")

for line in input_file:
    data = line.split("\t")
    electrode_data = data[int(electrode_number) - 1]
    output_file.write(electrode_data + "\n")

input_file.close()
output_file.close()