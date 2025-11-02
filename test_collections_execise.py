import unittest
from collections_exercise import return_grades_counts, return_day_or_index, find_lesson_days

test_days = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]


class TestCollectionMethods(unittest.TestCase):

    def test_return_day_or_index_string(self):
        for i in test_days:
            self.assertEqual(test_days.index(i) + 1, return_day_or_index(i))

    def test_return_day_or_index_number(self):
        for i in range(1, 8):
            test_index_number = i
            self.assertEqual(test_days[i - 1], return_day_or_index(test_index_number))

    def test_return_day_or_index_not_existing_index(self):
        self.assertEqual(None, return_day_or_index(0))

    def test_return_day_or_index_not_existing_string(self):
        self.assertEqual(None, return_day_or_index("Saturda"))

    def test_return_grades_counts_basic(self):
        test_grades = {"Anna": 5, "Peter": 4, "Viktoria": 5, "Harry": 3, "Daria": 4, "Yana": 5}
        expected = {5: 3, 4: 2, 3: 1}
        self.assertEqual(expected, return_grades_counts(test_grades))

    def test_return_grades_counts_empty_input(self):
        test_grades = {}
        expected = {}
        self.assertEqual(expected, return_grades_counts(test_grades))

    def test_return_grades_counts_all_same(self):
        grades = {"Anna": 4, "Pter": 4, "Harry": 4, "John": 4}
        expected = {4: 4}
        self.assertEqual(expected, return_grades_counts(grades))

    def test_find_lesson_days_math(self):
        expected = ["Monday", "Wednesday", "Friday"]
        self.assertEqual(find_lesson_days("math"), expected)

    def test_find_lesson_days_english(self):
        expected = ["Tuesday", "Thursday"]
        self.assertEqual(find_lesson_days("english"), expected)

    def test_find_lesson_days_not_existing(self):
        expected = "Lesson 'art' not found in the schedule."
        self.assertEqual(find_lesson_days("art"), expected)

