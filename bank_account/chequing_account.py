__author__ = "Phoenixx Izairiss Ordonez"
__version__ = "1.0.0"

from bank_account.bank_account import BankAccount
from datetime import date
from patterns.strategy.overdraft_strategy import OverdraftStrategy

class ChequingAccount(BankAccount):
    """
    ChequingAccount class: Maintains chequing account data.
    """
    def __init__(self, account_number: int, client_number: int, 
                balance: float, date_created: date, 
                overdraft_limit: float, overdraft_rate: float):
        """
        Initializes the class attributes with argument values.

        Args:
            account_number (int): The bank account number.
            client_number (int): The client number representing
                                    the account holder.
            balance (float): The current balance of the bank account.
            date_created (date): The date created.
            overdraft_limit (float): The maximum amount a balance can be 
                                    overdrawn (below 0.00) before overdraft 
                                    fees are applied.
            overdraft_rate (float): The rate to which the overdraft fees 
                                    will be applied.

        Raises:
            ValueError: When account number is non-numeric, or when client 
                        number is non-numeric.
        """
        super().__init__(account_number, client_number, balance, date_created)

        try: 
            self.__overdraft_limit = float(overdraft_limit)
        except ValueError as e:
            self.__overdraft_limit = -100

        try:
            self.__overdraft_rate = float(overdraft_rate)
        except ValueError as e:
            self.__overdraft_rate = 0.05

        self.__strategy = OverdraftStrategy(self.__overdraft_limit, \
                                            self.__overdraft_rate)

        
    def __str__(self) -> str:
        """
        Returns the string value returned from the superclass(BankAccount)
        along with a representation of the subclass instance.

        Returns: 
            str: The BankAccount and ChequingAccount instance 
                                                    foramatted as string.
        """
        rate = self.__overdraft_rate * 100
        return_string = super().__str__()
        return_string += (f"Overdraft Limit: ${self.__overdraft_limit:,.2f} "
                          + f"Overdraft Rate: {rate:.2f}% "
                          + "Account Type: Chequing")
        
        return(return_string)
        

    def get_service_charges(self) -> float:
        """
        Calculates service charge.

        Returns:
            float: The calculated service charge.
        """
        # if self.balance >= self.__overdraft_limit:
        #     service_charge = self.BASE_SERVICE_CHARGE
        # else:
        #     service_charge = (self.BASE_SERVICE_CHARGE + 
        #     (self.__overdraft_limit - self.balance) * self.__overdraft_rate)

        # return service_charge
        return self.__strategy.calculate_service_charges(self)
    
