# This code is designed for IPv4 parsing, where non hex values are also detected. The user can enter between 20 to 60 bytes.

#example hex dump: 45 00 00 3c 1c 46 40 00 40 06 b1 e6 c0 a8 00 68 c0 a8 00 01

#Note:
#byte 0 nibble 1 = version, byte 0 nibble 2 = ihl, byte 2-3 = total length, byte 9 = protocol, byte 12-15 = Source IP, byte 16 - 19 = Destination IP

#all inputs are converted to string to avoid mix of data types
#hex_arr = ['45','00','00','3c','1c','46','40','00','40','06','b1','e6','c0','a8','00','68','c0','a8','00','01']

#stores valid hex values
hexdigits = "0123456789abcdef"

#empty variable to store non-hex values for id
invalid_hex = []


#a loop that will force the user to enter the IPv4 Hex dump whose length must match the entered bytes number from ip_type
while True:
    #an input method that asks the user to enter how many bytes are in the IPv4 Header since it can range between 20 to 60 bytes
    #this makes the code more efficent and more flexible
    hex_dump = str(input(f"Enter the IPv4 Header Hex Dump: "))
    #turns user input into an array of values separated by whitespace
    hex_arr = hex_dump.split()

    # string variable is used as temporary storage for storing hex_arr without whitespace
    string = "".join(hex_dump.split())
    
    #turns string variable into a list with separated characters for hex validation 
    hex_val = list(string)
    
    # to check the length of user input values
    byte_num = len(hex_arr)

    #checks if IPv4 header length matches the entered bytes amount
    if byte_num < 20 or byte_num > 60:
        print("Please enter bytes between 20 and 60.")
        continue
        
    #if byte_num is valid,
    elif byte_num >= 20 or byte_num <= 60:
        # checks all string characters in hexdigit to compare with hex_val characters in a for loop
        if all(c in hexdigits for c in hex_val) == True:
            try:
                #uses the value from first_char, then converts to its integer equivalent
                #conversion done from base 16 -> hex to integer

                #Provides the version of the IPv4 header
                version = int(hex_arr[0][0], 16)

                #Provides the internet header length
                ihl = int(hex_arr[0][1],16)

                #provides the total length of the IPv4 header
                length = int(hex_arr[2], 16) | int(hex_arr[3], 16)

                #provides the number for protocol
                protocol = int(hex_arr[9], 16)

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
                s1 = int(hex_arr[12], 16)
                s2 = int(hex_arr[13], 16)
                s3 = int(hex_arr[14], 16)
                s4 = int(hex_arr[15], 16)

                #same as source but for destination ip
                d1 = int(hex_arr[16], 16)
                d2 = int(hex_arr[17], 16)
                d3 = int(hex_arr[18], 16)
                d4 = int(hex_arr[19], 16)

                break



            #Catch errors for debugging
            #---------------------------------------------
            except ValueError as e:
                error = e
                print(f"An error occurred: {error}")
                print(f"Error type: {type(error)}")
                continue
                

            except IndexError as e:
                error = e
                print(f"An error occurred: {error}")
                print(f"Error type: {type(error)}")
                continue
            #---------------------------------------------


        #variable invalid_hex is used to identify the non-hex values to inform user
        #a for loop to check all characters in hex_val to compare with characters in hexdigits
        for char in hex_val:
            #if the character is not found in hexdigits
            if char not in hexdigits:
                #add the character to invalid_hex
                invalid_hex.append(char)
                
        
        #a statement to check if invalid hex values have been found
        if invalid_hex:
            #the join method is used to add all the characters in invalid_hex together, separated by whitespace
            print(f"invalid hex: {', '.join(invalid_hex)}")
        else:
            print("All characters are valid hex values.")
    
        

                                                                                                                                                                                                                                                                                                                                   
#Prints the version, ihl, total length, protocol type, source & destination ip
print(f"Version: {version}")
print(f"IHL: {ihl}")
print(f"Total Length: {length}")
print(f"Protocol: {protocol_type}")
print(f"Source IP: {s1}.{s2}.{s3}.{s4}")
print(f"Destination IP: {d1}.{d2}.{d3}.{d4}")
