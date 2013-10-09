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

for iapp in INSTALL_APP:
    try:
        __import__(iapp+'.views')
    except:
        pass
