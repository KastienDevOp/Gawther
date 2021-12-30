import sqlite3 as sql 

def create_db():
    with sql.connect('main.db') as mdb:
        cur = mdb.cursor()
        
        cur.execute('''CREATE TABLE IF NOT EXISTS members(
            guildId INTEGER,
            memberID INTEGER,
            warnings INTEGER,
            mutes INTEGER,
            kicks INTEGER,
            bans INTEGER,
            balance REAL,
            status TEXT,
            subStatus TEXT
        )''')
        
        cur.execute('''(
            x
        )''')
        
        cur.execute('''(
            x
        )''')
        
        cur.execute('''(
            x
        )''')
        
        cur.execute('''(
            x
        )''')
        
        cur.execute('''(
            x
        )''')
        
        cur.execute('''(
            x
        )''')