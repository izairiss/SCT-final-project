__author__ = "ACE Faculty"
__version__ = "1.1.1"
__credits__ = "Phoenixx Izairiss Ordonez"

from PySide6.QtWidgets import QTableWidgetItem, QMessageBox
from PySide6.QtCore import Qt, Slot

from ui_superclasses.lookup_window import LookupWindow
from user_interface.account_details_window import AccountDetailsWindow
from user_interface.manage_data import load_data
from user_interface.manage_data import update_data
from bank_account.bank_account import BankAccount

class ClientLookupWindow(LookupWindow):
    """
    A class used to display client data.
    """
    def __init__(self):
        """
        Initializes the Client Lookup window
        """
        super().__init__()

        data_tuple = load_data()
        self.__client_listing = data_tuple[0]
        self.__accounts = data_tuple[1]

        self.filter_button.clicked.connect(self.__on_filter_clicked)
        self.lookup_button.clicked.connect(self.__on_lookup_client)
        self.client_number_edit.textChanged.connect(self.__on_text_changed)
        self.account_table.cellClicked.connect(self.__on_select_account)

    @Slot()
    def __on_lookup_client(self):
        """
        Obtain the Client object from the client_listing dictionary based on
        the client_number_edit widget, and display client data to the screen.
        Also, retrieve all BankAccount records assocoated with the Client and
        display details of those records in the account_table.
        If no Client record matches the client_number entered, a QMessageBox
        will display.
        """
        try:
            client_number = int(self.client_number_edit.text())
        except Exception as e:
            QMessageBox.information(self, "Input Error", "The client number " \
                                                    "must be a numeric value.")
            self.reset_display()

        if client_number in self.__client_listing:
            client = self.__client_listing[client_number]
            self.client_info_label.setText(f"Client Name: {client.first_name}"
                                        + f" {client.last_name}")
                
            self.account_table.setRowCount(0)
            row = 0

            for account in self.__accounts.values(): 

                if client.client_number == account.client_number:
                    account_number_item = \
                        QTableWidgetItem(str(account.account_number))
                        
                    balance_item = QTableWidgetItem(\
                                                f"${account.balance:,.2f}")

                    date_item = QTableWidgetItem(str(account._date_created))

                    account_type = \
                        QTableWidgetItem(account.__class__.__name__)
                    
                    
                    account_number_item.setTextAlignment(Qt.AlignCenter | 
                                                        Qt.AlignVCenter)
                    balance_item.setTextAlignment(Qt.AlignRight | 
                                                    Qt.AlignVCenter)
                    date_item.setTextAlignment(Qt.AlignCenter | 
                                                Qt.AlignVCenter)
                    account_type.setTextAlignment(Qt.AlignCenter | 
                                                    Qt.AlignVCenter)

                    
                    self.account_table.insertRow(row)
                    self.account_table.setItem(row, 0, account_number_item)
                    self.account_table.setItem(row, 1, balance_item)
                    self.account_table.setItem(row, 2, date_item)
                    self.account_table.setItem(row, 3, account_type)

                    row += 1

            self.account_table.resizeColumnsToContents()
            self.__toggle_filter(False)

        else:
            self.reset_display()
            QMessageBox.information(self, "Not Found", 
                                f"Client number: {client_number} not found.")
            

    @Slot()
    def __on_text_changed(self):
        """
        Clear all bank account records from the account_table.
        """
        self.account_table.setRowCount(0)


    @Slot(int, int)
    def __on_select_account(self, row: int, column: int):
        """
        Identify the account selected and transfer control to the Account 
        Details window based on the selected account.

        Args:
            row (int): Row that has been clicked on.
            column(int): Column that has been clicked on.
        """
        account_number = int(self.account_table.item(row, 0).text())

        if account_number in self.__accounts:
            account = self.__accounts[account_number]
            account_details = AccountDetailsWindow(account)
            account_details.balance_updated.connect(self.__update_data)
            account_details.exec_()

        elif account_number is None:
            QMessageBox.information(self, "Invalid Selection", 
                                    "Please select a valid record.")

        else:
            QMessageBox.information(self, "No Bank Account", 
                                    "Bank Account selected does not exist.")


    @Slot(BankAccount)
    def __update_data(self, account: BankAccount):
        """
        Updates the appropriate entry in the accounts dictionary with the 
        updated BankAccount.

        Args:
            account (BankAccount): A BankAccount object representing
                                    the updated BankAccount.
        """

        for row in range(self.account_table.rowCount()):
            account_number = int(self.account_table.item(row, 0).text())

            if account.account_number == account_number:
                self.account_table.item(row, 1).setText(\
                                f"${account.balance:,.2f}")

        
        self.__accounts[account.account_number] = account
        update_data(account)


    @Slot()
    def __on_filter_clicked(self):
        """
        Obtains user-defined filter criteria from the filter_combo_box and 
        the filter_edit widgets. Based on the criteria, filter the records 
        currently displayed in the account_table widget. Then toggle the 
        display of the filtering widgets so that the user can easily decipher 
        whether the listing in the account_table is complete of filtered.
        """

        if self.filter_button.text() == "Reset":
            self.__toggle_filter(False)
            return

        column_index = self.filter_combo_box.currentIndex()
        filter_value = self.filter_edit.text().strip().lower()

        # If user leaves filter_edit blank
        if not filter_value:
            self.__toggle_filter(False)
            return

        matching_accounts = []

        for i in range(self.account_table.rowCount()):
            item = self.account_table.item(i, column_index)
            self.account_table.setRowHidden(i, True)
            if item:
                cell_text = item.text().strip()
                match = False

                if column_index == 0:  # Account Number
                    try:
                        match = int(filter_value) == int(cell_text)
                    except ValueError:
                        match = False
                elif column_index == 1:  # Balance
                    try:
                        cell_amount = float(cell_text.replace('$', ''))
                        filter_amount = float(filter_value)
                        match = abs(cell_amount - filter_amount) < 0.01
                    except ValueError:
                        match = False
                elif column_index in (2, 3):  # Date Created or Account Type
                    match = filter_value in cell_text.lower()

            

                if match:
                    account_number_item = self.account_table.item(i, 0)
                    if account_number_item:
                        account_number = int(account_number_item.text())
                        account = self.__accounts.get(account_number)
                        if account:
                            matching_accounts.append(account)

                    self.account_table.setRowHidden(i, False)

        self.__toggle_filter(True)
        





    def __toggle_filter(self, filter_on: bool):
        """
        Toggles the display of the filter widgets to indicate to the user 
        whether or not filtering is currently taking place.

        Args:
            filter_on (bool): When True, the filter_button's text will display 
                            'Reset', filtering is currently taking place, 
                            and the user can press 'Reset' to redisplay all 
                            records.
                            When False, the filter_button's text will display 
                            'Apply Filter', filtering is currently not in 
                            place, and the user can apply filtering by making 
                            selections to the filtering widgets and press 
                            'Apply Filter' to display thee filtered subset 
                            of records.
        """
        self.filter_button.setEnabled(True)
        if filter_on:
            self.filter_button.setText("Reset")
            self.filter_combo_box.setEnabled(False)
            self.filter_edit.setEnabled(False)
            self.filter_label.setText("Data is Currently Filtered")
        else:
            self.filter_button.setText("Apply Filter")
            self.filter_combo_box.setEnabled(True)
            self.filter_edit.setEnabled(True)
            self.filter_edit.setText("")
            self.filter_combo_box.setCurrentIndex(0)
            
            for row in range(self.account_table.rowCount()):
                self.account_table.setRowHidden(row, False)

            self.filter_label.setText("Data is Not Currently Filtered")