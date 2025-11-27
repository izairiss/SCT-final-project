__author__ = "Phoenixx Izairiss Ordonez"
__version__ = "1.0.1"


from patterns.strategy.service_charge_strategy import ServiceChargeStrategy
from bank_account.bank_account import BankAccount
from datetime import date, timedelta

class ManagementFeeStrategy(ServiceChargeStrategy):
    """
    The ManagementFeeStrategy strategy is a subclass of the 
    ServiceChargeStrategy superclass.
    """
    TEN_YEARS_AGO = date.today() - timedelta(days = 10 * 365.25)

    def __init__(self, date_created: date, management_fee: float):
        """
        Initializes the class attributes with argument values.

        Args:
            date_created (date): The date created.
            management_fee (float): The flat-rate fee the bank charges for 
                                    managing an investment account.
        """
        self.__date_created = date_created
        self.__management_fee = management_fee


    def calculate_service_charges(self, account: BankAccount) -> float:
        """
        Calculates service charge.

        Args: 
            account (BankAccount): The user's bank account data.

        Returns:
            float: The calculated service charge based on the 
                    accounts date of creation.
        """
        if account._date_created < self.TEN_YEARS_AGO:
            service_charge = self.BASE_SERVICE_CHARGE
        else:
            service_charge = self.BASE_SERVICE_CHARGE + self.__management_fee

        return service_charge

