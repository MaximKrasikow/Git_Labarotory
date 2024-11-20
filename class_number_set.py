from abc import ABC, abstractmethod  # Модуль для реализации абстрактных классов

# Базовый класс для работы с числами
class NumberManager(ABC):
    """
    Абстрактный базовый класс для управления числами.

    Атрибуты:
        name (str): Имя калькулятора.
        numbers (list): Список чисел для операций.
        history (list): История операций.
    """
    def __init__(self, name):
        """
        Конструктор класса NumberManager.
        """
        self.name = name         # Имя типа вычисления (сумма/среднее)
        self.numbers = []        # Список чисел
        self.history = []        # История операций

    def add_number(self, number):
        """
        Функция добаления чисел в список.
        """
        self.numbers.append(number)
        self.history.append(f"Добавлено число: {number}")  # Добавляем запись в историю

    def reset(self):
        """
        Функция сброса списка чисел и очиcтки историю операций.
        """
        self.history.append("Сброс списка чисел.")  # Добавляем запись о сбросе
        self.history = []  # Очищаем историю операций
        self.numbers = []  # Очищаем список чисел
        return f"Выполнен сброс списка и истории."

    @abstractmethod
    def calculate(self):
        """
        Абстрактный метод для реализации расчётов в подклассах.
        Должен быть переопределён в наследуемых классах.
        """
        pass


# Класс для вычисления среднего значения списка чисел
class AverageCalculator(NumberManager):
    """
    Класс для вычисления среднего значения чисел.
    Наследуется от NumberManager.
    """
    def calculate(self):
        """
        Функция вычисления среднего значения чисел в списке.

        Возвращает:
            float: Среднее значение чисел (или 0, если список пуст).
        """
        if not self.numbers:  # Если список чисел пуст
            self.history.append("Попытка вычислить среднее значение: список пуст.")
            return 0  # Возвращаем 0 как результат
        result = sum(self.numbers) / len(self.numbers)  # Среднее значение
        self.history.append(f"Вычислено среднее значение: {result}")  # Запись в историю
        return result


# Класс для вычисления суммы чисел из списка
class SumCalculator(NumberManager):
    """
    Класс для вычисления суммы чисел.
    Наследуется от NumberManager.
    """
    def calculate(self):
        """
        Вычисляет сумму чисел в списке.

        Возвращает:
            int или float: Сумма чисел.
        """
        result = sum(self.numbers)  # Суммируем числа
        self.history.append(f"Вычислена сумма чисел: {result}")  # Запись в историю
        return result


# Пример использования
if __name__ == "__main__":
    # Вычисляем среднее значение чисел
    avg_calc = AverageCalculator("Средний калькулятор")
    avg_calc.add_number(10)  # Добавляем число 10
    avg_calc.add_number(20)  # Добавляем число 20
    print("Среднее значение:", avg_calc.calculate())  # Печатаем результат
    print("История операций:", avg_calc.history)  # Печатаем историю операций

    # Вычисляем сумму чисел
    sum_calc = SumCalculator("Сумматор")
    sum_calc.add_number(5)  # Добавляем число 5
    sum_calc.add_number(15)  # Добавляем число 15
    print("Сумма чисел:", sum_calc.calculate())  # Печатаем результат
    print("История операций:", sum_calc.history)  # Печатаем историю операций
    print("Сброс:", sum_calc.reset())  # Сбрасываем значения чисел и истории

   