import sqlite3
import requests


def get_data():
    r = requests.get('https://www.bitstamp.net/api/v2/ticker/btcusd/')
    return r.json()


def add_data(bitcoin_dict):
    with sqlite3.connect('bitcoin.db') as connection:
        c = connection.cursor()
        values = ['bitstamp', bitcoin_dict['last']]
        c.execute('INSERT INTO currency (exchange, price) VALUES(?, ?)', values)
    return True


if __name__ =='__main__':
    data = get_data()
    add_data(data)
