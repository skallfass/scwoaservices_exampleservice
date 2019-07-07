"""
This is an example how to implement an API inside the scwoaservice-structure.
"""

from sanic.blueprints import Blueprint
from sanic.log import logger
from sanic.request import Request
from sanic.response import HTTPResponse

from scwoaservices.decorators import api_documentation
from scwoaservices.decorators import api_inputmodel
from scwoaservices.decorators import api_outputmodel

from exampleservice.models.example_api import InputModel
from exampleservice.models.example_api import OutputModel
from exampleservice.processing.example_api import example_logic
from exampleservice.rules import SERVICERULES

NAME = 'Example'
API = '/example'
BLUEPRINT = Blueprint(NAME, API)


@BLUEPRINT.post('', strict_slashes=True)
@api_documentation(api=API, summary='example api', in_model=InputModel,
                   out_model=OutputModel,
                   out_description='the output for the example request.')
@api_inputmodel(api=API, model=InputModel,
                servicename=SERVICERULES.servicename, service_logger=logger)
@api_outputmodel(api=API, model=OutputModel,
                 servicename=SERVICERULES.servicename, service_logger=logger)
async def api_example(request: Request, service_params: InputModel,
                      service_logger: logger) -> HTTPResponse:
    """
    Example api to demonstrate the usage of sanic combined with pydantic.

    # Parameters
        request (Request): the request-object containing all informations
            concerning the made request to this api.
            Modified with the additional key `input_data` containing the
            transformed request-params as an instance of the
            `InputModelExample`.
        service_params (InputModelExample): the transformed request-data as an
            instance of `InputModelExample`.

    # Returns
        result (OutputModelExample): the processed result for this example api
            as an instance of `OutputModelExample`.
    """
    service_logger.info(f'processing request {request} with {service_params}')
    return await example_logic(service_params)


__all__ = [
    'BLUEPRINT',
]
