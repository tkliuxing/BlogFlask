import os
from flask import Flask
from flask.ext.mako import MakoTemplates
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

PROJECTROOT = os.path.dirname(os.path.abspath(__file__))

DbBase = declarative_base()
DbEngine = create_engine('sqlite:///'+PROJECTROOT+'/../blogflask.db', echo=False)
DbSession = sessionmaker(bind=DbEngine)
session = DbSession()
app = Flask('blogflask')
mako = MakoTemplates(app)
#DEBUG=True
INSTALL_APP = (
    'blogflask',
)

SECRET_KEY = '6s#q6tf38%)ku*ib5-ga^@5fhd0&*hw%&amp;o8t4pq5-7tzr$t)xk'

for iapp in INSTALL_APP:
    try:
        __import__(iapp+'.views')
    except:
        pass
