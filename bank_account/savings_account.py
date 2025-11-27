__author__ = "Phoenixx Izairiss Ordonez"
__version__ = "1.0.0"

from bank_account.bank_account import BankAccount
from datetime import date
from patterns.strategy.minimum_balance_strategy import MinimumBalanceStrategy

class SavingsAccount(BankAccount):
    """
    SavingsAccount class: Maintains savings account data.
    """
    # SERVICE_CHARGE_PREMIUM = 2.0

    def __init__(self, account_number: int, client_number: int, 
                balance: float, date_created: date, 
                minimum_balance: float):
        """
        Initializes the class attributes with argument values.

        Args:
            account_number (int): The bank account number.
            client_number (int): The client number representing
                                    the account holder.
            balance (float): The current balance of the bank account.
            date_created (date): The date created.
            minimum_balance (float): The minimum value a balance can be before
                                    further service charges are applied.

        Raises:
            ValueError: When account number is non-numeric, or when client 
                        number is non-numeric.
        """
        super().__init__(account_number, client_number, balance, date_created)
        
        try: 
            self.__minimum_balance = float(minimum_balance)
        except ValueError as e:
            self.__minimum_balance = 50

        self.__strategy = MinimumBalanceStrategy(minimum_balance)


    def __str__(self) -> str:
        """
        Returns the string value returned from the superclass(BankAccount)
        along with a representation of the subclass instance.

        Returns: 
            str: The BankAccount and SavingsAccount instance 
                                                    foramatted as string.
        """
        return_string = super().__str__()
        return_string += (f"Minimum Balance: ${self.__minimum_balance:,.2f} "
                        + "Account Type: Savings")
        
        return(return_string)


    def get_service_charges(self) -> float:
        """
        Calculates service charge.

        Returns:
            float: The calculated service charge.
        """
        # if self.balance >= self.__minimum_balance:
        #     service_charge = self.BASE_SERVICE_CHARGE
        # else: 
        #     service_charge = (self.BASE_SERVICE_CHARGE * 
        #                         self.SERVICE_CHARGE_PREMIUM)
            
        # return service_charge

        return self.__strategy.calculate_service_charges(self)
