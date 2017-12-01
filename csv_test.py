# coding: utf8
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import csv

list_ = [
    {'x': 1, 'b': 2},
    {'a': 3, 'b': 4},
    {'a': 5, 'b': 6},
]

with open('C:\\test.csv', b'wb') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=['b'], extrasaction='ignore')
    csv_writer.writeheader()
    for elem in list_:
        csv_writer.writerow(elem)
