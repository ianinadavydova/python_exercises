input_number = int(input("Enter a decimal number: "))

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


print("Десятичному числу " + str(input_number) + " соответствует:\n" +
      ("двоичное число " + "".join(make_binary_octa_or_hex_number(2, input_number))) + "\n" +
      ("восьмеричное число " + "".join(make_binary_octa_or_hex_number(8, input_number))) + "\n" +
      ("шестнадцатеричное число " + "".join(make_binary_octa_or_hex_number(16, input_number))))


