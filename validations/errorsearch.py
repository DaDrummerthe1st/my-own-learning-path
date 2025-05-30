from datetime import datetime
import random
import string
import os

import pandas as pd


class CheckForErrors:
    """
    All error checking in transaction-files are gathered in same class
    A unique identifier is applied - ok for up til 8 rows per microsecond.

    Mandatory column structure for csv-file:
    ['transaction_id','timestamp','amount','currency','sender_account',
    'receiver_account','sender_country','sender_municipality','receiver_country',
    'receiver_municipality','transaction_type','notes']

    This class looks for csv_filename in /data/...
    """
    def __init__(self, csv_filename):
        """
        1. Adding a unique identifier for the run
        """
        # argument to attributes definitions
        self.csv_filename = csv_filename

        # create the dataframe
        current_dir = os.path.dirname(os.path.abspath(__file__))
        csv_path = os.path.abspath(os.path.join(current_dir, '..', 'data', csv_filename))
        # TODO: on_ba_lines=... when reading the csv if any errors occur, perhaps a try/except?
        self.dataframe = pd.read_csv(csv_path)

        # object specific attributes definitions
        self.error_dict = {} # collection of all errors

        # TODO: run all
        # self.run_all()

    def random_uppercase_digit(self, length=8):
        random_string = ''.join(random.choices(
            string.ascii_uppercase + string.digits, k=length))
        return random_string


    def create_unique_parse_id(self):
        """
        Creates a unique identifier for transaction rows

        note: microseconds (%f) has 6 (six) digits
        note: if server runs are faste than 8 per milliseconds then up the length-value
        """

        # get the timestamp
        now = datetime.now().strftime("%Y%m%d%H%M%S%f")
        
        # create a random string for absolute uniqueness
        random_string = self.random_uppercase_digit(length=8)
        
        f = now + random_string
        return f
    
    def input_unique_identifier(self):
        self.dataframe["parse_id"] = self.create_unique_parse_id()
        # print(self.dataframe.head())

    # def run_all(self):
    #     for idx, row in self.dataframe.iterrows():


    def whitespace_in_amount(self):
        # successful_rows = 0
        # if self.dataframe.amount.
        # # try:
        # #     self.dataframe["amount"].astype(float)
        # #     self.dataframe["amount"] = self.dataframe["amount"].astype(str)
        # # except Exception as e:
        # #     self.error_dict.update({self.dataframe.parse_id:{"error_message":e, "field":"amount"}})
        # # else:
        # #     successful_rows += 1

        # print(successful_rows)
        # print(self.error_dict)

        # Prepare to check for whitespace in each field (particularly "amount") and track errors
        # error_log = {}

        # Loop through each row
        for index, row in self.dataframe.iterrows():
            row_errors = {}
            parse_id = self.dataframe.iloc[index]["parse_id"]

            for col in self.dataframe.columns:
                value = row[col]
                # Check for leading/trailing or mid-value space in numeric fields
                if col == "amount":
                    try:
                        int(str(value).replace('.', '', 1))
                        # Whitespace or other invalid format detected
                        # Method explained: erase maximum one period sign,
                        #     then make sure all remaining are digits
                        #     meaming no whitespace or other characters are present
                    except ValueError as e:
                        # Create an error_id
                        random_string = self.random_uppercase_digit()
                        unique_error_id = f"{parse_id}_{col}_{random_string}"

                        row_errors[unique_error_id] = {
                            "error_message": f"{e}: '{value}'",
                            "column" : col,
                            "parse_id" : parse_id
                        }

            if row_errors:
                self.error_dict[parse_id].update(row_errors)

        # Show error log
        print(self.error_dict)



new_run = CheckForErrors("transactions_original.csv")
new_run.input_unique_identifier()
new_run.whitespace_in_amount()

