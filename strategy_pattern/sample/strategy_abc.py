from abc import ABCMeta, abstractmethod


class AbsStrategy(metaclass=ABCMeta):
    """
    Declare an interface common to all supported algorithms.
    """
    @abstractmethod
    def calculate(self, order):
        """Calculate shipping cost"""
