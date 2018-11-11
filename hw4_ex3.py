# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

import random

my_list = [random.randint(-50,50) for _ in range(10)]

new_list = [number for number in my_list if number % 3 == 0 and number % 4 != 0 and number > 0]

print(new_list)

