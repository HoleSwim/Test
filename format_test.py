# coding: utf8
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

var_list = ['Tom', 5000]
var_dict = {'name': 'Tom', 'money': 5000}
print('name: {}, money: {}'.format(*var_list))
print('name: {0}, money: {1}'.format(*var_list))
print('name: {1}, money: {0}'.format(5000, 'Tom'))
print('name: {name}, money: {money}'.format(**var_dict))
print('name: {name}, money: {money}'.format(money=5000, name='Tom'))
print('-----------------------------------------')
print('{:X>4}'.format('10'))
print('{0:X<4}'.format(10))
print('{1:X^4}'.format(10, 20))
print('-----------------------------------------')
print('name: {0}, money: {1:.2f}'.format(*var_list))
print('name: {name}, money: {money:,}'.format(**var_dict))
print('{{{}}}'.format('test'))
