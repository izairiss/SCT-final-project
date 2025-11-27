__author__ = "Phoenixx Izairiss Ordonez"
__version__ = "1.0.1"

from bank_account.bank_account import BankAccount
from datetime import date, timedelta
from patterns.strategy.management_fee_strategy import ManagementFeeStrategy

class InvestmentAccount(BankAccount):
    """
    InvestmentAccount class: Maintains investment account data.
    """
    TEN_YEARS_AGO = date.today() - timedelta(days = 10 * 365.25)

    def __init__(self, account_number: int, client_number: int, 
                balance: float, date_created: date, 
                management_fee: float):
        """
        Initializes the class attributes with argument values.

        Args:
            account_number (int): The bank account number.
            client_number (int): The client number representing
                                    the account holder.
            balance (float): The current balance of the bank account.
            date_created (date): The date created.
            management_fee (float): The flat-rate fee the bank charges for 
                                    managing an investment account.

        Raises:
            ValueError: When account number is non-numeric, or when client 
                        number is non-numeric.
        """
        super().__init__(account_number, client_number, balance, date_created)
        
        try: 
            self.__management_fee = float(management_fee)
        except ValueError as e:
            self.__management_fee = 2.55

        self.__strategy = ManagementFeeStrategy(date_created, management_fee)

        


    def __str__(self) -> str:
        """
        Returns the string value returned from the superclass(BankAccount)
        along with a representation of the subclass instance.

        Returns: 
            str: The BankAccount and InvestmentAccount instance 
                                                    foramatted as string.
        """
        return_string = super().__str__()        

        if self._date_created >= self.TEN_YEARS_AGO:
            fee_result = f"${self.__management_fee:,.2f} "
        else:
            fee_result = "Waived Account "

        return_string += (f"Date Created: {self._date_created} "
                            + "Management Fee: " + fee_result
                            + "Account Type: Investment") 
        
        return(return_string)


    def get_service_charges(self) -> float:
        """
        Calculates service charge.

        Returns:
            float: The calculated service charge.
        """
        # if self._date_created < self.TEN_YEARS_AGO:
        #     service_charge = self.BASE_SERVICE_CHARGE
        # else:
        #     service_charge = self.BASE_SERVICE_CHARGE + self.__management_fee

        # return service_charge
        return self.__strategy.calculate_service_charges(self)