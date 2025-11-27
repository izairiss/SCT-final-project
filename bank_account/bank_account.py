__author__ = "Phoenixx Izairiss Ordonez"
__version__ = "1.1.1"

from abc import ABC, abstractmethod
from patterns.observer.subject import Subject
from patterns.observer.observer import Observer
from datetime import date


class BankAccount(Subject, ABC):
    """
    BankAccount class: Maintains bank account data 
    and handles the observers list.
    """ 
    # BASE_SERVICE_CHARGE = 0.50  
    LARGE_TRANSACTION_THRESHOLD = 9999.99
    LOW_BALANCE_LEVEL = 50.0

    def __init__(self, account_number: int, \
                client_number: int, balance: float, date_created: date):
        """
        Initializes the class attributes with argument values.

        Args:
            account_number (int): The bank account number.
            client_number (int): The client number representing
                                    the account holder.
            balance (float): The current balance of the bank account.
            date_created (date): The date created.

        Raises:
            ValueError: When account number is non-numeric, or when client 
                        number is non-numeric.

        """
        super().__init__()

        if isinstance(account_number, int):
            self.__account_number = account_number
        else:
            raise ValueError("Account Number must be numeric.")
        

        if isinstance(client_number, int):
            self.__client_number = client_number
        else:
            raise ValueError("Client Number must be numeric.")
        

        try:
            self.__balance = float(balance)

        except ValueError as e:
            self.__balance = 0


        if isinstance(date_created, date):
            self._date_created = date_created
        else:
            self._date_created = date.today()


    @property
    def account_number(self) -> int:
        """
        Accessor for account number attribute.

        Returns: 
            int: The bank account number.

        """
        return self.__account_number


    @property
    def client_number(self) -> int:
        """
        Accessor for client number attribute.

        Returns: 
            int: The client number representing
                            the account holder.

        """
        return self.__client_number
        

    @property
    def balance(self) -> float:
        """
        Accessor for balance attribute.

        Returns: 
            float: The current balance of the bank account.

        """
        return self.__balance
        
       
    def update_balance(self, amount: float) -> None:
        """
        Updates balance and notify a client 
        if either of the situations occur.

        Args:
            amount (float): The amount received.

        """
        if isinstance(amount, float):
            self.__balance += amount
        else:
            amount = 0

        if self.__balance < self.LOW_BALANCE_LEVEL:
            self.notify(f"Low balance warning ${self.__balance:,.2f}: "
                        + f"on account {self.__account_number}")

        if abs(amount) > self.LARGE_TRANSACTION_THRESHOLD: 
            self.notify(f"Large transaction ${amount:,.2f}: "
                        + f"on account {self.__account_number}")



    def deposit(self, amount: float) -> None:
        """
        Checks amount to make sure it's numeric and positive, 
        then uses the update_balance method to update the Bank
        Account's balance if amount is valid.

        Args:
            amount (float): The amount to be deposited.

        Raises:
            ValueError: When amount is non-numeric or negative.

        """
        if isinstance(amount, str) or isinstance(amount, int):
            raise ValueError(f"Deposit amount: {amount} must be numeric.")
        elif amount < 0:
            raise ValueError(f"Deposit amount: ${amount:,.2f} "
                            + "must be positive.")
        else:
            self.update_balance(amount)


    def withdraw(self, amount: float) -> None:
        """
        Checks amount to make sure it's numeric, positive, and equal
        or smaller than the account balance, then uses the update_balance 
        method to update the Bank Account's balance if amount is valid.

        Args:
            amount (float): The amount to be withdrawn.

        Raises:
            ValueError: When amount is non-numeric, negative, or when 
            amount is larger than the account balance.

        """
        if isinstance(amount, str) or isinstance(amount, int):
            raise ValueError(f"Withdrawal amount: {amount} must be numeric.")
        elif amount < 0:
            raise ValueError(f"Withdrawal amount: ${amount:,.2f} "
                            + "must be positive.")
        elif amount > self.__balance:
            raise ValueError(f"Withdrawal amount: ${amount:,.2f} must not "
                    + f"exeed the account balance: ${self.__balance:,.2f}")
        else:
            self.update_balance(-amount)


    def __str__(self) -> str:
        """
        Returns a string representation of the class instance.

        Returns:
            str: The BankAccount instance formatted as a string.

        """
        return(f"Account Number: {self.__account_number} "
                + f"Balance: ${self.__balance:,.2f}\n")


    @abstractmethod
    def get_service_charges() -> float:
        """
        Calculates service charges that a BankAccount will incur. 
        Implemented in subclass(es).
        """
        pass


    def attach(self, observer: Observer):
        """
        Adds a new observer to the subject's list of observers.

        Args:
            observer (Observer): A client

        """
        self._observers.append(observer)


    def detach(self, observer: Observer):
        """
        Removes an observer from the subject's list of observers.

        Args:
            observer (Observer): A client

        """
        self._observers.remove(observer)


    def notify(self, message: str):
        """
        Iterates through the list of observers and 
        updates each observer with the message. 

        Args:
            message (str): The details of the unusual activity.

        """
        for i in self._observers:
            i.update(message)