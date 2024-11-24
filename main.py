# основной файл программы
from book import *
from funks import *
id = 0
book = Book(0, '', '', '', '')


# функция приветствия
def hello():
    # выводим приветствие и команды
    print('Приветствуем вас в нашей библиотеке.', 'чтобы добавить книгу введите слово "добавить"',  'чтобы удалить книгу введите слово "удалить"',
          'чтобы найти книгу введите слово "найти"', 'чтобы посмотреть все имеющиеся книги введите "посмотреть"',
          'чтобы изменить статус книги введите "изменить"', 'для завершения программы введите "выход"', 'для продолжения нажмите Enter', sep='\n')
    input()
    main()

# вункция проверки базы данных
def check_library():
    global id, book
    with open('library.txt', 'r') as f:
        for line in f.readlines():
            a = line.split(',')
            if len(a) > 1:
                id = int(a[0][7:])
                title = a[1][14:-1]
                author =  a[2][11:-1]
                year = int(a[3][16:])
                status = a[4][12:-3]
                book = Book(id, title, author, year, status)
                book.set_book(book)
                
        id += 1
    hello()

# основная функция для работы с командами
def main():
    # функция для обработки запросов
    global id, book
    
    while True:
        # просим ввести запрос и обрабатываем его
        print('Введите ваш запрос')
        request = input()
        print()
        # если клиент хочет тобавить книгу то инициализируем класс Book и добовляем книгу
        if request.lower() == 'добавить':
            print('Сколько книг вы хотите добавить?')
            while True:
                num = input()
                try:
                    num = int(num)
                    break
                except:
                    print('Введите число')
            while num:
                num, id = add_book(id, book, num)

           
        # если пользователь хочет удалить книгу
        elif request.lower() == 'удалить':
            # проверяем что библиотека не пуста
            del_book(id, book)

        # если пользователь хочет найти книгу
        elif request.lower() == 'найти':
            find_book(book)
        
        # если пользователь хочет изменить статус
        elif request.lower() == 'изменить':
            change_status(book)
        
        # если пользователь хочет посмотреть все книги в библиотеке
        elif request.lower() == 'посмотреть':
            show_books(book)

        # если пользователь хочет завершить программу то выходим
        elif request.lower() == 'выход':
            close_library()
            break
            
        else:
            print('Введен некорректный запрос')
            print()


if __name__ == '__main__':
    check_library()

