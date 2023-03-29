import os

DEBUG = True
SECRET_KEY = 'Thisisasecret!'#session
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///'+ os.path.join(basedir,'freak.db')
#add additonal profile information.. if need is there.. 


