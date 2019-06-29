"""
This module includes all pydantic-models used for the input- and
output-transformations of the apis of the service.
"""

from pydantic import BaseModel


class InputModel(BaseModel):
    """
    Model used for the input-transformation of the api-endpoint `/example`.
    """
    param: str


class OutputModel(BaseModel):
    """
    Model used for the output-transformation of the api-endpoint `/example`.
    """
    message: str
