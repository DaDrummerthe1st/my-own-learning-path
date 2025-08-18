import time

start_time = time.time()

# import logging
# import sqlite3

import pandas as pd
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
from functools import partial

# def main():
#     logging.basicConfig(filename="")

class TransactionValidator:
    def __init__(self, df):
        self.df = df
        self.error_builder = pd.DataFrame(columns=list(df.columns) + ['error_messages', 'suggested_change'])
        self.run_builder = pd.DataFrame(columns=df.columns)

    def is_valid_iban(self, iban):
        return isinstance(iban, str) and iban.startswith('SE') and len(iban) == 24

    def is_valid_amount(self, amount):
        try:
            float(str(amount).replace(' ', ''))
            return True
        except (ValueError, TypeError):
            return False

    def is_valid_timestamp(self, ts):
        try:
            datetime.strptime(ts, '%Y-%m-%d %H:%M:%S')
            return True
        except (ValueError, TypeError):
            return False

    def validate_row(self, idx, row):
        errors = []
        suggested_changes = {}
        is_valid = True

        for col in self.df.columns:
            if col != 'notes' and pd.isna(row[col]):
                errors.append(f"{col} cannot be NaN/None")
                suggested_changes[col] = "[Provide valid value]"
                is_valid = False

        if not self.is_valid_amount(row['amount']):
            errors.append("amount must be a valid number")
            suggested_changes['amount'] = "[Provide valid number]"
            is_valid = False

        if not self.is_valid_timestamp(row['timestamp']):
            errors.append("timestamp must be in 'YYYY-MM-DD HH:MM:SS' format")
            suggested_changes['timestamp'] = "[Provide valid timestamp]"
            is_valid = False

        for acc_col in ['sender_account', 'receiver_account']:
            if not self.is_valid_iban(row[acc_col]):
                errors.append(f"{acc_col} must be a valid Swedish IBAN")
                suggested_changes[acc_col] = "[Provide valid SE IBAN]"
                is_valid = False

        if row['transaction_type'] not in ['incoming', 'outgoing']:
            errors.append("transaction_type must be 'incoming' or 'outgoing'")
            suggested_changes['transaction_type'] = "[Provide 'incoming' or 'outgoing']"
            is_valid = False

        return idx, row, errors, suggested_changes, is_valid

    def process_chunk(self, chunk):
        local_errors = []
        local_valid = []

        for idx, row in chunk.iterrows():
            idx, row, errors, suggested_changes, is_valid = self.validate_row(idx, row)

            if not is_valid:
                error_row = row.to_dict()
                error_row['error_messages'] = errors
                error_row['suggested_change'] = suggested_changes
                local_errors.append(error_row)
            else:
                local_valid.append(row.to_dict())

        #print(f"Processed chunk {chunk_number + 1} (rows {chunk_number * 10 + 1}-{(chunk_number + 1) * 10})")
        return local_errors, local_valid

    def run_validation(self, num_threads=4):
        chunks = [self.df[i:i+10] for i in range(0, self.df.shape[0], 10)]

        with ThreadPoolExecutor(max_workers=num_threads) as executor:
            results = list(executor.map(self.process_chunk, chunks))

        for local_errors, local_valid in results:
            self.error_builder = pd.concat([self.error_builder, pd.DataFrame(local_errors)], ignore_index=True)
            self.run_builder = pd.concat([self.run_builder, pd.DataFrame(local_valid)], ignore_index=True)

        self.run_builder['amount'] = self.run_builder['amount'].apply(lambda x: float(str(x).replace(' ', '')))
        self.run_builder['timestamp'] = pd.to_datetime(self.run_builder['timestamp'], errors='coerce')

        return self.error_builder, self.run_builder

# Example usage
df = pd.read_csv('../data/transactions_original.csv')
validator = TransactionValidator(df)
error_builder, run_builder = validator.run_validation()

print("Error Builder:")
print(error_builder.head())
print("\nRun Builder:")
print(run_builder.head())

# create new csv-files
path_to_runs = "../data/runs/"
error_builder_csv_filename = f"{path_to_runs}error_builder{time.time()}.csv"
run_builder_csv_filename = f"{path_to_runs}run_builder{time.time()}.csv"

try:
    error_builder.to_csv(error_builder_csv_filename, encoding="utf-8", index=False, header=True)
except (FileExistsError):
    print(f"{error_builder_csv_filename} already exist, but shouldn't")

try:
    run_builder.to_csv(run_builder_csv_filename, encoding="utf-8", index=False, header=True)
except (FileExistsError):
    print(f"{run_builder_csv_filename} already exist, but shouldn't")

(f"total elapsed time: {time.time() - start_time} seconds")

# if __name__ == '__main__':
#     main()

