# -*- coding: utf-8 -*-
import markdown2
import hashlib


def markdown(text):
    return markdown2.markdown(text)


def gravatar(text):
    mail = text.strip().lower()
    hash_md5 = hashlib.md5(mail).hexdigest()
    return "http://www.gravatar.com/avatar/%s" % hash_md5
