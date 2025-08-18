import pandas as pd
from datetime import datetime

# Load the CSV file
df = pd.read_csv('../data/transactions_original.csv')

# Initialize DataFrames
error_builder = pd.DataFrame(columns=list(df.columns) + ['error_messages', 'suggested_change'])
run_builder = pd.DataFrame(columns=df.columns)

# Iterate over each row
for idx, row in df.iterrows():
    errors = []
    suggested_changes = {}
    is_valid = True

    # Check for NaN/None in all columns except 'notes'
    for col in df.columns:
        if col != 'notes' and pd.isna(row[col]):
            errors.append(f"{col} cannot be NaN/None")
            suggested_changes[col] = "[Provide valid value]" # this might be overwritten if problems found later
            is_valid = False

    # Check amount format
    try:
        amount = float(str(row['amount']).replace(' ', ''))
    except (ValueError, TypeError):
        errors.append("amount must be a valid number")
        suggested_changes['amount'] = "[Provide valid number]"
        is_valid = False

    # Check timestamp format
    try:
        datetime.strptime(row['timestamp'], '%Y-%m-%d %H:%M:%S')
    except (ValueError, TypeError):
        errors.append("timestamp must be in 'YYYY-MM-DD HH:MM:SS' format")
        suggested_changes['timestamp'] = "[Provide valid timestamp]"
        is_valid = False

    # Check IBAN format for sender and receiver accounts
    for acc_col in ['sender_account', 'receiver_account']:
        if not (isinstance(row[acc_col], str) and row[acc_col].startswith('SE') and len(row[acc_col]) == 24):
            errors.append(f"{acc_col} must be a valid Swedish IBAN")
            suggested_changes[acc_col] = "[Provide valid SE IBAN]"
            is_valid = False

    # Check transaction_type
    if row['transaction_type'] not in ['incoming', 'outgoing']:
        errors.append("transaction_type must be 'incoming' or 'outgoing'")
        suggested_changes['transaction_type'] = "[Provide 'incoming' or 'outgoing']"
        is_valid = False

    # If errors found, add to error_builder, if not add to run_builder
    if not is_valid:
        error_row = row.to_dict()
        error_row['error_messages'] = errors
        error_row['suggested_change'] = suggested_changes
        error_builder = pd.concat([error_builder, pd.DataFrame([error_row])], ignore_index=True)
    else:
        run_builder = pd.concat([run_builder, row.to_frame().T], ignore_index=True)

# Convert amount to float and timestamp to datetime in run_builder
run_builder['amount'] = run_builder['amount'].apply(lambda x: float(str(x).replace(' ', '')))
run_builder['timestamp'] = pd.to_datetime(run_builder['timestamp'], errors='coerce')

# Display the first few rows of each DataFrame
print("Error Builder:")
print(error_builder.head())
print("\nRun Builder:")
print(run_builder.head())
