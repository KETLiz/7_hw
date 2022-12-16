def write(name, number):
    with open('7_hw/file.txt', 'a', encoding='utf-8') as data:
        data.write(f'Имя: {name}, номер: {number}\n')
    
    with open('7_hw/file.csv', 'a', encoding='utf-8') as data:
        data.write(f'Имя: {name}\nНомер: {number}\n')
        
def get_base():
    with open('7_hw/file.txt', 'r', encoding='utf-8') as data:
        return data.readlines()