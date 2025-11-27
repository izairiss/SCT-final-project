"""
Description: A client program written to verify implementation 
of the Observer Pattern.
"""
__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "Phoenixx Izairiss Ordonez"

# 1.  Import all BankAccount types using the bank_account package
#     Import date
#     Import Client
from bank_account import *
from datetime import date
from client.client import Client





# 2. Create a Client object with data of your choice.
try:
    client = Client(1008, "Jennifer", "Huh", 
                    "jenniferhuh@pixell-river.com")

except ValueError as e:
    print(e)



# 3a. Create a ChequingAccount object with data of your choice, using the client_number 
# of the client created in step 2.
# 3b. Create a SavingsAccount object with data of your choice, using the client_number 
# of the client created in step 2.
try:
    chequing_account = ChequingAccount(2001, client.client_number, 1500, \
                                        date(2004, 1, 6), -1000, 0.10)
    
except ValueError as e:
    print(e)

try:
    savings_account = SavingsAccount(2001, client.client_number, 1000, \
                                            date(2004, 1, 6), 100)
    
except ValueError as e:
    print(e)

# 4 The ChequingAccount and SavingsAccount objects are 'Subject' objects.
# The Client object is an 'Observer' object.  
# 4a.  Attach the Client object (created in step 1) to the ChequingAccount object (created in step 2).
# 4a.  Attach the Client object (created in step 1) to the SavingsAccount object (created in step 2).
chequing_account.attach(client)
savings_account.attach(client)



# 5a. Create a second Client object with data of your choice.
# 5b. Create a SavingsAccount object with data of your choice, using the client_number 
# of the client created in this step.
try:
    second_client = Client(1001, "Chaewon", "Kim", 
                    "chaewonkim@pixell-river.com")

except ValueError as e:
    print(e)

try:
    second_savings_account = SavingsAccount(8120, second_client.client_number, \
                                        5000, date(2000, 8, 1), 150)
    
except ValueError as e:
    print(e)

# 6. Use the ChequingAccount and SavingsAccount objects created 
# in steps 3 and 5 above to perform transactions (deposits and withdraws) 
# which would cause the Subject (BankAccount) to notify the Observer 
# (Client) as well as transactions that would not 
# cause the Subject to notify the Observer.  Ensure each 
# BankAccount object performs at least 3 transactions.
# REMINDER: the deposit() and withdraw() methods can raise exceptions
# ensure the methods are invoked using proper exception handling such 
# that any exception messages are printed to the console.

# Testing chequing_account
try: 
    chequing_account.deposit(10000.00)

except ValueError as e:
    print(e)

try: 
    chequing_account.withdraw(11450.01)

except ValueError as e:
    print(e)


try: 
    chequing_account.deposit(2000.00)

except ValueError as e:
    print(e)


# Testing savings_account
try: 
    savings_account.withdraw(950.01)

except ValueError as e:
    print(e)


try: 
    savings_account.deposit(10000.00)

except ValueError as e:
    print(e)


try: 
    savings_account.deposit(2000.00)

except ValueError as e:
    print(e)


# Testing second_savings_account
try: 
    second_savings_account.withdraw(950.01)

except ValueError as e:
    print(e)


try: 
    second_savings_account.deposit(10000.00)

except ValueError as e:
    print(e)


try: 
    second_savings_account.deposit(2000.00)

except ValueError as e:
    print(e)