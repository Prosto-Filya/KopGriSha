# painting_cost_calculator.py

class PaintingCostCalculator:
    # Базовая стоимость покраски
    BASE_COST = 12000

    # Словари с коэффициентами для цвета и детали
    COLOR_COEFFICIENTS = {
        "белый": 1,
        "синий": 1,
        "желтый": 1.1,
        "красный": 1,
        "перламутровый": 1.2,
        "серый металлик": 1.3,
    }

    PART_COEFFICIENTS = {
        "капот": 1,
        "передняя дверь": 1.2,
        "задняя дверь": 1.1,
        "передний бампер": 1,
        "задний бампер": 1,
        "крыша": 1.1,
    }

    def __init__(self, part, color):
        """
        Инициализация объекта.
        :param part: Наименование детали (строка)
        :param color: Цвет (строка)
        """
        self.part = part.lower()
        self.color = color.lower()

    def validate_input(self):
        """
        Проверяет, существуют ли введенные данные в словарях.
        :return: True, если данные корректны, иначе False.
        """
        if self.part not in self.PART_COEFFICIENTS:
            print("Ошибка: Деталь не найдена в списке.")
            return False
        if self.color not in self.COLOR_COEFFICIENTS:
            print("Ошибка: Цвет не найден в списке.")
            return False
        return True

    def calculate_cost(self):
        """
        Рассчитывает стоимость покраски.
        :return: Стоимость покраски (число) или None, если данные некорректны.
        """
        if not self.validate_input():
            return None

        # Получаем коэффициенты
        part_coeff = self.PART_COEFFICIENTS[self.part]
        color_coeff = self.COLOR_COEFFICIENTS[self.color]

        # Рассчитываем стоимость
        total_cost = self.BASE_COST * part_coeff * color_coeff
        return total_cost