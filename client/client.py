__author__ = "Phoenixx Izairiss Ordonez"
__version__ = "1.0.0"

from patterns.observer.observer import Observer
from utility.file_utils import simulate_send_email
from datetime import datetime
from email_validator import validate_email, EmailNotValidError

class Client(Observer):
    """
    Client class: Maintains client data
    """
    def __init__(self, client_number: int, first_name: str, \
                        last_name: str, email_address: str):
        """
        Initializes the class attributes with argument values.

        Args:
            client_number (int): Represents the client number.
            first_name (str): The client's first name.
            last_name (str): The client's last name.
            email_address (str): The client's email address.

        Raises:
            ValueError: When client number is non-numeric, 
                        first name is blank, or when last name is blank.

        """

        if isinstance(client_number, int):
            self.__client_number = client_number
        else:
            raise ValueError("Client Number must be numeric.")
        
        if len(first_name.strip()) > 0:
            self.__first_name = first_name
        else:
            raise ValueError("First Name cannot be blank.")
        
        if len(last_name.strip()) > 0:
            self.__last_name = last_name
        else:
            raise ValueError("Last Name cannot be blank.")
        
        try:
            validated_email = validate_email(email_address, 
                                            check_deliverability = False)

            self.__email_address = validated_email.normalized

        except EmailNotValidError as e:
            self.__email_address = "email@pixell-river.com"
        

    @property
    def client_number(self) -> int:
        """
        Accessor for client number attribute.

        Returns: 
            int: The client number.

        """
        return self.__client_number
    
    @property
    def first_name(self) -> str:
        """
        Accessor for first name attribute.

        Returns: 
            str: The client's first name.

        """
        return self.__first_name
    
    @property
    def last_name(self) -> str:
        """
        Accessor for last name attribute.

        Returns: 
            str: The client's last name.

        """
        return self.__last_name
    
    @property
    def email_address(self) -> str:
        """
        Accessor for email address attribute.

        Returns: 
            str: The client's email address.

        """
        return self.__email_address
    

    def __str__(self):
        """
        Returns a string representation of the client instance.

        Returns: 
            str: The client instance formatted as a string.

        """

        return (f"{self.__last_name.title()}, {self.__first_name.title()}"
                + f" [{self.__client_number}]"
                + f" - {self.__email_address} ")
    
    
    def update(self, message: str):
        """
        The update method performs some action 
        if the Observer has been notified.

        Args:
            message (str): The details of the unusual activity.

        """
        subject = f"ALERT: Unusual Activity: {datetime.now()}"
        message_format = (f"Notification for {self.__client_number}: "
                    + f"{self.__first_name} {self.__last_name}: {message}")
        
        simulate_send_email(self.__email_address, subject, message_format)

