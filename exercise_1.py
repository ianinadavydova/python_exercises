"""Module for working with strings."""

def output_word_with_dash():
    """
    This function is about replacing spaces
    :return:
    """
    words = input("Enter 3 words separated by space: ")
    words = words.replace(" ", "-")
    print(words)


output_word_with_dash()
