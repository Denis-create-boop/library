# файл со всеми функциями
from book import *



text_empty = 'Библиотека пока пуста'
text_add = 'Книга успешно добавлена'
text_id = 'Введен некорректный id пожалуйста введите число id книги'


# функция для добавления книг в библиотеку
def add_book(id, book, num):
    global text_add
    while True:
        print('Введите название книги')
        title = input() # вводим название книги
        print('Введите автора')
        author = input() # вводим автора книги
        flag = True
        for k, v in books.items():
            # если книга есть то меняем значение флага и прерываем цикл
            if title.capitalize() == v['описание'].capitalize() and author.capitalize() == v['автор'].capitalize():
                print(f'Книга: {title}, автор: {author}, уже имеется в библиотеке')
                print()
                flag = False
                break
        if flag:
            print('Введите год издания')

            while True:
                year = input() # вводим год выпуска книги
                try:
                    year = int(year) # проверяем что введена дата
                    break
                except:
                    print()
                    print('Введена некорректная дата, пожалуйста введите дату в виде числа')                
            status = 'в наличии'
            break

    # проверяем что в библиотеке есть книги
    if books:
        if len(author.split()) > 1:
            au = author.split()
            author = au[0].capitalize() + ' ' + au[1].capitalize()
        else:
            author = author.capitalize()
        book = Book(id, title.capitalize(), author, year, status.capitalize())
        book.set_book(book)
        print(text_add)
        num -= 1
        id += 1    
        print()
        
    # если библиотека пуста то просто добовляем книгу
    else:
        if len(author.split()) > 1:
            au = author.split()
            author = au[0].capitalize() + ' ' + au[1].capitalize()
        else:
            author = author.capitalize()
        book = Book(id, title.capitalize(), author, year, status.capitalize())
        book.set_book(book)
        print(text_add)
        id += 1
        num -= 1
        print()
    
    # сохраняем изменения
    with open('library.txt', 'r+') as f:
        f.truncate
    for k in books:
        with open('library.txt', 'a') as f:
            f.write(str(books[k]) + '\n')
    
    return [num, id]


# функция для удаления книги из библиотеки
def del_book(id, book):
    global text_empty, text_id
    # проверяем что библиотека не пуста
    if books:
        # просим id книги
        print('Введите номер(id) книги которую хотите удалить')
        while True:
            delete_id = input()
            try:
                delete_id = int(delete_id) # проверяем что введено число
                break
                
            except:
                print(text_id)
        # запускаем функцию удаления        
        book.del_book(delete_id)
        print()           
        
    else:
        print(text_empty)
        print()
    # сохраняем изменения
    with open('library.txt', 'r+') as f:
        f.truncate()
    for k in books:
        with open('library.txt', 'a') as f:
            f.write(str(books[k]) + '\n')


# функция для поиска книги
def find_book(book):
    global text_empty
    # проверяем что библиотека не пуста просим данные и запускаем функцию поиска
    if books:
        print('Введите автора, название или год издания книги')
        finder = input()
        book.find_book(finder.lower())
        print()
    else:
        print(text_empty)
        print()


# функция для изменения статуса книги
def change_status(book):
    global text_empty, text_id
    # проверяем что библиотека не пуста
    if books:
        # просим id книги и запускаем функцию изменения статуса
        print('Введите номер (id) книги')
        while True:
            try:
                ID = int(input()) # проверяем что введено число
                break       
            except:
                print(text_id)
        # запускаем цикл для того что бы контролировать правильность введенного статуса
        while True:
            # проверяем что id присутствует в библиотеке
            if ID in books:      
                print('Введите новый статус')
                new_status = input() # просим ввести статус
                # проверяем если статус корректный то изменяем его
                if new_status.lower() == 'выдана' or new_status.lower() == 'в наличии':
                    book.set_status_book(ID, new_status.lower())
                    print()
                    break
                else:
                    print('Введен некорректный статус')
                    print()
            else:
                print(f'Книги под номером {ID} нет в библиотеке')
                print()
                break
        
    else:
        print(text_empty)
        print() 
    # сохроняем изменения   
    with open('library.txt', 'r+') as f:
        f.truncate()
    for k in books:
        with open('library.txt', 'a') as f:
            f.write(str(books[k]) + '\n')      


# функция для вывода всех книг которые есть в библиотеке
def show_books(book):
    global text_empty
    # проверяем что библиотека не пуста и запускаем функцию для показа всех книг
    if books:
        book.get_book()
    else:
        print(text_empty)
        print()


# функция для выхода из программы
def close_library():
    # записываем все изменения
    with open('library.txt', 'r+') as f:
        f.truncate()
    for k in books:
        with open('library.txt', 'a') as f:
            f.write(str(books[k]) + '\n')
    print('Всего доброго')

        