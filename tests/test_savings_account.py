"""
Description: Unit tests for the SavingsAccount class.
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_savings_account.py
"""
__author__ = "Phoenixx Izairiss Ordonez"
__version__ = "1.0.1"

import unittest
from datetime import date
from bank_account.savings_account import SavingsAccount

class TestSavingsAccount(unittest.TestCase):
    # Tests for the __init__ method.
    def test_init_valid_arguments_attributes_set(self):
        # Arrange & Act
        savings_account = SavingsAccount(2001, 1008, 1000, \
                                        date(2004, 1, 6), 100)

        # Assert
        self.assertEqual(2001, \
                        savings_account._BankAccount__account_number)
        self.assertEqual(1008, savings_account._BankAccount__client_number)
        self.assertEqual(1000, savings_account._BankAccount__balance)
        self.assertEqual(date(2004, 1, 6), \
                        savings_account._date_created)
        self.assertEqual(100, \
                        savings_account._SavingsAccount__minimum_balance)
        

    def test_init_invalid_minimum_balance_set_to_default(self):
        # Arrange & Act
        savings_account = SavingsAccount(2001, 1008, 1000, \
                                        date(2004, 1, 6), "one")
        default = 50

        # Assert
        self.assertEqual(default, \
                        savings_account._SavingsAccount__minimum_balance)


    # Tests for the get_service_charges method.
    def test_get_service_charges_balance_greater_than_minimum_balance_return_base_service_charge(self):
        # Arrange & Act
        savings_account = SavingsAccount(2001, 1008, 1000, \
                                        date(2004, 1, 6), 100)

        # Assert
        self.assertEqual(0.50, savings_account.get_service_charges())


    def test_get_service_charges_balance_equal_minimum_balance_return_base_service_charge(self):
        # Arrange & Act
        savings_account = SavingsAccount(2001, 1008, 100, \
                                        date(2004, 1, 6), 100)

        # Assert
        self.assertEqual(0.50, savings_account.get_service_charges())


    def test_get_service_charges_balance_less_than_minimum_balance_return_base_service_charge(self):
        # Arrange & Act
        savings_account = SavingsAccount(2001, 1008, 99.99, \
                                        date(2004, 1, 6), 100)

        # Assert
        self.assertEqual(1.00, savings_account.get_service_charges())


    # Tests for the __str__ method.
    def test_str_valid_inputs_returns_formatted_string(self):
        # Arrange & Act
        savings_account = SavingsAccount(2001, 1008, 1000, \
                                        date(2004, 1, 6), 100)
        expected = ("Account Number: 2001 Balance: $1,000.00\n"
                    + f"Minimum Balance: $100.00 "
                    + "Account Type: Savings")

        # Assert
        self.assertEqual(expected, str(savings_account))