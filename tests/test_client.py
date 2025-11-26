"""
Description: Unit tests for the Client class.
Author: ACE Faculty
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_client.py
"""
__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "Phoenixx Izairiss Ordonez"

import unittest
from client.client import Client


class TestClient(unittest.TestCase):

    def setUp(self):
        self.client = Client(1008, "Jennifer", "Huh", 
                            "jenniferhuh@pixell-river.com")
        

    # Tests for the __init__ method    
    def test_init_valid_arguments_attributes_set(self):
        # Arrange & Act
        client = Client(1008, "Jennifer", "Huh", 
                        "jenniferhuh@pixell-river.com")
        
        # Assert
        self.assertEqual(1008, client._Client__client_number)
        self.assertEqual("Jennifer", client._Client__first_name)
        self.assertEqual("Huh", client._Client__last_name)
        self.assertEqual("jenniferhuh@pixell-river.com", 
                            client._Client__email_address)
        
    
    def test_init_non_numeric_client_number_raises_valueerror(self):
        # Arrange, Act, & Assert
        with self.assertRaises(ValueError):
            client = Client("ten", "Jennifer", "Huh", 
                            "jenniferhuh@pixell-river.com")
            

    def test_init_blank_first_name_raises_valueerror(self):
        # Arrange, Act, & Assert
        with self.assertRaises(ValueError):
            client = Client(1008, "", "Huh", 
                            "jenniferhuh@pixell-river.com")
            

    def test_init_blank_last_name_raises_valueerror(self):
        # Arrange, Act, & Assert
        with self.assertRaises(ValueError):
            client = Client(1008, "Jennifer", "", 
                            "jenniferhuh@pixell-river.com")
            

    def test_init_invalid_email_address_set_default_value(self):
        # Arrange & Act
        client = Client(1008, "Jennifer", "Huh", 
                        "jenniferhuh.compixell-@river")
        
        # Assert
        self.assertEqual("email@pixell-river.com", client._Client__email_address)
            

    # Tests for the accessors
    def test_client_number_accessor_valid_client_number_returned(self):
        # Arrange
        # done in the setup
    
        # Act & Assert
        self.assertEqual(1008, self.client.client_number)


    def test_first_name_accessor_valid_first_name_returned(self):
        # Arrange
        # done in the setup
    
        # Act & Assert
        self.assertEqual("Jennifer", self.client.first_name)


    def test_last_name_accessor_valid_last_name_returned(self):
        # Arrange
        # done in the setup
    
        # Act & Assert
        self.assertEqual("Huh", self.client.last_name)


    def test_email_address_accessor_valid_email_address_returned(self):
        # Arrange
        # done in the setup
    
        # Act & Assert
        self.assertEqual("jenniferhuh@pixell-river.com", 
                            self.client.email_address)


    # Test for the __str__ method
    def test_str_valid_inputs_returns_formatted_string(self):
        # Arrange
        expected = "Huh, Jennifer [1008] - jenniferhuh@pixell-river.com "

        # Act & Assert
        self.assertEqual(expected, str(self.client))