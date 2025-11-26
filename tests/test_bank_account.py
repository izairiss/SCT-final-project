"""
Description: Unit tests for the BankAccount class.
Author: ACE Faculty
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_bank_account.py
"""
__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "Phoenixx Izairiss Ordonez"

import unittest
from bank_account.bank_account import BankAccount


class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.bank_account = BankAccount(2001, 1008, 50220.22)
        

    # Tests for the __init__ method.
    def test_init_valid_arguments_attributes_set(self):
        # Arrange & Act
        bank_account = BankAccount(2001, 1008, 50220.22)
        
        # Assert
        self.assertEqual(2001, bank_account._BankAccount__account_number)
        self.assertEqual(1008, bank_account._BankAccount__client_number)
        self.assertEqual(50220.22, bank_account._BankAccount__balance)


    def test_init_non_numeric_balance_set_to_zero(self):
        # Arrange and Act
        bank_account = BankAccount(2001, 1008, "fifty")

        # Assert
        self.assertEqual(0, bank_account._BankAccount__balance)


    def test_init_non_numeric_account_number_raises_valueerror(self):
        # Arrange, Act, & Assert
        with self.assertRaises(ValueError):
            bank_account = BankAccount("twenty", 1008, 50220.22)


    def test_init_non_numeric_client_number_raises_valueerror(self):
        # Arrange, Act, & Assert
        with self.assertRaises(ValueError):
            bank_account = BankAccount(2001, "ten", 50220.22)


    # Tests for the accessors.
    def test_account_number_accessor_valid_account_number_returned(self):
        # Arrange
        # done in the setup
    
        # Act & Assert
        self.assertEqual(2001, self.bank_account.account_number)
    
    
    def test_client_number_accessor_valid_client_number_returned(self):
        # Arrange
        # done in the setup
    
        # Act & Assert
        self.assertEqual(1008, self.bank_account.client_number)


    def test_balance_accessor_valid_balance_returned(self):
        # Arrange
        # done in the setup
    
        # Act & Assert
        self.assertEqual(50220.22, self.bank_account.balance)


    # Tests for the update_balance method.
    def test_update_balance_positive_amount_update_balance(self):
        # Arrange
        expected = 60840.26

        # Act
        self.bank_account.update_balance(10620.04)
        actual = self.bank_account.balance

        # Assert
        self.assertEqual(expected, actual)


    def test_update_balance_negative_amount_update_balance(self):
        # Arrange
        expected = 39600.18

        # Act
        self.bank_account.update_balance(-10620.04)
        actual = self.bank_account.balance

        # Assert
        self.assertEqual(expected, actual)


    def test_update_balance_non_numeric_value_remains_unchanged(self):
        # Arrange
        expected = 50220.22

        # Act
        self.bank_account.update_balance("ten")
        actual = self.bank_account.balance

        # Assert
        self.assertEqual(expected, actual)


    # Tests for the deposit method.
    def test_deposit_valid_amount_update_balance(self):
        # Arrange
        expected = 60840.26

        # Act 
        self.bank_account.deposit(10620.04)
        actual = self.bank_account.balance

        # Assert
        self.assertEqual(expected, actual)


    def test_deposit_negative_amount_raises_valueerror(self):
        # Arrange, Act, & Assert
        with self.assertRaises(ValueError):
            self.bank_account.deposit(-1.0)


    def test_deposit_non_numeric_raises_valueerror(self):
        # Arrange, Act, & Assert
        with self.assertRaises(ValueError):
            self.bank_account.deposit("one")


    # Tests for the withdraw method.
    def test_withdraw_valid_amount_update_balance(self):
        # Arrange
        expected = 39600.18

        # Act 
        self.bank_account.withdraw(10620.04)
        actual = self.bank_account.balance

        # Assert
        self.assertEqual(expected, actual)


    def test_withdraw_negative_amount_raises_valueerror(self):
        # Arrange, Act, & Assert
        with self.assertRaises(ValueError):
            self.bank_account.withdraw(-1.0)


    def test_withdraw_amount_exceeds_balance_raises_valueerror(self):
        # Arrange, Act, & Assert
        with self.assertRaises(ValueError):
            self.bank_account.withdraw(50220.23)


    def test_withdraw_non_numeric_raises_valueerror(self):
        # Arrange, Act, & Assert
        with self.assertRaises(ValueError):
            self.bank_account.withdraw("one")


    # Test for the __str__ method.
    def test_str_valid_inputs_returns_formatted_string(self):
        # Arrange
        expected = (f"Account Number: 2001 "
                + f"Balance: $50,220.22\n")
        
        # Act & Assert
        self.assertEqual(expected, str(self.bank_account))