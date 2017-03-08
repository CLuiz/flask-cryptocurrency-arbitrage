from flask import Flask
from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.resources import INLINE
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

# add data from the db
def get_data():
    with sqlite3.connect('currency.db') as connection:
        c =  connection.cursor()
        c.execute('SELECT * FROM currency')
        data = c.fetchall()
    return data

if __name__ == '__main__':
    app.run(debug=True)
