__author__ = "Phoenixx Izairiss Ordonez"
__version__ = "1.0.0"

from abc import ABC, abstractmethod

class Observer(ABC):
    """
    The Observer superclass will be used to define the interface for all 
    concrete observers that need to be notified of changes in the subject.
    """
    @abstractmethod
    def update(self, message: str):
        """
        Abstract update method to be implemented in subclasses to notify
        observers when there are changes in the subject.

        Args:
            message (str): The message sent to notify about the changes.
        """
        pass