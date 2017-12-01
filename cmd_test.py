# coding: utf8
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import os

path = r'D:\Python\MongoDB\bin'
cmd_path = "d: && cd " + path
cmd_dump = 'mongodump ...'
os.system(cmd_path + " && " + cmd_dump)
