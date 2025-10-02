#example hex dump: 45 00 00 3c 1c 46 40 00 40 06 b1 e6 c0 a8 00 68 c0 a8 00 01
#Note:
#byte 0 nibble 1 = version, byte 0 nibble 2 = ihl, byte 2-3 = total length, byte 9 = protocol, byte 12-15 = Source IP, byte 16 - 19 = Destination IP

#all inputs are converted to string to avoid mix of data types
#hex_arr = ['45','00','00','3c','1c','46','40','00','40','06','b1','e6','c0','a8','00','68','c0','a8','00','01']

#define hex characters for comparison to check if user input hex value is valid
hex = "0123456789abcdef"


#a loop that will force the user to enter the IPv4 Hex dump whose length must match the entered bytes number from ip_type
while True:
    #an input method that asks the user to enter how many bytes are in the IPv4 Header since it can range between 20 to 60 bytes
    #this makes the code more efficent and more flexible
    byte_num = int(input(f"""State how many bytes are in the IPv4 Header between 20 - 60 bytes: """))

    #checks if 
    if byte_num >= 20 or byte_num <= 60:
        hex_dump = str(input(f"Enter the IPv4 Header Hex Dump: "))
        #splits the hex dump into arrays
        hex_arr = hex_dump.split()
        
    #checks if the number of bytes entered matches the user input for number of bytes in IPv4 header
    elif len(hex_arr) != byte_num:
        print(f"Please enter an IPv4 Header with {byte_num} bytes.")
        break
        
    else:
        print("Please enter bytes between 20 and 60.")


    #checks if user has entered a valid hexadecimal value using defined hex set -> hex
    for i in hex_arr:
        if (i in hex) != True:
            print("Hex invalid")

        else:
            break 

   
    if len(hex_arr) == byte_num:
        break
        


#uses the arrays in the hex_arr list to extract bytes
#Extracts version byte
byte_0 = hex_arr[0][0]

#Extracts ihl byte
byte_01 = hex_arr[0][1]

#Extracts total length 1st byte
byte_230 = hex_arr[2]
#Extracts total length 2nd byte
byte_231 = hex_arr[3]

#Extracts protocol byte
byte_9 = hex_arr[9]

#Extracts list of source IP bytes
byte_s1 = hex_arr[12]
byte_s2 = hex_arr[13]
byte_s3 = hex_arr[14]
byte_s4 = hex_arr[15]

#Extracts list of destination IP bytes
byte_d1 = hex_arr[16]
byte_d2 = hex_arr[17]
byte_d3 = hex_arr[18]
byte_d4 = hex_arr[19]


#uses the value from first_char, then converts to its integer equivalent
#conversion done from base 16 -> hex to integer

#Provides the version of the IPv4 header
version = int(byte_0, 16)

#Provides the internet header length
ihl = int(byte_01,16)

#provides the total length of the IPv4 header
length = int(byte_230, 16) | int(byte_231, 16)

#provides the number for protocol
protocol = int(byte_9, 16)

#identifies which protocol is in the IPv4 header
match protocol:
    case 1:
        protocol_type = "ICMP"

    case 6:
        protocol_type = "TCP"

    case 17:
        protocol_type = "UDP"

    case 121:
        protocol_type = "SMP"

#source ip int conversions - done separately as cannot print integer with strings using concat
s1 = int(byte_s1, 16)
s2 = int(byte_s2, 16)
s3 = int(byte_s3, 16)
s4 = int(byte_s4, 16)

#same as source but for destination
d1 = int(byte_d1, 16)
d2 = int(byte_d2, 16)
d3 = int(byte_d3, 16)
d4 = int(byte_d4, 16)


#Prints the version, ihl, total length, protocol type, source & destination ip
print(f"Version: {version}")
print(f"IHL: {ihl}")
print(f"Total Length: {length}")
print(f"Protocol: {protocol_type}")
print(f"Source IP: {s1}.{s2}.{s3}.{s4}")
print(f"Destination IP: {d1}.{d2}.{d3}.{d4}")
