# coding: utf8
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from cStringIO import StringIO

s = StringIO()
s.write('aaa\n')
s.write('bbb')
s.seek(4)
print(s.read(), end='\n\n')

s.seek(4)
s.seek(-2, 1)
print(s.read(), end='\n\n')

s.seek(-1, 2)
print(s.read(), end='\n\n')

s.seek(2)
s.write('cd')
s.truncate(5)
print(s.getvalue())
