from flask import Flask
from flask.ext.mako import MakoTemplates

app = Flask('blogflask')
mako = MakoTemplates(app)
#DEBUG=True
INSTALL_APP = (
    'blogflask',
)

for iapp in INSTALL_APP:
    __import__(iapp+'.views')
