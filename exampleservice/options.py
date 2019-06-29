"""
An example based on scwoaservices defines additional service-options inside
this module in the `create_service_options`-function.
Additional service-parameters and flags should be defined inside this function
using either the `scwoaservices.options.add_flag` or
`scwoaservices.options.add_param` function.
"""

from argparse import ArgumentParser


def create_service_options() -> ArgumentParser:
    """
    Example how to define additional service-options for a service.
    """
    parser = ArgumentParser()
    return parser
