#!/usr/bin/python3
import os
from random import shuffle, sample
__author__ = 'Сергей Кравченко'

"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87      
      16 49    55 77    88    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html

"""
class Ticket:

    def __init__(self):
        self.ticket = [' ' for x in range(27)]
        random_nums = sorted(sample(range(1, 91), 15), reverse=True)
        random_indexes = sample(range(9), 5)
        random_indexes += sample(range(9, 18), 5)
        random_indexes += sample(range(18, 27), 5)
        for index in sorted(random_indexes):
            self.ticket[index] = random_nums.pop()

    def __str__(self):
        return '{}\n{}\n{}'.format('  '.join(str(x) for x in self.ticket[:9]),
                                   '  '.join(str(x)
                                             for x in self.ticket[9:18]),
                                   '  '.join(str(x) for x in self.ticket[18:]))

    def __repr__(self):
        return self.__str__()

    def __iter__(self):
        return iter(self.ticket)

    @property
    def empty(self):
        return not any(str(x).isnumeric() for x in set(self.ticket))

    def check(self, value):
        self.ticket = ['-' if x == value else x for x in self.ticket]


class Bag:

    def __init__(self):
        self.index = 90
        self.__bag = [x for x in range(1, 91)]
        shuffle(self.__bag)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index > 0:
            self.index -= 1
            return self.__bag.pop()
        else:
            raise StopIteration

    def __str__(self):
        return '{} бочонков осталось в мешке'.format(self.index)

    def __repr__(self):
        return self.__str__()


class Game:

    def __init__(self):
        self.ticket1 = Ticket()
        self.ticket2 = Ticket()
        self.bag = Bag()

    def start(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        for number in self.bag:
            print('Новый бочонок: {} (осталось {})'.format(
                number, self.bag.index))
            print('-------- Ваша карточка -------')
            print(self.ticket1)
            print('------------------------------')
            print('---- Карточка компьютера -----')
            print(self.ticket2)
            print('------------------------------')
            answer = input('Зачеркнуть цифру? (y/n): ')
            if answer not in ('y', 'n'):
                result = 'Вы проиграли.'
                break
            if answer == 'y' and number not in self.ticket1:
                result = 'Вы проиграли.'
                break
            elif answer == 'n' and number in self.ticket1:
                result = 'Вы проиграли.'
                break
            if number in self.ticket1:
                self.ticket1.check(number)
            if self.ticket1.empty:
                result = 'Поздравляем. Вы выиграли!'
                break
            if number in self.ticket2:
                self.ticket2.check(number)
            if self.ticket2.empty:
                result = 'Вы проиграли.'
                break
            os.system('cls' if os.name == 'nt' else 'clear')
        print(result)


if __name__ == '__main__':
    game = Game()
    game.start()
    input()
