#!/bin/bash

# Install required npm package
echo "Installing OpenAPI Generator CLI..."
npm install @openapitools/openapi-generator-cli

# Generate the Python client
echo "Generating Python client..."
npx @openapitools/openapi-generator-cli generate \
  -i PrimaveraP6EPPMOpenAPIv3.json \
  -g python \
  -o /python/ \
  --skip-validate-spec

echo "Client generation complete!"