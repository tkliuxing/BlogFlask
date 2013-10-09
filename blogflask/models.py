# -*- coding: utf-8 -*-
import datetime
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import deferred, relationship
from blogflask import DbBase, session

"""
     ## ##   ### ##      ####  
    ##   ##   ##  ##      ##   
    ##   ##   ##  ##      ##   
    ##   ##   ## ##       ##   
    ##   ##   ##  ##  ##  ##   
    ##   ##   ##  ##  ##  ##   
     ## ##   ### ##    ## #    
                               
"""

class objects:

    def __init__(self, cls):
        self.cls = cls

    def filter(self, **kwargs):
        return session.query(self.cls).filter_by(**kwargs)

    def get(self, **kwargs):
        query = session.query(self.cls).filter_by(**kwargs)
        if query.count() != 1:
            raise Exception("count not only one!")
        return query.first()

    def all(self):
        return session.query(self.cls).all()

"""
    ##  ###   ## ##   ### ###  ### ##   
    ##   ##  ##   ##   ##  ##   ##  ##  
    ##   ##  ####      ##       ##  ##  
    ##   ##   #####    ## ##    ## ##   
    ##   ##      ###   ##       ## ##   
    ##   ##  ##   ##   ##  ##   ##  ##  
     ## ##    ## ##   ### ###  #### ##  
                                        
"""

class User(DbBase):
    __tablename__ = 'user'
    pk = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    fullname = Column(String, nullable=False)
    password = Column(String, nullable=False)
    blogs = relationship('Blog', backref='author')

    def __repr__(self):
        return "<User: %s>" % self.name or 'None'

    def save(self):
        session.add(self)
        session.commit()
        return self

User.objects = objects(User)

"""
    ### ##   ####      ## ##    ## ##   
     ##  ##   ##      ##   ##  ##   ##  
     ##  ##   ##      ##   ##  ##       
     ## ##    ##      ##   ##  ##  ###  
     ##  ##   ##      ##   ##  ##   ##  
     ##  ##   ##  ##  ##   ##  ##   ##  
    ### ##   ### ###   ## ##    ## ##   
                                        
"""

class Blog(DbBase):
    __tablename__ = 'blog'
    pk = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey('user.pk'), nullable=False)
    title = Column(String(100), nullable=False)
    content = deferred(Column(Text, nullable=False))
    create_time = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Blog: %d %s>" % (self.pk or None, self.title or 'None')

    def save(self):
        if not isinstance(self.create_time, datetime.datetime):
            self.create_time = datetime.datetime.now()
        session.add(self)
        session.commit()
        return self

Blog.objects = objects(Blog)
