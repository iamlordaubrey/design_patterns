# Using interfaces in Python using Abstract Based Class

import abc


class MyABC(metaclass=abc.ABCMeta):
    # __metaclass__ = abc.ABCMeta (python 2)

    @abc.abstractmethod
    def do_something(self, value):
        """Required method"""

    @abc.abstractproperty
    def some_property(self):
        """Required property"""


class MyClass(MyABC):
    """Implementation of MyABC"""

    def __init__(self, value=None):
        self._myprop = value

    def do_something(self, value):
        """Implementation of abstract method"""
        self._myprop *= 2 + value

    @property
    def some_property(self):
        """Implementation of abstract property"""
        return self._myprop


class BadClass(MyABC):
    pass


a = MyClass(value=42)
print(a.some_property)
a.do_something(3)
print(a.some_property)

b = BadClass()

# Summary:
# Abstract Based Classes gives us a way to define interfaces and implement them separately
# It also provides important checks on our Implementation to ensure that they are complete
