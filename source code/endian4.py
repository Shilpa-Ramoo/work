hex_string = str(input("Enter a 4 bytes hex values: \n"))
hex_arr = hex_string.split()

bytes_list = [0] * len(hex_arr)

for i in range(len(hex_arr)):
    bytes_list[i] = int(hex_arr[i], 16)


new_hex = bytes(bytes_list)

big_endian = int.from_bytes(new_hex, byteorder="big") 
little_endian = int.from_bytes(new_hex, byteorder="little") 


print(f"Big Endian: {big_endian}")
print(f"Little Endian: {little_endian}")

