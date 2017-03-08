import sqlite3
import requests

def get_data():
    r = requests.get('https://www.bitstamp.net/api/v2/ticker/btcusd/')
    return r.json()

def add_data(blah):
    print(blah)
    with sqlite3.connect('bitcoin.db') as connection:
        c = connection.cursor()
        values = ['bitstamp', blah['last']]
        c.execute('INSERT INTO currency (exchange, price) VALUES(?, ?)', values)
    return True

if __name__ =='__main__':
    data = get_data()
    add_data(data)

"""
exchange: bitstamp
price: 1256.23434
hora: 2017/03/07 19:08:06
"""
