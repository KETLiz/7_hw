# модель для добавления нового контакта

def add_contact():
    name = input('Введите имя: ')
    number = int(input('Введите номер телефона: '))
    data = tuple([name, number])
    return data


        
def search_contact(base, name):
    #base = base.split('\n')
    flag = True
    results = []
    for i in base:
        if name in i:
            flag = False
            results.append(i)
    return results