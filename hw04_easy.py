__author__ = 'Кравченко Сергей'

# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами. 
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

def gen_sqares(numbers_list):
    return [x ** 2 for x in numbers_list]

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

def gen_fruits(fruits_first_list, fruits_second_list):
    return [x for x in fruits_first_list if x in fruits_second_list]

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

def gen_numbers_list(numbers_list):
    return [x for x in numbers_list if x % 3 == 0 and x > 0 and x % 4 != 0]


''' Задание 1 '''
    print()
    numbers_list = list(range(-5, 5))
    squares_list = gen_sqares(numbers_list)
    print('Исходный список: {}'.format(numbers_list))
    print('Полученный список: {}'.format(squares_list))
    print()
''' Задание 2 '''
    fruits_first_list = ['яблоко', 'банан', 'груша', 'слива', 'персик']
    fruits_second_list = ['виноград', 'маракуя', 'папая', 'банан', 'персик']
    fruits_not_unique = gen_fruits(fruits_first_list, fruits_second_list)
    print('Общие фрукты в двух списках: {}'.format(fruits_not_unique))
    print()
''' Задание 3 '''
    numbers_list = [randint(-13, 13) for x in range(10)]
    new_numbers_list = gen_numbers_list(numbers_list)
    print('Исходный список: {}'.format(numbers_list))
    print('Новый список удовлетворяющий условиям: {}'.format(new_numbers_list))
    print()
