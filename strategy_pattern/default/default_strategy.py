"""
Define a family of algorithms
Encapsulate each one
Make them interchangeable
"""

import abc


class Context:
    """
    Define the interface of interest to the client (context_interface)
    """

    def __init__(self, strategy):
        self._strategy = strategy

    def context_interface(self):
        self._strategy.algorithm_inteface()


class Strategy(metaclass=abc.ABCMeta):
    """
    Declare an interface common to all supported algorithms (algorithm_interface)
    Context uses this interface to call the algorithm defined by a ConcreteStrategy
    """
    @abc.abstractmethod
    def algorithm_interface(self):
        pass


class ConcreteStrategyA(Strategy):
    """
    Implement the algorithm using the Strategy interface
    """
    def algorithm_interface(self):
        pass


class ConcreteStrategyB(Strategy):
    """
    Implement the algorithm using the Strategy interface
    """
    def algorithm_interface(self):
        pass


class ConcreteStrategyC(Strategy):
    """
    Implement the algorithm using the Strategy interface
    """
    def algorithm_interface(self):
        pass


def main():
    """
    1. create an object of Strategy class of choice
    2. create an object of the interface class, passing in the strategy object
    Clients can then couple to an interface
    3. call the method in the interface class (interface_object.method)
    """
    concrete_strategy_b = ConcreteStrategyB()
    context = Context(concrete_strategy_b)
    soln = context.context_interface()


if __name__ == "__main__":
    main()
