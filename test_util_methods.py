import unittest

from util_methods import (
    output_word_with_dash,
    output_person_info,
    make_convert,
    convert_dec_bin,
    convert_oct_bin,
    convert_hex_bin,
    align_numbers,
    print_square_of_figures,
)


class TestBasicFunctions(unittest.TestCase):

    def test_output_word_with_dash_happy_path(self):
        result = output_word_with_dash("Python C# Pascal")
        self.assertIn("-", result)
        self.assertNotIn(" ", result)
        self.assertTrue(result.startswith("Python"))
        self.assertTrue(result.endswith("Pascal"))

    def test_output_word_with_dash_empty(self):
        self.assertEqual(output_word_with_dash(""), "")

    def test_output_word_with_dash_nospaces(self):
        self.assertEqual(output_word_with_dash("PythonC#Pascal"), "PythonC#Pascal")

    def test_output_person_info_normal(self):
        result = output_person_info("Иванов", "Иван", 25)
        self.assertEqual(result, "Вас зовут Иван Иванов. Ваш возраст: 25")

    def test_output_person_info_case_insensitive(self):
        result = output_person_info("иВанова", "мария", 30)
        self.assertEqual(result, "Вас зовут Мария Иванова. Ваш возраст: 30")

    def test_make_convert_valid(self):
        self.assertEqual(make_convert(168), ('10101000', '250', 'a8'))

    def test_make_convert_type_error(self):
        with self.assertRaises(TypeError):
            make_convert("this_is_string")

    def test_make_convert_value_error(self):
        with self.assertRaises(ValueError):
            make_convert(0)

    def test_convert_dec_bin(self):
        self.assertEqual(convert_dec_bin(168), '10101000')
        self.assertEqual(convert_dec_bin(0), '0')

    def test_convert_oct_bin(self):
        result = convert_oct_bin('17')
        self.assertEqual(result, '1111')
        self.assertEqual(convert_dec_bin(0), '0')

    def test_convert_hex_bin(self):
        result = convert_hex_bin('1A')
        self.assertEqual(result, '11010')

    def test_align_numbers(self):
        aligned = align_numbers(12, 345, 6789)
        expected = "  12\n 345\n6789"
        self.assertEqual(aligned, expected)


    def test_print_square_of_figures_output(self):
        self.assertEqual(print_square_of_figures(5, 3), "Sп = 5.00; Sт = 3.00.")
        self.assertEqual(print_square_of_figures(2.345, 7.891), "Sп = 2.35; Sт = 7.89.")


if __name__ == '__main__':
    unittest.main()
