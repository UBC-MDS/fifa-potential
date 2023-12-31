import pytest
import sklearn
import pandas as pd
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.preprocessor import preprocessor

# Create test data to test the function
test_data = pd.DataFrame({
    'num_col_1': [1, 2, 3, 4, 5],
    'num_col_2': [6, 7, 8, 9, 10],
    'pass_col_1': ['jake', 'merete', 'simon', 'waleed', 'tiffany'],
    'num_col_3': [100, 200, 300, 400, 500],
    'pass_col_2': ['abc', 'def', 'ghi', 'jkl', 'mno']
})

# Create passthrough_feats and numeric_feats
passthrough_feats = ['pass_col_1']
numeric_feats = ['num_col_1', 'num_col_2', 'num_col_3']


# Tests

# Test to make sure function returns an object
def test_create_columntransformer():
    passthrough_feats = ['pass_col_1']
    numeric_feats = ['num_col_1', 'num_col_2', 'num_col_3']
    fifa_preprocessor = preprocessor(passthrough_feats, numeric_feats)
    assert isinstance(fifa_preprocessor, sklearn.compose._column_transformer.ColumnTransformer)


# Test to make sure the lists being passed to the function contain strings
def test_preprocessor_non_numeric_numeric_feats():
    for element in numeric_feats:
        assert isinstance(element, str)
    for element in passthrough_feats:
        assert isinstance(element, str)


# Test to make sure the function throws an error for improper input type
def test_preprocessor_invalid_passthrough_feats():
    passthrough_feats2 = 'not_a_list'
    numeric_feats2 = ['num_col_1', 'num_col_2', 'num_col_3']
    try:
        preprocessor(passthrough_feats2, numeric_feats2)
    except TypeError as e:
        assert str(e) == 'passthrough_feats must be a list'