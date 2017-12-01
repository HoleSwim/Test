# coding: utf8
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import numpy as np
import pandas as pd

# df = pd.DataFrame(np.array([[1, 2], [3, 4]]), columns=['a', 'b'])
# store = pd.HDFStore('test.h5', mode='w')
# store['foo'] = df
# store.close()

store = pd.HDFStore('test.h5', mode='r')
store.open(mode='w')
store.close()
