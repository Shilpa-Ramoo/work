# Code Documentations For Lab 1 & Lab 2
**Source**: [Python Software Foundation. (2025) Built in Functions](https://docs.python.org/3/library/functions.html)
> Lab 1 - Endianness
## [endian2.py](https://github.com/Shilpa-Ramoo/work/blob/c372829ce7eed45bca7074c438849e15874ad6f4/endian2.py)

### Line 1

- **Function**: 'hex_string = str(input("Enter a 2 hex values: \n"))'
  
- **Purpose**: to prompt the user to input two hexadecimal values (e.g., 2a 33), which is set as strings. It would be stored as such: “2a 33” in the variable hex_string.
  
- **Parameters**:
	- Input(): prompts the user to enter something, in this case 2 hex values.
	- Str(): sets the value given by the user as strings.


 
### Line 2
- **Function**: hex_arr = hex_string.split()
  
- **Purpose**: since the hex_string variable stores the values entered by the user as one value, it is split into arrays to store individual string values.
  
- **Parameters**:
	- Hex_arr: a variable used to store the array version of the user inputs.
	- .split(): a python method used to divide a string into arrays. For example the user input “2a 33” is split into an array, [“2a”, “33”]. The .split() method divides the array by whitespace when nothing is placed in its parentheses.
   
- **Example**:
	- If I were to divide a string “a, b, c, d” and I have separated the values by a comma, a comma would be placed in the split method’s parentheses to state that the values are to be divided by a comma.
	- User_input = “a,b,c,d”
	- Str_list = user_input.split(,)
	- **Output: [a b c d]** -> in individual array slots.



### Line 5 & 6
- **Function a**: byte1  = int(hex_arr[0], 16)

- **Function b**: byte2  = int(hex_arr[1], 16)

- **Purpose**: both function a and b are storing the two converted string values from the hex_arr array, accessing it using array index.

- **Parameters**
	- Byte1 & byte2: variables used to store the array values in integer form.
	- Int(hex_arr[0], 16): the integer method in python used to convert a hex value to integer by accessing the value [in this case the index 0 in hex_arr]  and stating the data type of the selected value [in this case base 16 for hexadecimal]. 

- **Error Case**:
	- Please note that this method does not accept string values, which is why the values in hex_string were split into arrays containing two separate values. The method already has a dictionary of all existing hexadecimal values. If an incorrect hexadecimal value was to be entered, this method would cause an error.


### Line 8 

- **Function**: new_hex = bytes([byte1, byte2])
- **Purpose**: the variables byte1 and byte2 are being converted to bytes and then stored in the variable new_hex, to be interpreted as hex values instead of integers or strings.
- **Parameters**:
	- New_hex: a variable used to store the converted values from integer to bytes.
	- Bytes([byte1, byte2]): Bytes() is a function in python used to convert values into bytes, the values need to be in integer format [since it can only convert from integer to binary or hex to binary], else there will be an error. Byte1 and byte2 are being parsed in the bytes function to be converted.
- **Example**: 
	- print(bytes(1)) ; **output b’\01’**

### Line 10 
**Function**: big_endian = int.from_bytes(new_hex, byteorder="big") 
**Purpose**: the variable big_endian stores the big-endian value generated from the function int.from_bytes()
- **Parameters**:
	- Big_endian: stores the big endian value
	- Int.from_bytes(new_hex, byteorder="big"): a function used to convert from bytes to integer, by entering the value or list of values and the order by which to sort the bytes (endianness).  Here the array new_hex that stores bytes are being used and the endian order is set to “big” for big endian, where the most significant byte is placed at the lowest memory address and the least significant byte placed last. 
- **Example**:
	- User_input = [01 02]
	- Z = int.frombytes(user_input, byteorder=”big”)
	- Print(f”little-endian: {z}”) ; **outputs: 258**


### Line 11
- **Function**: little_endian = int.from_bytes(new_hex, byteorder="little") 
- **Purpose**: same as line 10 but for little-endian.
- **Parameter**:
	- int.from_bytes(new_hex, byteorder="little"): same as line 10 but here the byteorder is set to “little for little-endian”, where the least significant byte is placed at the lowest memory address and the most significant byte placed last.
- **Example**:
	- User_input = [01 02]
	- Z = int.frombytes(user_input, byteorder=”little”)
	- Print(f”little-endian: {z}”) ; **outputs: 513**

### Line 14 & 15
- **Function a**: print(f"Big Endian: {big_endian}")
- **Function b**: print(f"Little Endian: {little_endian}")
- **Purpose**: both function a and b print the endianness Big and Little.




## [endian4.py](https://github.com/Shilpa-Ramoo/work/blob/c372829ce7eed45bca7074c438849e15874ad6f4/endian4.py)

### Line 1 
- **Function**: hex_string = str(input("Enter a 4 bytes hex values: \n"))
- **Purpose**: to prompt the user to input four hexadecimal values (e.g., 2a 33 ff 15), which is set as strings. It would be stored as such: “2a 33 ff 15” in the variable hex_string.
- **Parameters**:
	- Input(): prompts the user to enter something, in this case 4 hex values.
	- Str(): sets the value given by the user as strings.


### Line 2  
- **Function**: hex_arr = hex_string.split()
- **Purpose**: since the hex_string variable stores the values entered by the user as one value, it is split into arrays to store individual string values.
- **Parameters**:
	- Hex_arr: a variable used to store the array version of the user inputs.
	- .split(): a python method used to divide a string into arrays. (same as endian2.py’s Line 2)

### Line 4 
**Function**: bytes_list = [0] * len(hex_arr)

**Purpose**: this part is about creating an empty array with indices number of the same amount as the length of the value entered by the user in hex_arr. 
- **Parameters**:
	- Bytes_list: an array stores the new indices the size of the length of the hex_arr array.
	- [0] * len(hex_arr): [0] states the value of the index, here it is set to 0. It is being multiplied by len(hex_arr) to duplicate it the same amount as the length of the hex_arr array. In this case, len(hex_arr) is being used because the user can enter any number of bytes and this makes the program more adaptable to the user’s needs.
- **Example**:
	- A = [7] * 3, 
	- Print(A) ; **outputs: [7, 7, 7]** -> increases the index count by three, with 0 as their values.

### Line 6  
- **Function**: for i in range(len(hex_arr)):
- **Purpose**: a for loop designed to loop through a set of instructions at a defined number of times according to how many values there are in the hex_arr array.
- **Example**:
	- For x in range(2):
	      Print(“Hey, You ”) ; **Outputs: Hey, You Hey, You**

### Line 7 
- **Function**: bytes_list[i] = int(hex_arr[i], 16)
- **Purpose**: this is the set of instructions inside the for loop, to map the values from the hex_arr array, where it is being converted to integer.
- **Parameters**
	- Bytes_list[i]: this is the previously created array from Line 4 containing indices with empty values.
	- Int(hex_arr[i], 16): python’s built-in function converts the selected index from the hex_arr and states the conversion is from hexadecimal by setting the second value to 16. The converted index is then stored in the bytes_list array according to matching index (i).
- **Example**:
	- Print(X = int(FF, 16)) ; **Outputs: 256**

### Line 10 	
- **Function**: new_hex = bytes(bytes_list)
- **Purpose**: the array new_hex stores the values from the bytes_list which has been converted to bytes. This is done because the functions on line 12 and 13 require these values to be in bytes form.
- **Parameter**:
	- Bytes(bytes_list): python’s built-in function that converts the values in bytes_list array to bytes.
- **Example**:
	- Print(bytes(1)) ; **Outputs: b’\x01’**

### Line 12 
- **Function**: big_endian = int.from_bytes(new_hex, byteorder="big") 
- **Purpose**: to convert the bytes from new_hex array to big endian and store it in variable big_endian.
- **Parameters**:
	- Int.from_bytes(new_hex, byteorder=”big”): python’s built-in function that would produce the big-endian value in integer format. Inside the from_bytes function, two values are being parsed – new_hex which is the array containing the bytes values & byteorder=”big” which sets the value that are to be converted in big-endian format.
- **Example**:
	- User_input = [01 02 03 04]
	- Z = int.frombytes(user_input, byteorder=”big”)
	- Print(f”little-endian: {z}”) ; **outputs: 16909060**


### Line 13 
- **Function**: little_endian = int.from_bytes(new_hex, byteorder="little")
- **Purpose**: same as the function from line 12, on this function the byteorder is set to “little” for little-endian.
- **Example**:
	- User_input = [01 02 03 04]
	- Z = int.frombytes(user_input, byteorder=”little”)
	- Print(f”little-endian: {z}”) ; **outputs: 67305985**

### Line 16 & 17 
- **Function a**: print(f"Big Endian: {big_endian}")
- **Function b**: print(f"Little Endian: {little_endian}")
- **Purpose**: Both function a and b use the f string to display the big and little endian values.



> Lab 2 - IPv4 Parsing
## [hexdump60.py](https://github.com/Shilpa-Ramoo/work/blob/c372829ce7eed45bca7074c438849e15874ad6f4/hexdump60.py)

 * **Will upload soon** *
