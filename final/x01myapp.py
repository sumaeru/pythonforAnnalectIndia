from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json

#this whole code can be written in  class in factory format
#look in the project and adapt.. 

app = Flask(__name__)
app.config.from_pyfile('x00config.py')
db = SQLAlchemy(app)


from x02routes import *
#with app.app_context():
   # db.create_all()

if __name__ == '__main__':
    app.run()