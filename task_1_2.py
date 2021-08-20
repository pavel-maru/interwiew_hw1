# 2. Дополнить следующую функцию недостающим кодом:


def print_directory_contents(sPath):
    """
    Функция принимает имя каталога и распечатывает его содержимое
    в виде «путь и имя файла», а также любые другие
    файлы во вложенных каталогах.
    Эта функция подобна os.walk. Использовать функцию os.walk
    нельзя. Данная задача показывает ваше умение работать с
    вложенными структурами.
    """

    import os
    for sChild in os.listdir(sPath):
        sChildPath = os.path.join(sPath, sChild)
        if os.path.isdir(sChildPath):
            print_directory_contents(sChildPath)
        else:
            print(sChildPath)


print_directory_contents('course_3')


#     def get_directory_files(sPath):
#         struct = []
#         for file_or_directory in os.listdir(sPath):
#             full_name = os.path.join(os.path.abspath(sPath), file_or_directory)
#             if os.path.isfile(full_name):
#                 struct.append((os.path.abspath(sPath), file_or_directory))
#             else:
#                 struct.extend(get_directory_files(full_name))
#         return struct
#
#     print(get_directory_files(sPath))
