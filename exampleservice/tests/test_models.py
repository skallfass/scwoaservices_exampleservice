"""
Tests the input- and output-models of the apis of the exampleservice.
"""

import json

import pytest
from pydantic import ValidationError

from exampleservice.models.example_api import InputModel
from exampleservice.models.example_api import OutputModel


def test_input_loading_ok():
    """
    Tests if loading of json-string with correct data with the `InputModel`
    works as expected.
    """
    input_data = dict(param='test')
    input_json = json.dumps(input_data)
    input_model = InputModel.parse_raw(input_json)
    assert input_model.param


def test_input_loading_fails():
    """
    Tests if the loading of json-string with missing data raises a
    `ValidationError` as expected when using the `InputModel`.
    """
    input_data = dict(bla=1)
    input_json = json.dumps(input_data)
    with pytest.raises(ValidationError):
        InputModel.parse_raw(input_json)
