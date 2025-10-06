# input_decimal_number = input("Enter a decimal number: ")
# input_octal_number = input("Enter an octal number: ")
# input_hex_number = input("Enter a hexadecimal number: ")

octal_switch = {
    "0": "000",
    "1": "001",
    "2": "010",
    "3": "011",
    "4": "100",
    "5": "101",
    "6": "110",
    "7": "111",
    "8": "1111"
}

hex_switch = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "a": "1010",
    "b": "1011",
    "c": "1100",
    "d": "1101",
    "e": "1110",
    "f": "1111"
}

def modulo_by_2(x):
    return x & 1

def div_2(x):
    return x >> 1

def decimal_to_binary(decimal):
    output_digits_binary = []
    x = decimal
    while x != 0:
        z = modulo_by_2(x)
        x = div_2(x)
        output_digits_binary.append(str(z))
    output_digits_binary.reverse()
    return output_digits_binary

def hex_or_oct_to_binary(input, input_base):
    output_str_binary = ""
    for digit in input:
        if input_base == 16:
            output_str_binary += hex_switch.get(digit.lower())
        elif input_base == 8:
            output_str_binary += octal_switch.get(digit)
    while output_str_binary[0] == "0":
        output_str_binary = output_str_binary[1:]
    return output_str_binary

# print("Десятичному числу " + input_decimal_number + " соответствует:\n" +
#       ("двоичное число " + "".join(decimal_to_binary(int(input_decimal_number)))) + "\n" +
#       ("восьмеричное число " + hex_or_oct_to_binary(input_octal_number, 8) + "\n" +
#       ("шестнадцатеричное число " + hex_or_oct_to_binary(input_hex_number, 16))))

def convert_dec_bin(num):
    return bin(num)[2:]

def convert_oct_bin(num):
    int_num = int(num, 8)
    print(int_num, type(int_num))
    return bin(int_num)[2:]

def convert_hex_bin(num):
    int_num = int(num, 16)
    print(int_num, type(int_num))
    return bin(int_num)[2:]






















print(convert_dec_bin(8))
print(convert_oct_bin("23"))
print(convert_hex_bin("F5"))

