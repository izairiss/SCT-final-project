__author__ = "Phoenixx Izairiss Ordonez"
__version__ = "1.0.0"

from patterns.observer.observer import Observer
from abc import ABC, abstractmethod


class Subject(ABC):
    """
    The Subject abstract class is responsible for maintaining a list 
    of its observers and notifying them of state changes or events.
    """
    def __init__(self):
        """
        Initializes the class attribute to an empty list.
        """
        self._observers = []

    @abstractmethod
    def attach(self, observer: Observer):
        """
        Abstract attach method to be implemented in the concrete class.
        """
        pass

    @abstractmethod
    def detach(self, observer: Observer):
        """
        Abstract detach method to be implemented in the concrete class.
        """
        pass

    @abstractmethod
    def notify(self, message: str):
        """
        Abstract notify method to be implemented in the concrete class.
        """
        pass




