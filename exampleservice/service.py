"""
Exampleservice to demonstrate the usage of `sbwoaservices`.

This `exampleservice.service`-module loads the blueprints defined in the
`exampleservice.blueprints`-module to serve the api-endpoints of the service.
The options for the service are combined by the servicerules as defined in the
`exampleservice.rules` module and the arguments passed to the service as
defined by the `exampleservice.options`-module.

These settings aare used to run the service.
"""

from typing import NoReturn

from scwoaservices.options import create_base_options

from exampleservice.options import create_service_options
from exampleservice.rules import SERVICERULES
from exampleservice.blueprints.example_api import BLUEPRINT as api_example

__version__ = SERVICERULES.version


def run_service() -> NoReturn:
    """
    Runs the service with the api-endpoints to serve and the options as defined
    in the service-rules and passed as arguments to the service.
    """
    # load the api-endpoints as defined in the blueprints
    SERVICERULES.app.blueprint(api_example)

    # load the options passed to the service, like the port, the mode, etc.
    options = create_base_options(parser=create_service_options())
    host = options.hostname or SERVICERULES.host
    port = options.port or SERVICERULES.port
    debug = options.debugmode or SERVICERULES.debug
    workers = options.workers or SERVICERULES.workers
    mode = options.mode

    # reconfigure the host-port-information of the service
    SERVICERULES.reconfig(host=host, port=port, mode=mode)

    # run the service
    SERVICERULES.app.run(host=host, port=port, debug=debug, workers=workers)


if __name__ == "__main__":
    run_service()
