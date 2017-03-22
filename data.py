import requests
from app import db
from models import Currency

# imports required for sqlite implementation found below
#import sqlite3


def get_data():
    results = {}
    r = requests.get('https://www.bitstamp.net/api/v2/ticker/btcusd/')
    return r.json()

# sqlite db add_data function
# def add_data(bitcoin_dict):
#     with sqlite3.connect('bitcoin.db') as connection:
#         c = connection.cursor()
#         values = ['bitstamp', bitcoin_dict['last']]
#         c.execute('INSERT INTO currency (exchange, price) VALUES(?, ?)', values)
#     return True

def get_rates():
    results = {}
    try:
        bitstamp = requests.get(
            'https://www.bitstamp.net/api/v2/ticker/btcusd/')
        results['bitstamp'] = float(bitstamp.json()['bid'])
        kraken = requests.get(
            'https://api.kraken.com/0/public/Ticker?pair=XBTUSD')
        results['kraken'] = float(kraken.json()['result']['XXBTZUSD']['a'][0])
        bittrex = requests.get(
            'https://bittrex.com/api/v1.1/public/getticker?market=usdt-btc')
        results['bittrex'] = bittrex.json()['result']['Bid']
        return results
    except:
        return False

def add_data(bitcoin_dict):
    for key, value in bitcoint_dict.items():
        new_entry = Currency(key, value, None)
        db.session.add(new_entry)
        db.session.commit()
    return True

if __name__ == '__main__':
    data = get_data()
    add_data(data)
