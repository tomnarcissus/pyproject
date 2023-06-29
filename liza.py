import unittest
import math
# Степаненко Елизавета Романовна. Группа 44-22-121. Вариант 22
# Функция для вычисления значения в соответствии с условиями
def calculate_value(x):
    if x >= 0:
        return math.pow(x, 1/3)  # y = кубический корень из x при x >= 0
    else:
        return math.log(abs(x))  # y = натуральный логарифм модуля x при x < 0

# Класс для функционального теста
class ValueCalculationTest(unittest.TestCase):
    def test_positive_value(self):
        x = 8
        expected_value = 2.0  # Ожидаемое значение при x = 8
        calculated_value = calculate_value(x)
        self.assertEqual(calculated_value, expected_value)

    def test_negative_value(self):
        x = -3
        expected_value = 1.0986122886681098  # Ожидаемое значение при x = -3
        calculated_value = calculate_value(x)
        self.assertEqual(calculated_value, expected_value)

    def test_zero_value(self):
        x = 0
        expected_value = 0.0  # Ожидаемое значение при x = 0
        calculated_value = calculate_value(x)
        self.assertEqual(calculated_value, expected_value)

if __name__ == '__main__':
    unittest.main()


print(calculate_value(-1))