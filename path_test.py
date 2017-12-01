# coding: utf8
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import os

print('1', os.path.basename(__file__))
print('2', os.path.dirname(__file__))

print('3', os.path.abspath('..'))
print('4', os.path.join(os.path.dirname(__file__), '..'))
