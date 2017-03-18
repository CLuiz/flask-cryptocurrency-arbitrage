from app import db
from models import Currency

# create db & db table
db.create_all()

# commit changes
db.session.commit()
