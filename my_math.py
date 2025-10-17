import math
import random

class MathTasks:

    # arithmetic
    def task1(self, a: int, b: int) -> list[str]:
        return [
            f"{a} + {b} = {a + b}",
            f"{a} - {b} = {a - b}",
            f"{a} * {b} = {a * b}",
            f"{a} / {b} = {a / b:.3f}"
        ]

    # calculations
    def task2(self, a: float, b: float, c: float) -> float:
        result = abs(a - c) / (b + c) * (a**2 + b**2 - c) / (2 * (math.sqrt(b + c**2)) * 3)
        return round(result, 4)

    # division
    def task3(self, a: int, b: int) -> dict[str, float | int]:
        div_full = a / b
        div_int = a // b
        div_rem = a % b
        return {
            "полное_деление": div_full,
            "деление_нацело": div_int,
            "остаток": div_rem,
            "проверка_1": div_full * b,
            "проверка_2": div_int * b + div_rem
        }

    # division 3 digit
    def task4(self, n: int) -> tuple[int, int, int]:
        hundreds = n // 100
        tens = (n // 10) % 10
        ones = n % 10
        return (hundreds, tens, ones)

    # reverse number
    def task5(self, n: int) -> tuple[int, int]:
        thousands = n // 1000
        hundreds = (n // 100) % 10
        tens = (n // 10) % 10
        ones = n % 10
        reversed_num = ones * 1000 + tens * 100 + hundreds * 10 + thousands
        difference = n - reversed_num
        return reversed_num, difference

    # move point
    def task7(self, x: float, y: float, distance: float, angle_deg: float) -> tuple[int, int]:
        radians = math.radians(angle_deg)
        x
