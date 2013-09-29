from flask import Flask

app = Flask('blogflask')

#DEBUG=True
INSTALL_APP = (
    'blogflask',
)

for iapp in INSTALL_APP:
    __import__(iapp+'.views')
