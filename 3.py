f = open('songs.csv', encoding='UTF-8')
lst = []
for s in f:
    lst.append(s.split(';'))
f.close()
"""Чтение файла БД"""
name = input('Здравствуйте, пожалуйста введите имя артиста: ')
"""Ввод пользовательской команды"""
while name != '0':
    flag = True
    for s in lst:
        if s[1] == name:
            print('У', name, 'найдена песня:', s[2])
            flag = False
            break
    """Поиск имени исполнителя среди всех записей"""
    if flag:
        print('К сожалению, ничего не удалось найти.')
    name = input('Пожалуйста введите имя артиста: ')
    """Повторный ввод пользовательской команды"""
