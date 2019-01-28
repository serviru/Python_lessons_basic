__author__ = 'Кравченко Сергей'

# задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.

def main(args):
    if len(args) == 3:
        if args[1] == 'cp':
            filename = args[2]
            copyname = '{}.copy'.format(filename)
            shutil.copy(filename, copyname)
        elif args[1] == 'rm':
            filename = args[2]
            choice = input(
                'Вы действительно хотите'
                'удалить файл {} ? (д/Н)'.format(filename))
            if choice == 'д':
                os.remove(filename)
        elif args[1] == 'cd':
            path = args[2]
            os.chdir(path)
            print(os.getcwd())
    elif len(args) == 2 and args[1] == 'ls':
        full_path = os.getcwd()
        print('Полный путь текущей директории: {}'.format(full_path))


if __name__ == '__main__':
    args = sys.argv
    main(args)
