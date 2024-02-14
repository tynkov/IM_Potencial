f = open('songs.csv', encoding='UTF-8')
lst = f.readlines()
f.close()
"""Чтение файла БД"""

d = {}
"""Создание хэш-таблицы"""
tracks = set()
"""Создание множества для проверки, 
    не встречался ли до этого данный трек"""
for s in lst[1:]:
    tmp = s.split(';')
    if tmp[2] not in tracks:
        tracks.add(tmp[2])
        if tmp[1] in d:
            d[tmp[1]] += 1
        else:
            d[tmp[1]] = 1
        """Добавление в хэш-таблицу песен исполнителя"""

artists = []
for k in d:
    artists.append((d[k], k))
top10 = sorted(artists, reverse=True)[:10]
"""Сортировка списка артистов по количеству треков"""
for name in top10:
    print(name[1], 'выпустил', name[0], 'песен.')