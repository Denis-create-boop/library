
# класс для работы с библиотекой, осуществляет добавление, просмотр, поиск и удаление книг
text_none = 'Такой книги нет в библиотеке'

class Book:
    # инициализатор
    def __init__(self, id, title, author, year, status):
        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    # функция для показа всех книг в библиотеке
    def get_book(self):
        # проходимся по словорю и выводим все книги которые имеються в библиотеке
        for k, v in books.items():
            for key, value in v.items():
                print(f'{key}: {value}')
            print()

    # функция для добавления книги в библиотеку
    def set_book(self, book):
        books[book.id] = {'id': book.id, 'описание': book.title,'автор': book.author, 'год издания': book.year, 'статус': book.status}

    # функция для поиска книги по автору, названию, или году
    def find_book(self, finder):
        # проверяем написани ли дата
        if type(finder) is int or finder.isdigit():
            # переводим дату в число
            finder = int(finder)
            # флаг для проверки наличии искомой книги в библиотеке
            a = 0
            # проходимся по библиотеке
            for k, v in books.items():
                # проверяем имееться ли искомый год в библиотеке если да то выводим книгу
                if v['год издания'] == finder:
                    print(f'id: {v['id']}',  f'описание: {v['описание']}',  f'автор: {v['автор']}',  f'год издания: {v['год издания']}',
                          f'статус: {v['статус']}', sep='\n')
                    print()
                    a += 1
                
            if a == 0:
                print(text_none)
        # иначе если написана не дата а автор или название книги
        else:
            # проверяем имеються ли в библиотеке книги
            if books:
                # проходимся по библиотеке
                a = 0
                for k, v in books.items():
                    # проверяем соответсвует ли стово поиска автору или описанию если да то выводим
                    if v['описание'].lower() == finder or v['автор'].lower() == finder:
                        print(f'id: {v['id']}',  f'описание: {v['описание']}',  f'автор: {v['автор']}',  f'год издания: {v['год издания']}',
                              f'статус: {v['статус']}', sep='\n')
                        a += 1
                    
                if a == 0:
                    print(text_none)
            else:
                print(text_none)

    # изменение статуса книги
    def set_status_book(self, id, status):
        books[id]['статус'] = status
        print(f'Статус книги под номером {id} успешно изменен на "{status}"')


    # удаление книги по id

    def del_book(self, id):
        # проверяем являеться ли введенный id числом
        if  id in books.keys():
            book = books[id]
            print(f'Книга под номером {id}', f'автор: {book['автор']}', f'описание: {book['описание']}', f'год издания: {book['год издания']}',
                  f'успешно удалена', sep='\n')
            del books[id]
        else:
            print(f'Книги под номером {id} нет в библиотеке')


books = dict()


