__author__ = "Phoenixx Izairiss Ordonez"
__version__ = "1.0.0"


from patterns.strategy.service_charge_strategy import ServiceChargeStrategy
from bank_account.bank_account import BankAccount

class MinimumBalanceStrategy(ServiceChargeStrategy):
    """
    The MinimumBalanceStrategy strategy is a subclass of the 
    ServiceChargeStrategy superclass.
    """
    SERVICE_CHARGE_PREMIUM = 2.0

    def __init__(self, minimum_balance: float):
        """
        Initializes the class attributes with argument values.

        Args:
            minimum_balance (float): The minimum value a balance can be before
                                    further service charges are applied.
        """
        self.__minimum_balance = minimum_balance
        

    def calculate_service_charges(self, account: BankAccount) -> float:
        """
        Calculates service charge.

        Args: 
            account (BankAccount): The user's bank account data.

        Returns:
            float: The calculated service charge based on the 
                    account balance and minimum balance.
        """
        if account.balance >= self.__minimum_balance:
            service_charge = self.BASE_SERVICE_CHARGE
        else: 
            service_charge = (self.BASE_SERVICE_CHARGE * 
                                self.SERVICE_CHARGE_PREMIUM)
            
        return service_charge