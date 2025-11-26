"""
Description: Unit tests for the ChequingAccount class.
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_chequing_account.py
"""
__author__ = "Phoenixx Izairiss Ordonez"
__version__ = "1.0.1"

import unittest
from datetime import date
from bank_account.chequing_account import ChequingAccount

class TestChequingAccount(unittest.TestCase):

    def setUp(self):
        self.chequing_account = ChequingAccount(2001, 1008, -50, \
                                                date(2025, 1, 6), -1000, 0.10)
        

    # Tests for the __init__ method.
    def test_init_valid_arguments_attributes_set(self):
        # Arrange & Act
        chequing_account = ChequingAccount(2001, 1008, -50, \
                                            date(2025, 1, 6), -1000, 0.10)

        # Assert
        self.assertEqual(2001, \
                        chequing_account._BankAccount__account_number)
        self.assertEqual(1008, chequing_account._BankAccount__client_number)
        self.assertEqual(-50, chequing_account._BankAccount__balance)
        self.assertEqual(date(2025, 1, 6), chequing_account._date_created)
        self.assertEqual(-1000, \
                        chequing_account._ChequingAccount__overdraft_limit)
        self.assertEqual(0.10, \
                        chequing_account._ChequingAccount__overdraft_rate)


    def test_init_invalid_overdraft_limit_set_to_default(self):
        # Arrange & Act
        chequing_account = ChequingAccount(2001, 1008, -50, \
                                            date(2025, 1, 6), "one", 0.10)
        default = -100

        # Assert 
        self.assertEqual(default, \
                        chequing_account._ChequingAccount__overdraft_limit)


    def test_init_invalid_overdraft_rate_set_to_default(self):
         # Arrange & Act
        chequing_account = ChequingAccount(2001, 1008, -50, \
                                            date(2025, 1, 6), -1000, "one")
        default = 0.05

        # Assert 
        self.assertEqual(default, \
                        chequing_account._ChequingAccount__overdraft_rate)


    def test_init_invalid_date_created_set_to_today_method(self):
        # Arrange & Act
        chequing_account = ChequingAccount(2001, 1008, -50, \
                                            (2025, 1, 6), -1000, 0.10)
        expected = date.today()

        # Assert 
        self.assertEqual(expected, chequing_account._date_created)

    
    # Tests for the get_service_charges method.
    def test_get_service_charges_balance_greater_than_overdraft_limit_return_base_service_charge(self):
        # Arrange, Act & Assert
        self.assertEqual(0.50, self.chequing_account.get_service_charges())


    def test_get_service_charges_balance_less_than_overdraft_limit_return_calculated_service_charge(self):
        # Arrange & Act 
        chequing_account = ChequingAccount(2001, 1008, -6000, \
                                            date(2025, 1, 6), -1000, 0.10)

        # Assert
        self.assertEqual(500.50, chequing_account.get_service_charges())


    def test_get_service_charges_balance_equal_overdraft_limit_return_base_service_charge(self):
        # Arrange & Act  
        chequing_account = ChequingAccount(2001, 1008, -1000, \
                                            date(2025, 1, 6), -1000, 0.10)

        # Assert
        self.assertEqual(0.50, chequing_account.get_service_charges())


    # Test for the __str__ method.
    def test_str_valid_inputs_returns_formatted_string(self):
        # Arrange
        expected = ("Account Number: 2001 Balance: $-50.00\n"
                    + "Overdraft Limit: $-1,000.00 "
                    + "Overdraft Rate: 10.00% Account Type: Chequing")
        
        # Act & Assert
        self.assertEqual(expected, str(self.chequing_account))