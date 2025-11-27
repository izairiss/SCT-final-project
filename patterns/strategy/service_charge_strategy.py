__author__ = "Phoenixx Izairiss Ordonez"
__version__ = "1.0.0"

from abc import ABC, abstractmethod
from bank_account.bank_account import BankAccount

class ServiceChargeStrategy(ABC):
    """
    The ServiceChargeStrategy abstract class defines a common interface 
    for all concrete strategies to be applied to the bank_account classes.
    """
    BASE_SERVICE_CHARGE = 0.50

    @abstractmethod
    def calculate_service_charges(self, account: BankAccount) -> float:
        """
        Abstract calculate_service_charges method to be implemented in subclasses.

        Args: 
            account (BankAccount): The user's bank account data.

        Returns:
            float: The calculated service charge  
        """
        pass
