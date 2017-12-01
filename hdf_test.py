# coding: utf8
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import numpy as np
import pandas as pd


df_1 = pd.DataFrame(np.array([[1, 2], [3, 4]]), columns=['a', 'b'])
df_2 = pd.DataFrame(np.array([[5, 6], [7, 8]]), columns=['c', 'd'])

# write
# store = pd.HDFStore('test.h5', mode='w', complevel=9, complib=b'blosc')
# store.put('one', df_1, format='table', append=True, data_columns=True, encoding='utf8')
# store.put('two', df_2, format='table', append=False, data_columns=True, encoding='utf8')
# store.close()

# read
# store = pd.HDFStore('test.h5', mode='r', complevel=9, complib=b'blosc')
# print(store)
# print(store.keys())
# print(store.get('one'))
# print(store.select('one', where=['a == 1', 'b == 2']))
# store.close()

# change
# store = pd.HDFStore('test.h5', mode='a', complevel=9, complib=b'blosc')
# print(store)
# store.remove('one', where=['a == 1', 'b == 2'])
# store.close()
