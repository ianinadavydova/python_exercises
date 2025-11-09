from unittest import TestCase
from stack import Stack


"""
Реализовать логику внутри каждого теста,
используя self.stack.push(), self.stack.pop() ...

Проверять результаты с помощью assertEqual, assertTrue, assertFalse ...

Запускать тесты командой:

python -m unittest discover -v
python -m nose2 -v test_stack_
"""

class TestStack(TestCase):
    """Тесты для класса Stack"""

    def setUp(self):
        """Подготовка перед каждым тестом"""
        self.stack = Stack()

    def tearDown(self):
        """Очистка после каждого теста"""
        self.stack = None

    def test_push(self):
        """Тест добавления (push) элемента в стек"""
        self.stack.push(1)
        self.assertEqual(1, self.stack.items[-1])
        self.stack.push("One")
        self.assertEqual("One", self.stack.items[-1])

    def test_pop(self):
        """Тест удаления (pop) элемента из стека"""
        self.stack.push(1)
        print(self.stack.items)
        self.assertEqual(1, self.stack.pop())
        print(self.stack.items)
        self.assertEqual(0, len(self.stack.items))

    def test_peek(self):
        """Тест просмотра верхнего элемента (peek)"""
        self.stack.push(1)
        print(self.stack.items)
        self.assertEqual(1, self.stack.peek())
        self.assertEqual(1, len(self.stack.items))

    def test_is_empty(self):
        """Тест проверки, пуст ли стек"""
        print(self.stack.items)
        self.assertTrue(self.stack.is_empty())
        self.stack.push(1)
        print(self.stack.items)
        self.assertFalse(self.stack.is_empty())
