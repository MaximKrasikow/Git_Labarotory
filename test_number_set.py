import unittest
from abc import ABC, abstractmethod  # Убедитесь, что тестируемый код импортирован правильно

from class_number_set import AverageCalculator, SumCalculator  # Импортируем тестируемые классы


class TestNumberManager(unittest.TestCase):
    
    def test_average_calculator_empty_list(self):
        """Тест: вычисление среднего значения для пустого списка."""
        avg_calc = AverageCalculator("Тест среднего")
        result = avg_calc.calculate()
        self.assertEqual(result, 0, "Ожидалось среднее значение 0 для пустого списка.")
        self.assertIn("Попытка вычислить среднее значение: список пуст.", avg_calc.history)

    def test_sum_calculator_empty_list(self):
        """Тест: вычисление суммы для пустого списка."""
        sum_calc = SumCalculator("Тест суммы")
        result = sum_calc.calculate()
        self.assertEqual(result, 0, "Ожидалось сумма чисел 0 для пустого списка.")
        self.assertIn("Вычислена сумма чисел: 0", sum_calc.history)

    def test_average_calculator_correct(self):
        """Тест: корректное вычисление среднего значения."""
        avg_calc = AverageCalculator("Тест среднего")
        avg_calc.add_number(10)
        avg_calc.add_number(20)
        avg_calc.add_number(30)
        result = avg_calc.calculate()
        self.assertEqual(result, 20, "Ожидалось среднее значение 20.")
        self.assertIn("Вычислено среднее значение: 20.0", avg_calc.history)

    def test_sum_calculator_correct(self):
        """Тест: корректное вычисление суммы."""
        sum_calc = SumCalculator("Тест суммы")
        sum_calc.add_number(5)
        sum_calc.add_number(10)
        sum_calc.add_number(15)
        result = sum_calc.calculate()
        self.assertEqual(result, 30, "Ожидалось сумма чисел 30.")
        self.assertIn("Вычислена сумма чисел: 30", sum_calc.history)

    def test_history_tracking_average(self):
        """Тест: проверка корректности ведения истории операций для AverageCalculator."""
        avg_calc = AverageCalculator("Тест истории")
        avg_calc.add_number(50)
        avg_calc.add_number(100)
        avg_calc.calculate()
        self.assertEqual(len(avg_calc.history), 3, "Ожидалось 3 записи в истории.")
        self.assertIn("Добавлено число: 50", avg_calc.history)
        self.assertIn("Добавлено число: 100", avg_calc.history)
        self.assertIn("Вычислено среднее значение: 75.0", avg_calc.history)

    def test_history_tracking_sum(self):
        """Тест: проверка корректности ведения истории операций для SumCalculator."""
        sum_calc = SumCalculator("Тест истории")
        sum_calc.add_number(20)
        sum_calc.add_number(30)
        sum_calc.calculate()
        self.assertEqual(len(sum_calc.history), 3, "Ожидалось 3 записи в истории.")
        self.assertIn("Добавлено число: 20", sum_calc.history)
        self.assertIn("Добавлено число: 30", sum_calc.history)
        self.assertIn("Вычислена сумма чисел: 50", sum_calc.history)

    def test_reset_functionality_average(self):
        """Тест: сброс данных и истории для AverageCalculator."""
        avg_calc = AverageCalculator("Тест сброса")
        avg_calc.add_number(10)
        avg_calc.add_number(20)
        reset_msg = avg_calc.reset()
        self.assertEqual(reset_msg, "Выполнен сброс списка и истории.")
        self.assertEqual(len(avg_calc.numbers), 0, "Ожидался пустой список чисел после сброса.")
        self.assertEqual(len(avg_calc.history), 0, "Ожидалась пустая история после сброса.")

    def test_reset_functionality_sum(self):
        """Тест: сброс данных и истории для SumCalculator."""
        sum_calc = SumCalculator("Тест сброса")
        sum_calc.add_number(10)
        sum_calc.add_number(20)
        reset_msg = sum_calc.reset()
        self.assertEqual(reset_msg, "Выполнен сброс списка и истории.")
        self.assertEqual(len(sum_calc.numbers), 0, "Ожидался пустой список чисел после сброса.")
        self.assertEqual(len(sum_calc.history), 0, "Ожидалась пустая история после сброса.")

# Запуск тестов
if __name__ == "__main__":
    unittest.main()
