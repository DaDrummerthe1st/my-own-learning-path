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
        # attributes definitions
        self.csv_filename = csv_filename

        current_dir = os.path.dirname(os.path.abspath(__file__))
        csv_path = os.path.abspath(os.path.join(current_dir, '..', 'data', csv_filename))

        self.dataframe = pd.read_csv(csv_path)
        # self.dataframe = pd.read_csv("../data/transactions_original.csv")
        
        # self.dataframe = dataframe
        # self.run_all()

    def create_unique_run_id(self):
        """
        Creates a unique identifier for transaction rows

        note: microseconds (%f) has 6 (six) digits
        note: if server runs are faste than 8 per milliseconds then up the length-value
        """

        # get the timestamp
        now = datetime.now().strftime("%Y%m%d%H%M%S%f")
        
        # create a random strin for absolute uniqueness
        length = 8 # accepts <8 runs per microsecond
        random_string = ''.join(random.choices(
            string.ascii_uppercase + string.digits, k=length))
        
        f = now + random_string
        return f
    
    def input_unique_identifier(self):
        self.dataframe["run_id"] = self.create_unique_run_id()
        print(self.dataframe.head())

    # def run_all(self):
    #     for idx, row in self.dataframe.iterrows():


    # def whitespace_in_amount(self, idx, row):
    #     try:
    #         self.dataframe["amount"].astype(float)
    #         self.dataframe["amount"] = self.dataframe["amount"].astype(str)


new_run = CheckForErrors("transactions_original.csv")
new_run.input_unique_identifier()

