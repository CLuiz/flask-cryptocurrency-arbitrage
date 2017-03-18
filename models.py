from datetime import datetime

from app import db

class Currency(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    exchange = db.Column(db.String())
    price = db.Column(db.String())
    hora = db.Column(db.DateTime())

    def __init__(self, exchange, price, hora):
        self.exchange = exchange
        self.price = price
        if hora is None:
            hora = datetime.utcnow()
        self.hora = hora

    def __repr__(self):
        return '<Currency {}>'.format(self.exchange)
