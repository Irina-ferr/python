import struct

electrode_number = input("Введите номер отведения: ")
output_file_name = "Rat_" + electrode_number + ".txt"

with open("Rat.wdq", "rb") as input_file, open(output_file_name, "w") as output_file:
    for _ in range(100):
        data = input_file.read(2)
        electrode_data = struct.unpack('h', data)[0]
        output_file.write(str(electrode_data) + "\n")