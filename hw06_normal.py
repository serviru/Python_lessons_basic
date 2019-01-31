from random import randint
__author__ = 'Кравченко Сергей'
# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе


class People:

    def __init__(self, lastname, firstname, patronymic):
        """ Initialization method of People class
        Args:
            lastname (str): Lastname of a people.
            firstname (str): Firstname of a people.
            patronymic (str): Patronymic of a people.
        """
        self.lastname = lastname
        self.firstname = firstname
        self.patronymic = patronymic

    def __repr__(self):
        return '{} {:.1}.{:.1}.'.format(self.lastname,
                                        self.firstname,
                                        self.patronymic)


class Student(People):

    def __init__(self, lastname, firstname, patronymic, class_room, father, mother):
        super().__init__(lastname, firstname, patronymic)
        self._class_room = {'class_num': class_room.split()[0],
                            'class_letter': class_room.split()[1]}
        self.father = father
        self.mother = mother

    @property
    def class_room(self):
        return '{} {}'.format(self._class_room['class_num'],
                              self._class_room['class_letter'])


class Teacher(People):

    def __init__(self, lastname, firstname, patronymic, subject):
        super().__init__(lastname, firstname, patronymic)
        self.subject = subject
        self.class_rooms = []

    def add_to_class(self, class_room):
        if class_room not in self.class_rooms:
            self.class_rooms.append(class_room)
        else:
            raise ValueError('Teacher {} was already'
                             'added to class_room "{}"'.format(
                                 self.__repr__(), class_room))


if __name__ == '__main__':

    class_rooms = ['5 A', '6 B', '7 D', '8 A']

    students = [
        Student('Ivanov', 'Ivan', 'Ivanovich', class_rooms[randint(0, len(
            class_rooms) - 1)], People('Ivanov', 'Ivan', 'Sergeevich'),
            People('Ivanova', 'Darya', 'Petrovna')),
        Student('Petrov', 'Peter', 'Petrovich', class_rooms[randint(0, len(
            class_rooms) - 1)], People('Petrov', 'Peter', 'Sergeevich'),
            People('Petrova', 'Anya', 'Petrovna')),
        Student('Sidorov', 'Egor', 'Egorovich', class_rooms[randint(0, len(
            class_rooms) - 1)], People('Sidorov', 'Egor', 'Sergeevich'),
            People('Sidorova', 'Katya', 'Petrovna')),
        Student('Fedorov', 'Sergey', 'Victorovich', class_rooms[randint(0, len(
            class_rooms) - 1)], People('Fedorov', 'Victor', 'Sergeevich'),
            People('Fedorova', 'Lena', 'Petrovna'))
    ]

    teachers = [
        Teacher('Nesterov', 'Alexey', 'Victorovich', 'Math'),
        Teacher('Bolshov', 'Nester', 'Petrovich', 'English'),
        Teacher('Grefman', 'Victor', 'Alexeevich', 'Music')
    ]

    # Задача-1
    all_classes = list(set([x.class_room for x in students]))
    print('All classrooms which students attends: {}'.format(all_classes))
    # Задача-2
    class_room = class_rooms[randint(0, len(class_rooms) - 1)]
    all_students = [x for x in students if x.class_room == class_room]
    print('All students in classroom {}: {}'.format(class_room, all_students))
    # Задача-3
    for class_room in class_rooms:
        teachers[0].add_to_class(class_room)
        teachers[1].add_to_class(class_room)
    teachers[2].add_to_class('7 D')
    student = students[randint(0, len(students) - 1)]
    subjects = [
        x.subject for x in teachers if student.class_room in x.class_rooms]
    print('Student {} attends the following subject(s): {}'.format(student,
                                                                   subjects))
    # Задача-4
    student = students[randint(0, len(students) - 1)]
    print('Student {} father: {}'.format(student, student.father))
    print('Student {} mother: {}'.format(student, student.mother))
    # Задача-5
    # 5. Получить список всех Учителей, преподающих в указанном классе
    class_room = class_rooms[randint(0, len(class_rooms) - 1)]
    teachers_in_class = [x for x in teachers if class_room in x.class_rooms]
    print('Teachers in class "{}": {}'.format(class_room, teachers_in_class))
