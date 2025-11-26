__author__ = "Phoenixx Izairiss Ordonez"
__version__ = "1.0.0"


from patterns.strategy.service_charge_strategy import ServiceChargeStrategy
from bank_account.bank_account import BankAccount

class OverdraftStrategy(ServiceChargeStrategy):
    """
    The OverdraftStrategy strategy is a subclass of the ServiceChargeStrategy
    superclass.
    """

    def __init__(self, overdraft_limit: float, overdraft_rate: float):
        """
        Initializes the class attributes with argument values.

        Args:
            overdraft_limit (float): The maximum amount a balance can be 
                                    overdrawn (below 0.00) before overdraft 
                                    fees are applied.
            overdraft_rate (float): The rate to which the overdraft fees 
                                    will be applied.
        """

        self.__overdraft_limit = overdraft_limit
        self.__overdraft_rate = overdraft_rate


    def calculate_service_charges(self, account: BankAccount) -> float:
        """
        Calculates service charge.

        Args: 
            account (BankAccount): The user's bank account data.

        Returns:
            float: The calculated service charge based on the 
                    account balance and overdraft limit.
        """
        
        if account.balance >= self.__overdraft_limit:
            service_charge = self.BASE_SERVICE_CHARGE
        else:
            service_charge = (self.BASE_SERVICE_CHARGE + 
                            (self.__overdraft_limit - account.balance) * 
                            self.__overdraft_rate)

        return service_charge