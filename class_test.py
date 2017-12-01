# coding: utf8
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals


class Foo(object):
    X = 1.0
    Y = 2.0

    @staticmethod
    def averag(*mixes):
        return sum(mixes) / len(mixes)

    @staticmethod
    def static_method():
        return Foo.averag(Foo.X, Foo.Y)

    @classmethod
    def class_method(cls):
        return cls.averag(cls.X, cls.Y)


class Son(Foo):
    X = 3.0
    Y = 5.0

    @staticmethod
    def averag(*mixes):
        return sum(mixes) / 3.0


p = Son()
print(p.static_method())
print(p.class_method())
