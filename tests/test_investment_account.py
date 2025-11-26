"""
Description: Unit tests for the InvestmentAccount class.
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_investment_account.py
"""
__author__ = "Phoenixx Izairiss Ordonez"
__version__ = "1.0.1"

import unittest
from datetime import date, timedelta
from bank_account.investment_account import InvestmentAccount

class TestInvestmentAccount(unittest.TestCase):

    def setUp(self):
        self.old_date = date.today() - timedelta(days = 11 * 365.25)
        self.exactly_ten = date.today() - timedelta(days = 10 * 365.25)
        self.new_date = date.today() - timedelta(days = 9 * 365.25)


    # Tests for the __init__ method.
    def test_init_valid_arguments_attributes_set(self):
        # Arrange & Act
        investment_account = InvestmentAccount(2001, 1008, 1000, \
                                                date(2004, 1, 6), 1.50)

        # Assert
        self.assertEqual(2001, \
                        investment_account._BankAccount__account_number)
        self.assertEqual(1008, investment_account._BankAccount__client_number)
        self.assertEqual(1000, investment_account._BankAccount__balance)
        self.assertEqual(date(2004, 1, 6), \
                        investment_account._date_created)
        self.assertEqual(1.50, \
                        investment_account._InvestmentAccount__management_fee)


    def test_init_invalid_management_fee_set_to_default(self):
        # Arrange & Act
        investment_account = InvestmentAccount(2001, 1008, 1000, \
                                                date(2004, 1, 6), "one")
        default = 2.55

        # Assert
        self.assertEqual(default, \
                        investment_account._InvestmentAccount__management_fee)


    # Tests for the get_service_charges method.
    def test_get_service_charges_more_than_ten_years_return_base_service_charge(self):
        # Arrange & Act
        investment_account = InvestmentAccount(2001, 1008, 1000, \
                                                self.old_date, 1.50)

        # Assert
        self.assertEqual(0.50, investment_account.get_service_charges())


    def test_get_service_charges_exactly_ten_years_return_calculated_service_charge(self):
        # Arrange & Act
        investment_account = InvestmentAccount(2001, 1008, 1000, \
                                                self.exactly_ten, 1.50)

        # Assert
        self.assertEqual(2.00, investment_account.get_service_charges())


    def test_get_service_charges_within_ten_years_return_calculated_service_charge(self):
        # Arrange & Act
        investment_account = InvestmentAccount(2001, 1008, 1000, \
                                                self.new_date, 1.50)

        # Assert
        self.assertEqual(2.00, investment_account.get_service_charges())


    # Tests for the __str__ method.
    def test_str_more_than_ten_years_return_waived_account_str(self):
        # Arrange
        investment_account = InvestmentAccount(2001, 1008, 1000, \
                                                self.old_date, 1.50)
        expected = ("Account Number: 2001 Balance: $1,000.00\n"
                    + f"Date Created: {self.old_date} "
                    + "Management Fee: Waived Account "
                    + "Account Type: Investment")
        
        # Act & Assert
        self.assertEqual(expected, str(investment_account))


    def test_str_more_than_within_years_return_waived_account_str(self):
        # Arrange
        investment_account = InvestmentAccount(2001, 1008, 1000, \
                                                self.new_date, 1.50)
        expected = ("Account Number: 2001 Balance: $1,000.00\n"
                    + f"Date Created: {self.new_date} "
                    + "Management Fee: $1.50 "
                    + "Account Type: Investment")
        
        # Act & Assert
        self.assertEqual(expected, str(investment_account))