import sqlite3


class takeFromDB:
    def __init__(self):
        self.con = sqlite3.connect("players")
        self.cur = self.con.cursor()
        self.cur.execute('''CREATE TABLE IF NOT EXIST 'persons' (
            'id' INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            'player_name' STRING,
            'max_hits' INTEGER,
            'race' STRING,
            'strength' INTEGER,
            'dexterity' INTEGER,
            'constitution' INTEGER,
            'intelligence' INTEGER,
            'wisdom' INTEGER,
            'charisma' INTEGER,
            'inventory' INTEGER,
            'exp' INTEGET,
            FOREIGN KEY (inventory) REFERENCES items(id)
            )''')
        self.cur.execute('''CREATE TABLE IF NOT EXIST 'items' (
            'id' INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            'title' INTEGER NOT NULL,
            'cost' INTEGER NOT NULL,
            'desc' STRING
            ) ''')
