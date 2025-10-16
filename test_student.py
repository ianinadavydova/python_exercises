import unittest

from oop import Student

test_student = Student(last_name="Haha", first_name=50, patronymic="Vasilevich", age=-20, gender="male",
                       faculty="Programming", course=4, specialty="Python", group="group3", expelled=False)

class TestStudentMethods(unittest.TestCase):
    def test_change_faculty(self):
        new_faculty = "Economy"
        test_student.change_faculty(new_faculty)
        self.assertEqual(new_faculty, test_student.faculty)

    def test_raise_course(self):
        course_before_raise = test_student.course
        test_student.raise_course()
        self.assertGreater(test_student.course, course_before_raise)
        self.assertEqual(5, test_student.course)

    def test_error_attrs(self):
        student_with_unknown = Student()
        self.assertIn("unknown", student_with_unknown.__dict__.values())


if __name__ == '__main__':
    unittest.main()
