import json

FILE_NAME = 'library.json'


def get_library_from_json():
    '''
    Функция читает файл FILENAME и восстанавливает объект из файла
    :return:объект (список словарей)
    '''
    with open(FILE_NAME, 'r') as f:
        library = json.load(f)
    return library


def library_to_json(obj):
    '''
    Функция, которая сохраняет obj в json файл
    :param obj:объект для записи
    :return:
    '''
    with open(FILE_NAME, 'w') as f:
        json.dump(obj, f, indent=4)


def add_(lib: list, book: dict):
    '''
    Функция, добавляющая книгу в словарь
    :param lib: Библиотека книг (список словарей)
    :param book: Книга (словарь)
    :return: Библиотеку книг
    '''
    lib.append(book)
    return lib


def delete_(lib: list, number_to_delete: int):
    '''
    Функция, удаляющая книгу из библиотеки. При каждом удалении книги обновляется нумерация книг
    :param lib: Библиотека (список словарей)
    :param number_to_delete: Номер книги, которую необходимо удалить
    :return: Библиотеку
    '''
    i = 1
    for book in lib:
        if number_to_delete == book['number']:
            lib.remove(book)
            break
    for book in lib:
        book['number'] = i
        i += 1
    return lib


def edit_(lib: list, command_list: list):
    '''
    Функция, редактирующая выбранный параметр книги
    :param lib: Библиотека кнги (список словарей)
    :param command_list: список команд со следующими индексами: 0-ой - номер книги,
    1-ый - параметр для редактирования, 2-ой - новое значение данного параметра
    :return: Библиотека книг (список словарей)
    '''
    lib[command_list[0]-1][command_list[1]] = command_list[2]
    return lib


def search_(lib: list, command: list):
    '''
    Функция, выполняющая поиск по параметру и значению
    :param lib: Библиотека кнги (список словарей)
    :param command: список команд со следующими индексами: 0-ой - параметр книги по которому осуществлять поиск,
    1-ый - искомое значение
    :return: Книгу с данным значением
    '''
    for book in lib:
        if book[command[0]] == command[1]:
            return book
    return 'Искомое значение не найдено'


def sort_(lib, command: list):
    '''
    Функция выполняющая сортировку по выбранному параметру книги с возможность выбора по возрастанию или по убыванию
    :param lib: Библиотека кнги (список словарей)
    :param command: список команд со следующими индексами: 0-ой - параметр книги по которому осуществлять сортировку,
    1-ый - по возрастанию/по убыванию
    :return:
    '''
    sort_lib = sorted(lib, key=lambda k: k[command[0]], reverse=command[1])
    for book in sort_lib:
        print(book)