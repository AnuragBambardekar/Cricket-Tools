import sqlite3

conn = sqlite3.connect('DLS.db')

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS DLS_vals (
        overs_left REAL,
        wickets_lost INTEGER,
        resources_left REAL
    )
''')

data = [
    (50, 0, 100.0),
    (50, 1, 93.4),
    (50, 2, 85.1),
    (50, 3, 74.9),
    (50, 4, 62.7),
    (50, 5, 49.0),
    (50, 6, 34.9),
    (50, 7, 22.0),
    (50, 8, 11.9),
    (50, 9, 4.7),
]

cursor.executemany('INSERT INTO DLS_vals (overs_left, wickets_lost, resources_left) VALUES (?, ?, ?)', data)

conn.commit()
conn.close()
