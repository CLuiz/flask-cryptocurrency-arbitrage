import requests
from app import db
from models import Currency

# imports required for sqlite implementation found below
#import sqlite3



def get_data():
    r = requests.get('https://www.bitstamp.net/api/v2/ticker/btcusd/')
    return r.json()

# sqlite db add_data function
# def add_data(bitcoin_dict):
#     with sqlite3.connect('bitcoin.db') as connection:
#         c = connection.cursor()
#         values = ['bitstamp', bitcoin_dict['last']]
#         c.execute('INSERT INTO currency (exchange, price) VALUES(?, ?)', values)
#     return True

def add_data(bitcoin_dict):
    new_entry = Currency('bitstamp', bitcoin_dict['last'], None)
    db.session.add(new_entry)
    db.session.commit()
    return True

if __name__ =='__main__':
    data = get_data()
    add_data(data)
