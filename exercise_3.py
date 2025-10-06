#input_number = int(input("Enter a decimal number: "))

def make_binary_octa_or_hex_number(base, decimal):
    output_digits_binary = []
    x = decimal
    while x != 0:
        x, z = divmod(x, base)
        if base == 16 and 10 <= z <= 15:
            hex_symbols = {
                    10: "A",
                    11: "B",
                    12: "C",
                    13: "D",
                    14: "E",
                    15: "F"
                }
            output_digits_binary.append(hex_symbols.get(z))
        else:
            output_digits_binary.append(str(z))
    prefixes = {
        2: "0b",
        8: "0o",
        16: "0x"
    }
    output_digits_binary.append(prefixes.get(base))

    output_digits_binary.reverse()
    return output_digits_binary

def make_convert(int_number:int) -> tuple:
    """
    function convert from decimal to bin, oct and hex
    :param input_number: integer positive value
    :return: tuple with string value
    >>> make_convert(168)
    ('10101000', '250', 'a8')
    >>> make_convert(145)
    ('10010001', '221', '91')
    """
    if type(int_number) not in [int]:
        raise TypeError("Int number must be a decimal integer number")
    if int_number <= 0:
        raise ValueError("Int number must be a positive number")
    return bin(int_number)[2:], oct(int_number)[2:], hex(int_number)[2:]

print(make_convert(-250))

# print("Десятичному числу " + str(input_number) + " соответствует:\n" +
#       ("двоичное число " + "".join(make_binary_octa_or_hex_number(2, input_number))) + "\n" +
#       ("восьмеричное число " + "".join(make_binary_octa_or_hex_number(8, input_number))) + "\n" +
#       ("шестнадцатеричное число " + "".join(make_binary_octa_or_hex_number(16, input_number))))

def my_function(x, y):
    """

    Args:
        x:
        y:

    Returns:

    >>>
    """
