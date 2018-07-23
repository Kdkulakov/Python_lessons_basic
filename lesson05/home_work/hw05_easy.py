# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import os

# создаем директории по списку

def create_dir_in_list(namedir):
    for dir in namedir:
        if not os.path.exists(dir):
            os.makedirs(dir)
            print('Директория {} создана.'.format(dir))
        else:
            print('Что-то пошло не так.')

# удаляем директории по списку

def delete_directory(namedir):
    for dir in namedir:
        if os.path.exists(dir):
            os.rmdir(dir)
            print('Директория {} удалена.'.format(dir))
        else:
            print('Что-то пошло не так.')


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
def show_me_dirs():
    dirs = os.listdir()
    for dir in dirs:
        if os.path.isdir(dir):
            print(dir)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

# source = 'hw05_easy_copy.py'
# dest = 'hw05_easy.py'
# with open(source, 'r') as src, open(dest, 'w') as dst:dst.write(src.read())


def change_current_dir(namedir):
    os.chdir(namedir)
    print('Вы находитесь в папке {}.'.format(namedir))