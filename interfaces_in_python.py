# Interfaces in Python using Abstract Based Class
# FYI: 1. An abstract method is a method that is declared, but contains no implementation.
#          2. Abstract classes may not be instantiated, and require subclasses to provide
#            implementations for the abstract methods.
#          3. Properties are generally used to provide access methods to change an attribute
#            of a class. By adding a @property decorator, a method can be accessed like a variable

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
