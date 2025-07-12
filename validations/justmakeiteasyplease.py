import pandas as pd

# https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
pd.options.mode.copy_on_write = True

# file = ("./data/transactions_original.csv")

# df_transactions = pd.read_csv(file)

class ErrorSearch:
    def __init__(self, csv):
        self.csv_path = f"./data/{csv}"
        self.df_transactions = pd.read_csv(self.csv_path)

        self.start_checkups(self.df_transactions)

    def check_this_out(self, name, cell, type):
        error_messages = []
        match type:
            case "st": # string-test
                try:
                    str(cell)
                except Exception as e:
                    error_messages.append(f"In {name}, exception: {e}")
        
            case "dt": # datetime-test
                try:
                    pd.to_datetime(cell)
                except Exception as e:
                    error_messages.append(f"In {name}, exception: {e}")

            case "fl": # float-test
                try:
                    float(cell)
                except Exception as e:
                    error_messages.append(f"In {name}, exception: {e}")
            case _:
                return

        if error_messages == []:
            return
        else:
            # print(f"error_messages should not be empty inside here: {error_messages}")
            return error_messages
        
    def start_checkups(self, dataframe):
        # starting two new dfs from dataframe
        df_incorrect = dataframe[dataframe.isna().any(axis=1)]
        df_incorrect["error_messages"] = "there are empty cells"
        # print(df_incorrect.head())    

        df_remaining = dataframe[~dataframe.isna().any(axis=1)]
        # print(df_remaining.head())

        # searching for the rest of the errors
        for idx, row in df_remaining.iterrows():
            error_messages = []

            # # to be able to pop the current row
            # row_index = row.index
            # print(row_index)

            for index_n, indexname in enumerate(row.index):
                match row.index[index_n]:
                    case "timestamp":
                        if self.check_this_out(row.index[index_n], row[indexname], "dt"):
                            error_messages.append(self.check_this_out(row.index[index_n], row[indexname], "dt"))
                            print("timestamp")
                    case "amount":
                        if self.check_this_out(row.index[index_n], row[indexname], "fl"):
                            error_messages.append(self.check_this_out(row.index[index_n], row[indexname], "fl"))
                            print("amount")
                    case "transaction_id" | "currency" | "sender_account" | "receiver_account" | "sender_country" | "sender_municipality" | "receiver_country" | "receiver_municipality" | "transaction_type" | "notes":
                        if self.check_this_out(row.index[index_n], row[indexname], "st"):
                            error_messages.append(self.check_this_out(row.index[index_n], row[indexname], "st"))
                
                # where there any faults discovered?
                # print(len(error_messages))
                if len(error_messages) > 0:
                    # there were errors
                    print(idx)
                    # df_remaining[df_remaining['transactoin_id'] == row['transaction_id']].index[0]
                    # print(f"error_message contains {error_messages}")
                    # print(f"{row} and also {error_messages}")
                    # df_new_row = pd.Series(row)
                # else:
                    # # no errors
                    # print(f"error_messages empty, however: {error_messages}")

run = ErrorSearch("transactions_original.csv")