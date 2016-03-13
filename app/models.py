from hashlib import md5
import re
from app import db
from app import app

import sys
if sys.version_info >= (3, 0):
    enable_search = False


class Post(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
    author = db.Column(db.String(100))

    def __repr__(self):  # pragma: no cover
        return '<Post %r>' % (self.body)

