f = open('songs.csv', encoding='UTF-8')
lst = f.readlines()
f.close()
"""Чтение файла БД"""

mnRus = set()
mnFor = set()
"""Создание множеств с именами артистов"""

for s in lst[1:]:
    tmp = s.split(';')
    flag = False
    for char in tmp[1]:
        if 1040 <= ord(char) <= 1103:
            """Проверка, является ли исполнитель русскоязычным"""
            flag = True
    if flag:
        mnRus.add(tmp[1])
    else:
        mnFor.add(tmp[1])
    """Добавление имён исполнителей в множества"""

print('Количество российских исполнителей:', len(mnRus))
print('Количество иностранных исполнителей:', len(mnFor))
"""Вывод ответа на задачу"""
russian = open('russian_artists.txt', 'w', encoding='UTF-8')
foreign = open('foreign_artists.txt', 'w', encoding='UTF-8')
"""Открытие файлов с именами исполнителей"""
for name in mnRus:
    russian.write(name + '\n')
for name in mnFor:
    foreign.write(name + '\n')
"""Запись имён исполнителей в файлы"""
russian.close()
foreign.close()
