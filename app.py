import os
#import sqlite3
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

BASE = os.path.abspath(os.path.dirname(__file__))
DATABASE_PATH = os.path.join(BASE, 'test.db')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + DATABASE_PATH
db = SQLAlchemy(app)

import models

@app.route('/')
def index():
    return 'Hello World!'

#port = int(os.environ.get('PORT', 5000)

# add data from the db
@app.route('/data')
def get_data():
    data_lst = []
    with sqlite3.connect('bitcoin.db') as connection:
        c =  connection.cursor()
        c.execute('SELECT * FROM currency')
        data = c.fetchall()
        for value in data:
            data_lst.append({
            'exchange': value[0],
            'price': value[1],
            'time': value[1]
            })
        return jsonify(data_lst)

if __name__ == '__main__':
    app.run(port=8080)
