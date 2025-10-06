# Code Documentations For Lab 1 & Lab 2

## Project Overview

This repository contains Python programs developed for **Lab 1** and **Lab 2** as part of coursework on **Core Computer Science & Networking Fundamentals**.  
These labs explore fundamental concepts of **endianness** and **IPv4 header parsing**.

---

## Lab Summaries

### **Lab 1: Number Systems & Endianness**

- **Objective:**  
  Understand how hexadecimal values are interpreted in **Big Endian** and **Little Endian** formats.

- **Concept:**  
  Endianness determines the order of byte storage in memory.  
  - **Big Endian:** Most Significant Byte (MSB) first  
  - **Little Endian:** Least Significant Byte (LSB) first

#### Scripts
- [`endian2.py`](https://github.com/ShilpaRamoo/work/blob/main/source%20code/endian2.py) – 2-byte endianness conversion  
- [`endian4.py`](https://github.com/ShilpaRamoo/work/blob/main/source%20code/endian4.py) – 4-byte endianness conversion

---

### **Lab 2: IPv4 Header Parsing**

- **Objective:**  
  Learn to interpret raw hexadecimal strings as structured network data (IPv4 headers).

- **Concept:**  
  IPv4 packets are sequences of bytes. Each field (e.g., version, IHL, protocol, IPs) can be extracted by parsing the corresponding byte positions.

#### Script
- [`hexdump60.py`](https://github.com/ShilpaRamoo/work/blob/main/source%20code/hexdump60.py)

---

## Requirements
- **Python Version:** 3.13.7
- **Libraries:** No external dependencies (uses only built-in Python functions)

---

## Acknowledgements
[Python Software Foundation. (2025) Built in Functions](https://docs.python.org/3/library/functions.html)

[Stackoverflow](https://stackoverflow.com/questions)


---

## [Lab work 1 - Endianness for two bytes](https://github.com/ShilpaRamoo/work/blob/db9c23d2fd105ab971f6c1f8577e0743eb93a79c/source%20code/endian2.py)

### Line 1

- **Function**: hex_string = str(input("Enter a 2 hex values: \n"))
  
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


---

## [Lab work 1 - Endianness for four bytes](https://github.com/Shilpa-Ramoo/work/blob/db9c23d2fd105ab971f6c1f8577e0743eb93a79c/source%20code/endian4.py)

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


---

## [Lab work 2 - IPv4 Parsing](https://github.com/Shilpa-Ramoo/work/blob/db9c23d2fd105ab971f6c1f8577e0743eb93a79c/source%20code/hexdump60.py)

### Line 12
- **Function**: hexdigits = "0123456789abcdef"
- **Purpose**: A variable used to store valid hexdecimal values to be used for comparison


### Line 15
- **Function**: invalid_hex = []
- **Purpose**: An empty list used to stored detected non-hex values


### Line 19
- **Function**: while True:
- **Purpose**: A loop to prompt the user to enter the IPv4 header and if error detected, it will force the user to enter the value again.


### Line 19
- **Function**: while True:
- **Purpose**: A loop to prompt the user to enter the IPv4 header and if error detected, it will force the user to enter the value again.


### Line 22
- **Function**: hex_dump = str(input(f"Enter the IPv4 Header Hex Dump: "))
- **Purpose**: An input method to prompt the user to enter the IPv4 Header, stored as string in the variable hex_dump.


### Line 24
- **Function**: hex_arr = hex_dump.split()
- **Purpose**: hex_arr is a variable that stores the value entered by the user in the format where each characters are separated by whitespace and stored individually in an array. The .split() method performs this task.
- **Example**:
test = "hello world"
print(f"{test.split()}") **outputs: hello world**


### Line 27
- **Function**: string = "".join(hex_dump.split())
- **Purpose**: string variable is used as temporary storage for storing hex_arr without whitespace. 
- **Example**:
test = "hello world"
print(f"{test.join()}") **outputs: helloworld**

### Line 29
- **Function**: hex_val = list(string)
- **Purpose**: turns string variable into a list with separated characters for hex validation 


### Line 31
- **Function**: byte_num = len(hex_arr)
- **Purpose**: to check the length of user input values


### Line 34 - 36
- **Function**: if byte_num < 20 or byte_num > 60:
        print("Please enter bytes between 20 and 60.")
        continue
- **Purpose**: checks if IPv4 header length matches the required bytes amount between 20 and 60


### Line 39
- **Function**: byte_num >= 20 or byte_num <= 60:
- **Purpose**: a conditional statement that performs a task if byte amount entered is valid.


### Line 41
- **Function**: if all(c in hexdigits for c in hex_val) == True:
- **Purpose**: checks all string characters in hexdigit to compare with hex_val characters in a for loop


### Line 42 & Line 90 - 97
- **Purpose**: A try... except is a statement used to handle errors during execution.


### Line 47 - 82
- **Purpose**: The sectioning of the user's provided IPv4 header to identify the parts of the header.
- **Example**: version = int(hex_arr[0][0], 16)
here the program is accessing the first value in the first array found in the hex_arr array and uses the int function to convert from hex to decimal, the second parameter - 16, is used to specify that the conversion is from hexadecimal.


### Line 59 - 70
- **Purpose**: A match statement sued to identify the type of protocol in the IPv4 header.
- **Example**: Case 1 = ICMP, because ICMP is protocol 1.


### Line 107 - 111
- **Purpose**: It is a validation check to detect non-hexadecimal values using a for loop to loop through the values in hex_val. The if statement checks if the current character from the hex_val is in the hexdigits variable (which contains the valid hexadecimal values). After the check, the current character is stored in the invalid_hex variable to help the user identify the non-hexadecimal values.


### Line 115 - 119
- **Purpose**: An if statement used to check if the invalid hexadecimal values have been detected and if so, output the invalid value.


### Line 125 - 130
- **Purpose**: Prints the version, ihl, total length, protocol type, source & destination ip


---


## Example Input / Output

### Example (Lab 1)
```
Input: 01 02
Big Endian: 258
Little Endian: 513
```

---

### Example (Lab 2)
```
Input: 45 00 00 3c 1c 46 40 00 40 06 b1 e6 c0 a8 00 68 c0 a8 00 01

Version: 4
IHL: 5
Total Length: 60
Protocol: TCP
Source IP: 192.168.0.104
Destination IP: 192.168.0.1
```
