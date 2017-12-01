# coding: utf8
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import pandas as pd

df = pd.DataFrame([[1, 2], [2, 4]], columns=['c1', 'c2'], index=['r1', 'r2'])

print(df)

print('-' * 100)

# c1列中值为2的所有行的数据
print(df.loc[df.loc[:, 'c1'] == 2])


print('-' * 100)

# r1行中值为2的所有列的数据
print(df.loc[:, df.loc['r1'] == 2])
