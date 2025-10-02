def decoding_menu():
    print(
        '''Decoding Menu
-------------
1. Decode hexadecimal
2. Decode binary
3. Convert binary to hexadecimal
4. Quit
'''
    )
def hex_string_decode(hex):
    hex_list = []
    for char in hex:
        hex_list.append(char)
    if hex_list[1] == "x":
        del hex_list[0:2]
    for char in range(len(hex_list)):
        val = (hex_list[char])
        hex_list.insert(char,hex_char_decode(val))
        hex_list.pop(char+1)
    hex_list.reverse()
    decimal_value = 0
    for char in range(len(hex_list)):
        val = int(hex_list[char])
        decimal_value += (16 ** char) * val
    return decimal_value
def hex_char_decode(digit):
    if digit == "a":
        return 10
    elif digit == "b":
        return 11
    elif digit == "c":
        return 12
    elif digit == "d":
        return 13
    elif digit == "e":
        return 14
    elif digit == "f":
        return 15
    else:
        return digit
def binary_string_decode(binary):
    bin_list = []
    for char in binary:
        bin_list.append(char)
    if bin_list[1] == "b":
        del bin_list[0:2]
    bin_list.reverse()
    decimal_value = 0
    for char in range(len(bin_list)):
        val = int(bin_list[char])
        if val == 1:
            decimal_value += 2**char
    return str(decimal_value)
def binary_to_hex(binary):
    decimal_value = int(binary_string_decode(binary))
    dec_list = []
    for i in range(len(str(decimal_value))-1):
        remainder = int(decimal_value) % 16
        if remainder == 15:
            dec_list.append("F")
        elif remainder == 14:
            dec_list.append("E")
        elif remainder == 13:
            dec_list.append("D")
        elif remainder == 12:
            dec_list.append("C")
        elif remainder == 11:
            dec_list.append("B")
        elif remainder == 10:
            dec_list.append("A")
        else:
            dec_list.append(str(remainder))
        decimal_value = decimal_value // 16
    dec_list.reverse()
    if dec_list[0] == "0":
        dec_list.pop(0)
    hex_value = "".join(dec_list)
    return hex_value

start_decipher = True
while start_decipher:
    decoding_menu()
    user_decision = int(input("Please enter an option: "))
    if user_decision == 1:
        num_string = (input("Please enter the numeric string to convert: ")).lower()
        print(f"Result: {hex_string_decode(num_string)}\n")
    elif user_decision == 2:
        num_string = (input("Please enter the numeric string to convert: ")).lower()
        print(f"Result: {binary_string_decode(num_string)}\n")
    elif user_decision == 3:
        num_string = (input("Please enter the numeric string to convert: ")).lower()
        print(f"Result: {binary_to_hex(num_string)}\n")
    elif user_decision == 4:
        print("Goodbye!")
        start_decipher = False







