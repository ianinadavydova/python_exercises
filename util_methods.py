"""Module for different helpful methods"""

def output_word_with_dash(input_words: str) -> str:
    """
    function replaces spaces to dashes
    :param input_words: string with spaces in it
    :return: string with dashes instead of spaces
    >>> output_word_with_dash("Python C# Pascal")
    'Python-C#-Pascal'
    >>> output_word_with_dash("")
    ''
    """
    output = input_words.replace(" ", "-")
    return output

def output_person_info(input_surname: str, input_name: str, input_age: int) -> str:
    """
    function gets 3 strings with person's data and returns message containing these data
    :param input_surname: string containing person's surname
    :param input_name: string containing person's name
    :param input_age: integer containing person's surname
    :return: message containing these strings
    >>> output_person_info("Иван", "Иванов", 25)
    'Вас зовут Иванов Иван. Ваш возраст: 25'
    """
    output = ("Вас зовут " + input_name.capitalize() + " "\
              + input_surname.capitalize() + ". Ваш возраст: " + str(input_age))
    return output

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

def convert_dec_bin(num: int) -> str:
    """
    function converts decimal number to binary number
    :param num: integer
    :return: str
    >>> convert_dec_bin(168)
    '10101000'
    """
    return bin(num)[2:]

def convert_oct_bin(num: str) -> str:
    """
       converts octagonal number to binary without '0b' prefix.

       >>> convert_oct_bin('17')
       '1111'
       """
    int_num = int(num, 8)
    return bin(int_num)[2:]

def convert_hex_bin(num: str) -> str:
    """
    converts hexagonal number to binary without prefix '0b'.

    >>> convert_hex_bin('1A')
    '11010'
    """
    int_num = int(num, 16)
    return bin(int_num)[2:]

def align_numbers(input_2_digits_number, input_3_digits_number, input_4_digits_number) -> str:
    """Method for format numbers"""
    return (f"{input_2_digits_number:>4}" + "\n"
           + f"{input_3_digits_number:>4}" + "\n"
           + f"{input_4_digits_number:>4}")

def print_square_of_figures(input_s_rectangle, input_s_triangle) -> str:
    """
    Returns formatted string with squares of figures.
    >>> print_square_of_figures(5, 3)
    'Sп = 5.00; Sт = 3.00.'
    >>> print_square_of_figures(2.345, 7.891)
    'Sп = 2.35; Sт = 7.89.'
    """
    output = f"Sп = {float(input_s_rectangle):.2f}; Sт = {float(input_s_triangle):.2f}."
    return output

if __name__ == "__main__":
    print(convert_hex_bin("5f"))
    import doctest
    print(doctest.testmod(verbose=True))
