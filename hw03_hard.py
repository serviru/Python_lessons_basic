__author__ = "Кравченко Сергей Иванович"

# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3

def  get_fractions_with_operand ( выражение ):
    '' ' Функция возвращает приведенные дробные и операторные выражения ' ''
    операнды = []
    # Получаем оператор выражения
    operator = re.search ( ' . [- +]. ' , выражение) .group ( 0 ) .strip ()
    # Получаем сырые операнды
    parts = re.split ( ' . [- +]. ' , выражение)
    для операнда по частям:
        # Разделяем операнд
        operand_parts = operand.split ()
        # Если длина списка равна 2-м, то есть целая и дробная части
        if  len (operand_parts) ==  2 :
            # Преобразуем целую часть операнда для первых вычислений
            first_operand_part =  int (operand_parts [ 0 ])
            last_operand_part = operand_parts [ 1 ]
            # Разделяем дробную часть для открытых вычислений
            fraction_parts = last_operand_part.split ( ' / ' )
            # Перемножаем знаменатель из дробной части и целую часть
            figurerator_part =  int ( фракция_частей [ 1 ]) * first_operand_part
            если numberrator_part <  0 :
                # Если выражение отрицательное, вычитаем числитель
                числитель = числитель_часть -  int (дробная_часть [ 0 ])
            еще :
                # Если положительное, прибавляем числитель
                числитель = числитель_часть +  int (дробная_часть [ 0 ])
            # Для читаемости указываем переменную для знаменателя
            знаменатель = фракция_частей [ 1 ]
            operands.append ( ' {} / {} ' .format (числитель, знаменатель))
        # В противном случае имеем только дробную часть
        еще :
            operands.append (операнд)
    возвратные операнды, оператор


def  sum_fractions ( операнды , оператор ):
    '' ' Функция возвращает результат операции с двумя дробями ' ''
    # Первый числитель
    first_numerator =  int ( operands [ 0 ] .split ( ' / ' ) [ 0 ])
    # Первый знаменатель
    first_denominator =  int (операнды [ 0 ] .split ( ' / ' ) [ 1 ])
    # Второй числитель
    second_numerator =  int (операнды [ 1 ] .split ( ' / ' ) [ 0 ])
    # Второй знаменатель
    second_denominator =  int (операнды [ 1 ] .split ( ' / ' ) [ 1 ])
    # Получаем итоговый знаменатель
    common_denominator = first_denominator * second_denominator
    если оператор ==  ' + ' :
        common_numerator = first_numerator * second_denominator + \
            second_numerator * first_denominator
    еще :
        common_numerator = first_numerator * second_denominator - \
            second_numerator * first_denominator
    # Проверяем что числитель больше знаменателя
    if  abs (common_numerator) > = common_denominator:
        floor_part =  int (common_numerator / common_denominator)
        Fraction_numerator =  abs (common_numerator) % common_denominator
        Fraction_denominator = Common_denominator
        return  ' {}  {} / {} ' .format (floor_part,
                                 дробный_числитель, дробный_доменатор)
    return  ' {} / {} ' .format (common_numerator, common_denominator)


# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

def  load_data ( filepath , exclude_header = False ):
    если  нет os.path.exists (filepath):
        возврат  Нет
    с  открытым (filepath, ' r ' ) в качестве file_handler:
        если exclude_header:
            следующий (file_handler)
        вернуть file_handler.readlines ()


def  create_employees_dict ( employee_data ):
    names = ( '  ' .join (x.split () [: 2 ]) для x в параметрах employee_data)
    wages = ( int (x.split () [ 2 ]) для x в employee_data)
    planed_hours = ( int (x.strip ( ' \ n ' ) .split () [ 4 ]) для x в employee_data)
    return  dict ( zip (names, [ list (x) для x в  zip (wages, planed_hours)]))


def  create_employees_hours_dict ( hours_data ):
    names = ( '  ' .join (x.split () [: 2 ]) для x в hours_data)
    works_hours = ( int (x.strip ( ' \ n ' ) .split () [ - 1 ]) для x в hours_data)
    вернуть  dict ( zip (names, works_hours))


def  create_full_dict ( сотрудники , раб_часы ):
    employee_copy = deepcopy (сотрудников)
    для имени в employee_copy:
        employees_copy [имя] .append (worked_hours [имя])
    возврат сотрудников


Защиту  calculate_wage ( full_employees_data ):
    full_employees_data_copy = deepcopy (full_employees_data)
    для имени, данные в full_employees_data_copy.items ():
        заработная плата = данные [ 0 ]
        planed_hours = data [ 1 ]
        works_hours = data [ 2 ]
        if planed_hours > = works_hours:
            real_wage = заработная плата * works_hours / planed_hours
        еще :
            сверхурочное время = отработанные часы - плановые часы
            overtime_wage = overtime * wage / planed_hours
            real_wage = заработная плата * planed_hours / planed_hours + overtime_wage
        data.append (real_wage)
    вернуть full_employees_data_copy


# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))

def  get_fruits_dict ( фрукты ):
    fruits_dict = {}
    fruits_capitals = (first_letter [ 0 ] для first_letter во фруктах)
    для письма в fruits_capitals:
        fruits_dict [letter] = [x для x во фруктах, если буква == x [ 0 ]]
    вернуть фрукты


def  write_fruits_to_files ( fruits_dict ):
    для письма, фрукты в fruits_dict.items ():
        filename = os.path.join ( ' data ' , ' fruits_ {} ' .format (letter))
        с  открытым (имя файла, ' w + ' ) в качестве f_handler:
            f_handler.write ( ' \ n ' .join (фрукты))


если  __name__  ==  ' __main__ ' :
