__author__ = 'Кравченко Сергей'

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

def create_dirs():
    for x in ('dir_{}'.format(x) for x in range(1, 10)):
def create_dir(dirname):
        try:
            os.mkdir(x)
            os.mkdir(dirname)
            print('Директория "{}" успешно создана'.format(dirname))
        except FileExistsError:
            print('Error. Directory "{}" already exists.'.format(x))
            print('Ошибка. Невозможно создать директорию "{}"'.format(dirname))


def remove_dirs():
    for x in ('dir_{}'.format(x) for x in range(1, 10)):
def remove_dir(dirname):
        try:
            os.rmdir(x)
            os.rmdir(dirname)
            print('Директория "{}" успешно удалена'.format(dirname))
        except FileNotFoundError:
            print('Error. Directory "{}" not found'.format(x))
            print('Ошибка. Невозможно удалить директорию "{}"'.format(dirname))

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def show_dirs():
    return sorted([x.name for x in os.scandir() if x.is_dir()])
def show_dirs(directory=None):
    return sorted([x.name for x in os.scandir(directory) if x.is_dir()])


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

if __name__ == '__main__':
    create_dirs()
    remove_dirs()
    (create_dir('dir_{}'.format(x)) for x in range(1, 10))
    (remove_dir('dir_{}'.format(x)) for x in range(1, 10))
    dirs = show_dirs()
    if dirs:
        print('Список директорий в текущем каталоге:')
