#!/usr/bin/env python
# -*- coding: utf-8 -*-
from blogflask import INSTALL_APP, DbEngine, DbBase, session
# import blogflask
# import optparse
# import sys

for iapp in INSTALL_APP:
    try:
        __import__(iapp+'.models')
    except:
        pass

session.bind.echo = True
DbBase.metadata.create_all(DbEngine)
session.bind.echo = False