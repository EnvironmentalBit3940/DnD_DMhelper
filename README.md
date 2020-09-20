# Dungeon&Dragons DM helper

Тут когда-нибудь появится программа для создания и проведения игр по D&D

# База данных
Используется sqlite3, возможно перейду на Redis
На данный момент бд players содержит таблицы:
persons(
 - id, 
 - player_name, 
 - max_hits,
 - strength, 
 - dexterity, 
 - constitution,
 - intelligence,
 - wisdom,
 - charisma
 - inventory (Относится к items(id))
)

items(
 - id
 - title
 - cost
 - desc
)
 

## TODO:
 - Создание персонажей
 - Добавление приключений
 - Инвентарь, магазины
 - Учет подготовленных заклинаний мага


