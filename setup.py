# -*- coding: utf-8 -*-
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'Ronald Bai',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'ouyanghongyu@gmail.com',
    'version': '0.1',
    'install_requires': [],
    'packages': ['blogflask'],
    'scripts': [],
    'name': 'blogflask'
}

setup(**config)
