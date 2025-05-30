# pytests/test_errorsearch.py

import sys
import os
import pytest

# append path of parent directory (in order to find the module errorsearch)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))
from validations.errorsearch import CheckForErrors


def test_csv_loading():
    # Create instance without passing a path, should resolve correctly via __file__ logic
    checker = CheckForErrors(csv_filename="transactions_original.csv")

    # Assert that the dataframe is loaded and not empty
    assert checker.dataframe is not None, "DataFrame is None"
    assert not checker.dataframe.empty, "DataFrame is empty"
    assert 'transaction_id' in checker.dataframe.columns, "Expected column 'transaction_id' not found"
