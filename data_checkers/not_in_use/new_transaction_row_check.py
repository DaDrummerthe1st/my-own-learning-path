import os

import pandas as pd

file = "data/transactions_original.csv"

df_transactions = pd.read_csv(file)
# display(df_transactions.head())
# print(df_transactions.dtypes)

# print(df_transactions.columns)
# this filename is f26185400.ipynb from dataretrieval

# df_parsed = pd.DataFrame()
class Checks:
    def  __init__(self):
        pass

    def none(self, cell):
        if cell is None:
            error_message = "transaction_id is None"
            return error_message
    

class Rows:
    def __init__(self, csv_datafrane):
        self.csv_dataframe = csv_datafrane
        self.error_messages = []

        self.check_transaction_id()
    
    def check_transaction_id(self, cell):
        """I would want this to be a class instead. ParentClass: stdsearches. Others inherit with specific attributes and settings"""

        self.error_messages.append(self.checker.none())
        
        try:
            str(cell)
        except Exception as e:
            self.error_messages.append(f"In amount, exception: {e}")

        if self.error_messages != []:
            return self.error_messages


    def check_timestamp(cell):
        error_messages = []

        if cell is None:
            error_messages.append("Timestamp is None")
            return error_messages


        try:
            pd.to_datetime(cell)
        except Exception as e:
            error_messages.append(f"In timestamp, exception: {e}")

        if error_messages == []:
            return
        else:
            return error_messages
############ Only refactored up until here!

    def check_amount(cell):
        error_messages = []

        if cell is None:
            error_messages.append(f"amount is None")
            return error_messages


        try:
            float(cell)
        except Exception as e:
            error_messages.append(f"In amount, exception: {e}")

        if error_messages == []:
            return
        else:
            return error_messages

    def check_currency(cell):
        error_messages = []

        if cell is None:
            error_messages.append("currency is None")
            return error_messages


        try:
            str(cell)
        except Exception as e:
            error_messages.append(f"In currency, exception: {e}")

        if error_messages == []:
            return
        else:
            return error_messages


    def check_sender_account(cell):
        error_messages = []

        if cell is None:
            error_messages.append("sender_account is None")
            return error_messages


        try:
            str(cell)
        except Exception as e:
            error_messages.append(f"In sender_account, exception: {e}")

        if error_messages == []:
            return
        else:
            return error_messages
        
    def check_receiver_account(cell):
        error_messages = []

        if cell is None:
            error_messages.append("receiver_account is None")
            return error_messages


        try:
            str(cell)
        except Exception as e:
            error_messages.append(f"In receiver_account, exception: {e}")

        if error_messages == []:
            return
        else:
            return error_messages

    def check_sender_country(cell):
        error_messages = []

        if cell is None:
            error_messages.append("sender_country is None")
            return error_messages


        try:
            str(cell)
        except Exception as e:
            error_messages.append(f"In sender_country, exception: {e}")

        if error_messages == []:
            return
        else:
            return error_messages

    def check_sender_municipality(cell):
        error_messages = []

        if cell is None:
            error_messages.append("sender_municipality is None")
            return error_messages


        try:
            str(cell)
        except Exception as e:
            error_messages.append(f"In sender_municipality, exception: {e}")

        if error_messages == []:
            return
        else:
            return error_messages

    def check_receiver_country(cell):
        error_messages = []

        if cell is None:
            error_messages.append("receiver_country is None")
            return error_messages


        try:
            str(cell)
        except Exception as e:
            error_messages.append(f"In receiver_country, exception: {e}")

        if error_messages == []:
            return
        else:
            return error_messages

    def check_receiver_municipality(cell):
        error_messages = []

        if cell is None:
            error_messages.append("receiver_municipality is None")
            return error_messages


        try:
            str(cell)
        except Exception as e:
            error_messages.append(f"In receiver_municipality, exception: {e}")

        if error_messages == []:
            return
        else:
            return error_messages

    def check_transaction_type(cell):
        error_messages = []

        if cell is None:
            error_messages.append("transaction_type is None")
            return error_messages

        try:
            str(cell)
        except Exception as e:
            error_messages.append(f"In transaction_type, exception: {e}")

        if error_messages == []:
            return
        else:
            return error_messages
        
    def check_notes(cell):
        error_messages = []

        if cell is None:
            error_messages.append("notes is None")
            return error_messages

        try:
            str(cell)
        except Exception as e:
            error_messages.append(f"In notes, exception: {e}")

        if error_messages == []:
            return
        else:
            return error_messages
        

row = Rows

