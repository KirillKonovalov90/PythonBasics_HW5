from pathlib import Path

file_path = Path('phonebook.txt')
format_book = '{:<15} {:<15} {:^11}'

def create_empty_book():
    with open(file_path, 'w', encoding = 'UTF-8') as file_data:
        line = 'Имя Фамилия Телефон'.split()
        file_data.write(f'{format_book.format(line[0], line[1], line[2])} \n')

def print_phonebook():
    with open(file_path, 'r', encoding = 'UTF-8') as book:
        rows = book.readlines()
        for row in rows:
            print(row.strip('\n'))

def find_contact():
    variant = int(input('Выберите вариант поиска:\n 1 - По имени и фамилии\n 2 - по номеру телефона\n'))
    match variant:
        case 1:
            name = input('Введите имя: ')
            surname = input('Введите фамилию: ')
            with open(file_path, 'r', encoding = 'UTF-8') as book:
                rows = book.readlines()
                for row in rows:
                    contact = row.split()
                    if (name in contact[0]) & (surname in contact[1]):
                        print('\n', row)
                        break
                else:
                    print('такого контакта не существует')
        case 2:
            telephone = input('Введите номер телефона: ')
            with open(file_path, 'r', encoding = 'UTF-8') as book:
                rows = book.readlines()
                for row in rows:
                    contact = row.split()
                    if (telephone in contact[2]):
                        print('\n', row)
                        break
                else:
                    print('такого контакта не существует')
        case _:
            print('Вы ввели неправильный параметр')

def add_contact():
    name = input('Введите имя: ')
    surname = input('Введите фамилию: ')
    telephone = input('Введите номер телефона: ')
    with open(file_path, 'a', encoding = 'UTF-8') as book:
        book.write(f'{format_book.format(name.strip(), surname.strip(), telephone.strip())} \n')
        print('Контак добавлен')
       
def delete_contact():
    variant = int(input('Выберите вариант поиска:\n 1 - По имени и фамилии\n 2 - по номеру телефона\n'))
    match variant:
        case 1:
            name = input('Введите имя: ')
            surname = input('Введите фамилию: ')
            with open(file_path, 'r', encoding = 'UTF-8') as book:
                rows = book.readlines()
            with open(file_path, 'w', encoding = 'UTF-8') as book:
                found = False
                for row in rows:
                    contact = row.split()
                    if (name in contact[0]) & (surname in contact[1]):
                        found = True
                        print()
                    else:
                        book.write(row)
                if found:
                    print('Контакт удалён')
                else:
                    print('Такого контакта не существует')
        case 2:
            telephone = input('Введите номер телефона: ')
            with open(file_path, 'r', encoding = 'UTF-8') as book:
                rows = book.readlines()
            with open(file_path, 'w', encoding = 'UTF-8') as book:
                found = False
                for row in rows:
                    contact = row.split()
                    if (telephone in contact[2]):
                        found = True
                        print()
                    else:
                        book.write(row)
                if found:
                    print('Контакт удалён')
                else:
                    print('Такого контакта не существует')      
        case _:
            print('Вы ввели неправильный параметр')
            
def contact_change():
    variant = int(input('Выберите вариант поиска:\n 1 - По имени и фамилии\n 2 - по номеру телефона\n'))
    match variant:
        case 1:
            name = input('Введите имя: ')
            surname = input('Введите фамилию: ')
            with open(file_path, 'r', encoding = 'UTF-8') as book:
                rows = book.readlines()
            with open(file_path, 'w', encoding = 'UTF-8') as book:
                found = False
                for row in rows:
                    contact = row.split()
                    if (name in contact[0]) & (surname in contact[1]):
                        name = input('Введите новое имя: ')
                        surname = input('Введите новую фамилию: ')
                        telephone = input('Введите новый номер телефона: ')
                        book.write(f'{format_book.format(name, surname, telephone)} \n')
                        found = True
                    else:
                        book.write(row)
                if found:
                    print('Контакт изменён')
                else:
                    print('Такого контакта не существует')
        case 2:
            telephone = input('Введите номер телефона: ')
            with open(file_path, 'r', encoding = 'UTF-8') as book:
                rows = book.readlines()
            with open(file_path, 'w', encoding = 'UTF-8') as book:
                found = False
                for row in rows:
                    contact = row.split()
                    if (telephone in contact[2]):
                        name = input('Введите новое имя: ')
                        surname = input('Введите новую фамилию: ')
                        telephone = input('Введите новый номер телефона: ')
                        book.write(f'{format_book.format(name, surname, telephone)} \n')
                        found = True
                    else:
                        book.write(row)
                if found:
                    print('Контакт изменён')
                else:
                    print('Такого контакта не существует')      
        case _:
            print('Вы ввели неправильный параметр')
              
inpt = int(input('Выберите пункт меню:\n \
1 - Создать чистую телефонную книгу\n 2 - Вся телефонная книга\n 3 - Поиск контакта\n \
4 - Добавление контакта\n 5 - Изменение контакта \n 6 - Удаление контакта \n 7 - Выход \n'))

match inpt:
    case 1:
        create_empty_book()
    case 2:
        print_phonebook()
    case 3:
        find_contact()
    case 4: #если другое
        add_contact()
    case 5:
        contact_change()
    case 6:
        delete_contact()
    case 7:
        print('До встречи!')
    case _:
        print('Вы ввели неверный параметр')