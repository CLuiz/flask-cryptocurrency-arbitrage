import sqlite3

def drop_table():
    with sqlite3.connect(db) as connection:
        c = connection.cursor()
        c.execute()'DROP TABLE if EXISTS currency;')
    return True

def create_db():
    with sqlite3.connect('bitcoin.db') as connection:
        c = connection.cursor()
        c.execute("""CREATE TABLE currency (
                    currency text,
                    price Real,
                    Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                );""")
    return True

if __name__ == '__main__':
    drop_table()
    create_db()
