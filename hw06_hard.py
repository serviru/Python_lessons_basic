import os
__author__ = 'Кравченко Сергей'
# Задание-1: Решите задачу (дублированную ниже):

# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки они получают
# удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

# С использованием классов.
# Реализуйте классы сотрудников так, чтобы на вход функции-конструктора
# каждый работник получал строку из файла

class Employee:

    def __init__(self, data):
        self.name = ' '.join(data.split()[:2])
        self.wage = int(data.split()[2])
        self.planed_hours = int(data.strip().split()[4])

    def __repr__(self):
        return self.name

    def add_worked_hours(self, worked_hours_data):
        for data in worked_hours_data:
            name = ' '.join(data.split()[:2])
            if self.name == name:
                self.worked_hours = int(data.strip().split()[-1])

    @property
    def real_wage(self):
        if self.worked_hours:
            if self.planed_hours >= self.worked_hours:
                return self.wage * self.worked_hours / self.planed_hours
            overtime = self.worked_hours - self.planed_hours
            overtime_wage = overtime * self.wage / self.planed_hours
            return self.wage * self.planed_hours / self.planed_hours + overtime_wage


def load_data(filepath, exclude_header=False):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r') as file_handler:
        if exclude_header:
            next(file_handler)
        return file_handler.readlines()


if __name__ == '__main__':
    filename = os.path.join('data', 'workers')
    employees_data = load_data(filename, exclude_header=True)
    employees = [Employee(data) for data in employees_data]
    filename = os.path.join('data', 'hours_of')
    worked_hours_data = load_data(filename, exclude_header=True)
    print('{:<20}{}'.format('Employee', 'Wage'))
    for employee in employees:
        employee.add_worked_hours(worked_hours_data)
        print('{:<20}{:.2f}'.format(employee.name, employee.real_wage))
