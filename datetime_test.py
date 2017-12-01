# coding: utf8
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import datetime

dt = datetime.datetime.now()
print('now time: {}'.format(dt))
print('now week: {}'.format(dt.isoweekday()))
dt = dt.replace(year=1998)
dt += datetime.timedelta(days=1)
print('change time: {}'.format(dt))
