hex_string = str(input("Enter a 2 bytes hex values: \n"))
hex_arr = hex_string.split()


byte1  = int(hex_arr[0], 16)
byte2  = int(hex_arr[1], 16)

new_hex = bytes([byte1, byte2])
 
big_endian = int.from_bytes(new_hex, byteorder="big") 
little_endian = int.from_bytes(new_hex, byteorder="little") 


print(f"Big Endian: {big_endian}")
print(f"Little Endian: {little_endian}")
