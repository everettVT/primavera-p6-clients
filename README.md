# Primavera P6 API Clients

This repository contains automatically generated API clients for Oracle's Primavera P6 EPPM REST API. These clients are generated using OpenAPI Generator from Oracle's official API specification.

## Overview

The clients provide programmatic access to Primavera P6's REST API endpoints, allowing developers to interact with:
- Projects and EPS
- Activities and WBS
- Resources and Assignments
- Calendars
- Cost Accounts
- And many other P6 entities

## Getting Started

### Prerequisites

- Node.js (for running the generator)
- Python 3.7+ (for using the Python client)
- Git (for installation from GitHub)

### Installation

There are several ways to install the client:

#### Install from GitHub
```bash
pip install git+https://github.com/yourusername/primavera-p6-clients.git#subdirectory=python
```

#### Install from Local Source
1. Clone the repository:
```bash
git clone https://github.com/yourusername/primavera-p6-clients.git
cd primavera-p6-clients/python
```

2. Install in editable mode:
```bash
pip install -e .
```

#### Build and Install from Local Distribution
1. Clone the repository:
```bash
git clone https://github.com/yourusername/primavera-p6-clients.git
cd primavera-p6-clients/python
```

2. Build the package:
```bash
python setup.py sdist bdist_wheel
```

3. Install the built package:
```bash
pip install dist/primavera_p6_client-*.whl
```

### Generating the Clients

If you want to regenerate the clients yourself:

1. Install the OpenAPI Generator CLI:
```bash
npm install @openapitools/openapi-generator-cli
```

2. Generate the client:
```bash
npx @openapitools/openapi-generator-cli generate \
  -i PrimaveraP6EPPMOpenAPIv3.json \
  -g python \
  -o /tmp/ \
  --skip-validate-spec
```

[Rest of README remains the same...]

## Usage Example

```python
from primavera_p6_client import Configuration, ApiClient, ProjectApi

# Configure API client
configuration = Configuration(
    host="https://your-p6-server/p6/rest/v1",
    username="your_username",
    password="your_password"
)

# Create an instance of the API class
api_client = ApiClient(configuration)
project_api = ProjectApi(api_client)

# Get all projects
try:
    projects = project_api.get_projects()
    for project in projects:
        print(f"Project ID: {project.id}, Name: {project.name}")
except Exception as e:
    print(f"Exception when calling ProjectApi: {e}")
```

## API Specification Source

The API clients are generated from Oracle's Primavera P6 REST API specification. The OpenAPI/Swagger specification was obtained from:

1. Oracle's P6 REST API documentation at [docs.oracle.com](https://docs.oracle.com/cd/F37125_01/English/Integration_Documentation/rest_api/api-activity.html)
2. The complete API documentation is available in the [P6 EPPM Help Documentation](https://docs.oracle.com/cd/F37125_01/helpmain.htm?toc.htm?55497.htm)

## Client Generation Process

The clients are generated using [OpenAPI Generator](https://openapi-generator.tech/), following these steps:

1. Extract the OpenAPI specification from Oracle's documentation
2. Clean up and validate the specification
3. Generate the client using OpenAPI Generator
4. Package and distribute the generated client

For more information about OpenAPI client generation, see:
- [FastAPI's Client Generation Guide](https://fastapi.tiangolo.com/advanced/generate-clients/)
- [OpenAPI Generator Documentation](https://openapi-generator.tech/docs/installation)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For issues related to:
- The generated client: Please open an issue in this repository
- The Primavera P6 API itself: Please refer to [Oracle Support](https://support.oracle.com)

## Disclaimer

This is not an official Oracle product. This project is community-maintained and is not supported by Oracle. All Oracle trademarks are property of their respective owners.