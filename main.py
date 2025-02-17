# main.py

from painting_cost_calculator import PaintingCostCalculator

# Ввод данных от пользователя
part_input = input("Введите наименование детали: ")
color_input = input("Введите цвет: ")

# Создание объекта и расчет стоимости
calculator = PaintingCostCalculator(part_input, color_input)
cost = calculator.calculate_cost()

# Вывод результата
if cost is not None:
    print(f"Стоимость покраски детали '{part_input}' в цвет '{color_input}' составляет: {cost:.2f} рублей.")