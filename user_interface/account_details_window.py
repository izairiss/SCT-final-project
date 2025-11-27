__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "Phoenixx Izairiss Ordonez"

from ui_superclasses.details_window import DetailsWindow
from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import Signal, Qt, Slot
from bank_account.bank_account import BankAccount
import copy

class AccountDetailsWindow(DetailsWindow):
    """
    A class used to display account details and 
    perform bank account transactions.
    """
    balance_updated = Signal(BankAccount)
    def __init__(self, account: BankAccount) -> None:
        """
        Initializes a new instance of the ExtendedAccountDetails window.
        Args:
            account: The bank account to be displayed.
        Returns:
            None
        """
        super().__init__()

        if isinstance(account, BankAccount):
            self.__account = copy.deepcopy(account)

            self.account_number_label.setText(str(account.account_number))
            self.balance_label.setText(f"${account.balance:,.2f}")

            self.account_number_label.setAlignment(Qt.AlignRight | 
                                                        Qt.AlignVCenter)
            self.balance_label.setAlignment(Qt.AlignRight | 
                                                    Qt.AlignVCenter)
            
            self.deposit_button.clicked.connect(self.__on_apply_transaction)
            self.withdraw_button.clicked.connect(self.__on_apply_transaction)
            self.exit_button.clicked.connect(self.__on_exit)


        else:
            self.reject()


    @Slot()
    def __on_apply_transaction(self):
        """
        Attempts to perform a transaction using the amount entered into the 
        corresponding BankAccount. It will update the balance label upon 
        success, and issue a QMessageBox if transaction is unsuccessful.
        """
        try:
            amount = float(self.transaction_amount_edit.text())

            try:
                sender = self.sender()

                if sender == self.deposit_button:
                    transaction = "Deposit"
                    self.__account.deposit(amount)
                elif sender == self.withdraw_button:
                    transaction = "Withdraw"
                    self.__account.withdraw(amount)

                self.balance_updated.emit(self.__account)

                self.balance_label.setText(f"${self.__account.balance:,.2f}")
                self.transaction_amount_edit.setText("")
                self.transaction_amount_edit.setFocus()
 
            except Exception as e:
                QMessageBox.information(self, f"{transaction} Failed", str(e))
                
        except Exception as e:
            QMessageBox.information(self, "Invalid Data", 
                                    "Amount must be numeric.")
            self.transaction_amount_edit.setText("")
            self.transaction_amount_edit.setFocus()


    @Slot()
    def __on_exit(self):
        """
        Will close the QDialog, returning the user to Client Lookup Window.
        """
        self.close()
