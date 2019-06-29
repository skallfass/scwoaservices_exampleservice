"""
Example to demonstrate the usage of the `sbwoaservices.rules`-module in
your own services.

These rules contain all service-specific rules like the port, the runtime-mode,
but also contains rules required for processing-logics of the apis.
"""

from pathlib import Path

from scwoaservices.rules import BaseServiceRules

SERVICERULES = BaseServiceRules(
    servicename='exampleservice',
    host='0.0.0.0',
    port=50004,
    debug=False,
    workers=1,
    title='exampleservice',
    description=Path('exampleservice/README.md').read_text(),
    contact_email='skallfass@ouroboros.info',
    mode='devl')
