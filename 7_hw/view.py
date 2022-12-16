# выбор записи или поиска контакта

def contact_to_s():
    return input('Введите контакт:')

def choose_add_or_search():
    print('Выберите режим: 1 - добавление контакта, 2 - поиск контакта ')
    c = int(input('Введите 1 или 2: '))
    return c

def search(result):
    for i in result:
        print(i)