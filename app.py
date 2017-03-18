import os
#import sqlite3
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

BASE = os.path.abspath(os.path.dirname(__file__))
DATABASE_PATH = os.path.join(BASE, 'test.db')
DATABSE_URI = os.getenv('DATABASE_URL', 'sqlite:///' + DATABASE_PATH)

app = Flask(__name__)
#local solution
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + DATABASE_PATH
#updated for heroku deployment
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
db = SQLAlchemy(app)

import models

@app.route('/')
def index():
    return 'Hello World!'


# add data from the db
@app.route('/data')
def get_data():
    data_lst = []
    # with sqlite3.connect('bitcoin.db') as connection:
    #     c =  connection.cursor()
    #     c.execute('SELECT * FROM currency')
    #     data = c.fetchall()
    #     for value in data:
    #         data_lst.append({
    #         'exchange': value[0],
    #         'price': value[1],
    #         'time': value[1]
    #         })
    query = models.Currency.query.all()
    for row in query:
        obj = {
            'exchange': row.exchange,
            'price': row.price,
            'time': row.hora
        }
        data_lst.append(obj)
    return jsonify(data_lst)


port = int(os.environ.get('PORT', 8080)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
