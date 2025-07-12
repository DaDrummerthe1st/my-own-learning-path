import pandas as pd
import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))

file = "../data/transactions_original.csv"

df_transactions = pd.read_csv(file)
# display(df_transactions.head())
# print(df_transactions.dtypes)

# print(df_transactions.columns)

def check_this_out(name, cell, type):
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

# pytests:
# print(check_this_out("amount", "1. 0", "fl")) # ["In amount, exception: could not convert string to float: '1. 0'"]
# print(check_this_out("amount", "1.0", "fl")) # None
# print(type(check_this_out("amount", "1. 0", "fl"))) # <class 'list'>
# print(type(check_this_out("amount", "1.0", "fl"))) # <class 'NoneType'>

def first_check(dataframe):
    # starting two new dfs from dataframe
    # df_incorrect = dataframe[df_transactions.isna().any(axis=1)]
    # df_remaining = dataframe[df_transactions.notna().any(axis=1)]
    # display(df_incorrect.head())
    # display(df_remaining.head())

    # searching for the rest of the errors
    for idx, row in dataframe.iterrows():
        error_messages = []
        print(row)
    #     # print(row.index) # headline
    #     # print(type(row)) # value
        for index_n, indexname in enumerate(row.index):
            print("onefucking run")
            match row.index[index_n]:
                case "timestamp":
                    if check_this_out(row.index[index_n], row[indexname], "dt"):
                        error_messages.append(check_this_out(row.index[index_n], row[indexname], "dt"))
                case "amount":
                    if check_this_out(row.index[index_n], row[indexname], "fl"):
                        error_messages.append(check_this_out(row.index[index_n], row[indexname], "fl"))
                # case "transaction_id" | "currency" | "sender_account" | "receiver_account" | "sender_country" | "sender_municipality" | "receiver_country" | "receiver_municipality" | "transaction_type" | "notes":
                #     if check_this_out(row.index[index_n], row[indexname], "st"):
                #         error_messages.append(check_this_out(row.index[index_n], row[indexname], "st"))
                # case "transaction_id":
                #     if check_this_out(row.index[index_n], row[indexname], "st"):
                #         error_messages.append(check_this_out(row.index[index_n], row[indexname], "st"))
                # case "sender_account":
                #     if check_this_out(row.index[index_n], row[indexname], "fl"):
                #         error_messages.append(check_this_out(row.index[index_n], row[indexname], "st"))
                # case "receiver_account":
                #     if check_this_out(row.index[index_n], row[indexname], "fl"):
                #         error_messages.append(check_this_out(row.index[index_n], row[indexname], "st"))
                # case "sender_country":
                #     if check_this_out(row.index[index_n], row[indexname], "fl"):
                #         error_messages.append(check_this_out(row.index[index_n], row[indexname], "st"))
                # case "sender_municipality":
                #     if check_this_out(row.index[index_n], row[indexname], "fl"):
                #         error_messages.append(check_this_out(row.index[index_n], row[indexname], "st"))
                # case "receiver_country":
                #     if check_this_out(row.index[index_n], row[indexname], "fl"):
                #         error_messages.append(check_this_out(row.index[index_n], row[indexname], "st"))
                # case "receiver_municipality":
                #     if check_this_out(row.index[index_n], row[indexname], "fl"):
                #         error_messages.append(check_this_out(row.index[index_n], row[indexname], "st"))
                # case "transaction_type":
                #     if check_this_out(row.index[index_n], row[indexname], "fl"):
                #         error_messages.append(check_this_out(row.index[index_n], row[indexname], "st"))
                # case "notes":
                #     if check_this_out(row.index[index_n], row[indexname], "fl"):
                #         error_messages.append(check_this_out(row.index[index_n], row[indexname], "st"))

                # case _:
                #     print(f"trying to reach a column that doesn't exist: {row.index[index_n]}")
        # if idx >= 0:
        #    return
        
        # where there any faults discovered?
        # print(len(error_messages))
        if len(error_messages) > 0:
            # there were errors
            print(f"error_message contains {error_messages}")
        else:
            return
            # no errors
            print(f"error_messages empty, however: {error_messages}")

first_check(df_transactions)