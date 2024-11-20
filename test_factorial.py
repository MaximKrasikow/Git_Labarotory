import unittest
from class_factorial import FactorialCalculator

class TestFactorialCalculator(unittest.TestCase):

    def test_iterative_factorial_valid(self):
        """Тест: Корректность расчёта факториала положительного числа."""
        calc = FactorialCalculator(5)
        result = calc.calculate()
        self.assertEqual(result, 120, "Ошибка в расчёте факториала для числа 5.")

    def test_zero_factorial(self):
        """Тест: Факториал 0 равен 1 (по определению)."""
        calc = FactorialCalculator(0)
        result = calc.calculate()
        self.assertEqual(result, 1, "Ошибка в расчёте факториала для числа 0.")

    def test_large_number(self):
        """Тест: Факториал большого числа для проверки корректности."""
        calc = FactorialCalculator(10)
        result = calc.calculate()
        self.assertEqual(result, 3628800, "Ошибка в расчёте факториала для числа 10.")

    def test_negative_number_raises_error(self):
        """Тест: Факториал отрицательного числа вызывает ValueError."""
        calc = FactorialCalculator(-5)
        with self.assertRaises(ValueError):
            calc.calculate()

# Запуск тестов
if __name__ == "__main__":
    unittest.main()
