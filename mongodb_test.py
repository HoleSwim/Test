# coding: utf8
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import pymongo

client = pymongo.MongoClient('localhost', 27017)
db = client['admin']
db.authenticate("admin", "admin")
collection = db['collection']

# 唯一索引
collection.ensure_index([('number', pymongo.ASCENDING), ('name', pymongo.ASCENDING)])
