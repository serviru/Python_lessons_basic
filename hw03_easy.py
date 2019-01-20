__author__ = "Кравченко Сергей Иванович"

# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    pass


print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))

def my_round(number, ndigits):
    int_ndigits = int(ndigits)
    degree = pow(10,int(ndigits))
    mul =  number*degree
    res = int(mul)
    ost = mul-res
# print(number,mul,res,ost)
    if not (abs(ost) < 0.5):
        if res>0: res+=1
        else: res-=1
    return res/degree



my_round(2.1234567, 5)


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    pass


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))


def lucky_ticket(ticket_number):
    tn_list=str(ticket_number)
    if len(tn_list) != 6: return False
    first=0
    last=0
    for i in range(3):
        first+=int(tn_list[i])
        last+=int(tn_list[-i-1])
    return first==last

def test(got, expected):
    prefix = "OK" if got == expected else "X"
    print("{0} - Получено: {1} | Ожидалось: {2}".format(prefix, repr(got), repr(expected)))

print("Задача 1. Округление.")
test(my_round(5.234,2),5.23)
test(my_round(5.255,2),5.26)
test(my_round(-5.245,1),-5.2)
test(my_round(-5.255,1),-5.3)

print("\nЗадача 2. Билет.")
test(lucky_ticket(345534),True)
test(lucky_ticket("045414"),True)
test(lucky_ticket(345043),False)
test(lucky_ticket(345542),False)

