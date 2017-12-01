# coding: utf8
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import re


content = 'name: Tom\tage: 20\nname: Tim\tage: 25\n'
print(content)
pattern = re.compile('name: (.*?)\sage: (.*?)\s', re.S)
items = pattern.findall(content)
print(items)
