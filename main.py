import sqlite3

SQLMDL = '''
    CREATE TABLE IF NOT EXITS apuestas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    apuesta TEXT NOT NULL
    )
'''

con = sqlite3.connect('apuesta.db', isolation_level=None)

con.execute(SQLMDL)




con.close()