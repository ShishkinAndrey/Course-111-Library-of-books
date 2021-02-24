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


def edit_(lib: list, command_dict: dict):
    '''
    Функция, редактирующая выбранный параметр книги
    :param lib: Библиотека книг (список словарей)
    :param command_dict: словарь команд со следующими ключами: number - номер книги,
    edit_param - параметр для редактирования, new_value - новое значение данного параметра
    :return: Библиотека книг (список словарей)
    '''
    lib[command_dict['number']-1][command_dict['edit_param']] = command_dict['new_value']
    return lib


def search_(lib: list, command: dict):
    '''
    Функция, выполняющая поиск по параметру и значению
    :param lib: Библиотека кнги (список словарей)
    :param command: словарь команд со следующими ключами: search_parameter - параметр книги по которому
    осуществлять поиск, search_value - искомое значение
    :return: Книгу с данным значением
    '''
    for book in lib:
        if book[command['search_parameter']] == command['search_value']:
            return book
    return 'Искомое значение не найдено'


def sort_(lib, command: dict):
    '''
    Функция выполняющая сортировку по выбранному параметру книги с возможность выбора по возрастанию или по убыванию
    :param lib: Библиотека кнги (список словарей)
    :param command: словарь команд со следующими ключами:
    sort_parameter - параметр книги по которому осуществлять сортировку,
    choose_reverse - по возрастанию/по убыванию
    :return:
    '''
    sort_lib = sorted(lib, key=lambda k: k[command['sort_parameter']], reverse=command['choose_reverse'])
    for book in sort_lib:
        print(book)