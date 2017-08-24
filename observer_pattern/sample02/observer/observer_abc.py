import abc


class AbsObserver(metaclass=abc.ABCMeta):

    def __init__(self):
        self._subject = None
        self._observer_state = None

    @abc.abstractmethod
    def _update(self, arg):
        pass
