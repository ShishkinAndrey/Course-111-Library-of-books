from Library import add_, get_library_from_json, library_to_json, delete_, edit_, search_


def _input():
    list_par = ['add', 'delete', 'edit', 'search', 'review']
    input_command = input('Введите команду add-delete-edit-search-review \n')
    while not input_command.isalpha() or input_command not in list_par:
        input_command = input('Error! Введите одну из команд add-delete-edit-search-review \n')
    return input_command.lower()


def command_review(lib):
    for book in lib:
        print(book)


def command_add(lib):
    new_book = {}
    new_book['number'] = len(lib)+1
    new_book['name'] = input('Введите имя книги')
    new_book['year'] = int(input('Введите год выпуска книги'))
    new_book['pages'] = int(input('Введите кол-во страниц книги'))
    new_book['rating'] = float(input('Введите рейтинг книги'))
    new_book['price'] = float(input('Введите цену книги'))
    new_book['author'] = input('Введите автора книги')
    return new_book


def command_delete():
    number_deleted_book = int(input('Введите номер книги, чтобы удалить'))
    return number_deleted_book


def command_edit(lib):
    command_list = []
    number = int(input(f'Введите номер книги, которую хотите отредактировать от 1 до {len(lib)} '))
    command_list.append(number)
    list_edit_par = [i for i in lib[0].keys() if i != 'number']
    edit_param = input(f'Выберите из списка параметр, который хотите отредактировать {list_edit_par} ')
    while edit_param not in list_edit_par:
        edit_param = input(f'Выберите из списка параметр, который хотите отредактировать {list_edit_par} ')
    command_list.append(edit_param)
    if edit_param == 'year' or edit_param == 'pages':
        new_value = int(input('Введите новые данные для данного параметра'))
    elif edit_param == 'rating' or edit_param == 'price':
        new_value = float(input('Введите новые данные для данного параметра'))
    else:
        new_value = input('Введите новые данные для данного параметра')
    command_list.append(new_value)
    return command_list


def command_search(lib):
    command_list = []
    list_search_par = [i for i in lib[0].keys()]
    search_parameter = input(f'Введите из списка параметр, который хотите найти {list_search_par} ')
    if search_parameter == 'name' or search_parameter == 'author':
        search_value = input(f'Введите значение {search_parameter}, который хотите найти ')
    elif search_parameter == 'rating' or search_parameter == 'price':
        search_value = float(input(f'Введите значение {search_parameter}, который хотите найти '))
    else:
        search_value = int(input(f'Введите значение {search_parameter}, который хотите найти '))
    command_list.append(search_parameter)
    command_list.append(search_value)
    return command_list


def main_func():
    lib = get_library_from_json()
    while True:
        input_command = _input()
        if input_command == 'add':
            library_to_json(add_(lib, command_add(lib)))
        elif input_command == 'delete':
            library_to_json(delete_(lib, command_delete()))
        elif input_command == 'review':
            command_review(lib)
        elif input_command == 'edit':
            library_to_json(edit_(lib, command_edit(lib)))
        elif input_command == 'search':
            print(search_(lib, command_search(lib)))


if __name__ == '__main__':
    main_func()
