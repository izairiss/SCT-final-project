""""
Description: A client program written to verify correctness of 
the BankAccount and Client classes.
"""
__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "Phoenixx Izairiss Ordonez"

from bank_account.bank_account import BankAccount
from client.client import Client

def main():
    """Test the functionality of the methods encapsulated 
    in the BankAccount and Client classes.
    """ 
    # In the statements coded below, ensure that any statement that could result 
    # in an exception is handled.  When exceptions are 'caught', display the exception 
    # message to the console.

    # 1. Code a statement which creates a valid instance of the Client class.
    # Use your own unique valid values for the inputs to the class.
    try:
        client = Client(1008, "Jennifer", "Huh", 
                        "jenniferhuh@pixell-river.com")

    except ValueError as e:
        print(e)



    # 2. Declare a BankAccount object with an initial value of None.
    bank_account = None
 


    # 3. Using the bank_account object declared in step 2, code a statement 
    # to instantiate the BankAccount object.
    # Use any integer value for the BankAccount number.
    # Use the client_number used to create the Client object in step 1 for the 
    # BankAccount's client_number. 
    # Use a floating point value for the balance. 
    try:
        bank_account = BankAccount(2001, client.client_number, 50220.22)

    except ValueError as e:
        print(e)



    # 4. Code a statement which creates an instance of the BankAccount class.
    # Use any integer value for the BankAccount number.
    # Use the client_number used to create the Client object in step 1 for the 
    # BankAccount's client_number. 
    # Use an INVALID value (non-float) for the balance. 
    try:
        invalid_balance = BankAccount(2001, client.client_number, "fifty")

    except ValueError as e:
        print(e)



    # 5. Code a statement which prints the Client instance created in step 1. 
    # Code a statement which prints the BankAccount instance created in step 3.
    print(client)
    print(bank_account)



    # 6. Attempt to deposit a non-numeric value into the BankAccount create in step 3. 
    try:
        bank_account.deposit("one")

    except ValueError as e:
        print(e)



    # 7. Attempt to deposit a negative value into the BankAccount create in step 3. 
    try:
        bank_account.deposit(-1.0)

    except ValueError as e:
        print(e)



    # 8. Attempt to withdraw a valid amount of your choice from the BankAccount create in step 3. 
    try:
        bank_account.withdraw(10620.04)

    except ValueError as e:
        print(e)



    # 9. Attempt to withdraw a non-numeric value from the BankAccount create in step 3. 
    try:
        bank_account.withdraw("ten")

    except ValueError as e:
        print(e)



    # 10. Attempt to withdraw a negative value from the BankAccount create in step 3. 
    try:
        bank_account.withdraw(-1.0)

    except ValueError as e:
        print(e)



    # 11. Attempt to withdraw a value from the BankAccount create in step 3 which 
    # exceeds the current balance of the account. 
    try:
        bank_account.withdraw(50220.23)

    except ValueError as e:
        print(e)

 

    # 12. Code a statement which prints the BankAccount instance created in step 3. 
    print(bank_account)
  


if __name__ == "__main__":
    main()