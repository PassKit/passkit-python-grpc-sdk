# PassKit Python gRPC SDK

[![PyPI](https://img.shields.io/pypi/v/passkit-python-grpc-sdk.svg)](https://pypi.org/project/passkit-python-grpc-sdk/)
[![Python](https://img.shields.io/pypi/pyversions/passkit-python-grpc-sdk.svg)](https://pypi.org/project/passkit-python-grpc-sdk/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Generated Python clients and message types for the PassKit gRPC API. Use the
SDK to build integrations for membership and loyalty cards, coupons, event
tickets, boarding passes, and the other PassKit services.

## Requirements

- Python 3.9 or newer
- A PassKit account and API credentials for live API calls

## Install

```bash
python -m pip install passkit-python-grpc-sdk
```

Pin a specific release when reproducible installs are important:

```bash
python -m pip install passkit-python-grpc-sdk==1.1.162
```

The package installs the compatible gRPC, Protocol Buffers, Google API
annotations, and OpenAPI annotation runtimes automatically.

## Use the SDK

Import the generated messages and service stubs for the PassKit product you
want to use:

```python
import grpc

from passkit.io.common.common_objects_pb2 import Id
from passkit.io.member.a_rpc_pb2_grpc import MembersStub

with open("certs/ca-chain.pem", "rb") as file:
    root_certificate = file.read()
with open("certs/key.pem", "rb") as file:
    private_key = file.read()
with open("certs/certificate.pem", "rb") as file:
    certificate_chain = file.read()

credentials = grpc.ssl_channel_credentials(
    root_certificates=root_certificate,
    private_key=private_key,
    certificate_chain=certificate_chain,
)
channel = grpc.secure_channel(
    "grpc.pub1.passkit.io:443",
    credentials,
)
members = MembersStub(channel)

program = members.getProgram(Id(id="YOUR_PROGRAM_ID"))
print(program)
```

For complete credential setup and runnable membership, coupon, event-ticket,
and flight examples, see the
[PassKit Python quickstart](https://github.com/PassKit/passkit-python-quickstart).

## Main modules

- `passkit.io.member`
- `passkit.io.single_use_coupons`
- `passkit.io.event_tickets`
- `passkit.io.flights`
- `passkit.io.core`
- `passkit.io.analytics`
- `passkit.io.scheduler`
- `passkit.io.raw`

The generated method names intentionally match the PassKit API definitions.

## Development

```bash
python -m pip install -e ".[dev]"
python -m unittest discover -s tests -v
python -m build
python -m twine check dist/*
```

## Documentation and support

- [PassKit API documentation](https://docs.passkit.io/)
- [PassKit Help Centre](https://help.passkit.com/)
- [Open an SDK issue](https://github.com/PassKit/passkit-python-grpc-sdk/issues)
- Email [support@passkit.com](mailto:support@passkit.com)

## Licence

Distributed under the [MIT Licence](LICENSE).
