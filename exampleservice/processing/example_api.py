"""
This is a simple example for the logic-part of an API of a scwoaservice.
"""

from exampleservice.models.example_api import InputModel
from exampleservice.models.example_api import OutputModel


async def example_logic(params: InputModel) -> OutputModel:
    """
    creates the "processed" result and returns the "calculated" result as an
    instance of the `OutputModel`. In a real API this logic would be more
    complex.

    # Parameters
        params (InputModel): the request-data as an instance of the
            `InputModel`.

    # Returns
        result (OutputModel): the final result of the api-logic.
    """
    result_data = dict(message=params.param)
    result = OutputModel(**result_data)
    return result
