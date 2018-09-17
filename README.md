# Graviton

## Purpose

Graviton is a pure-python, pulse-based pipeline scheduler for querying Rest APIs into generic persistent storage solutions. For its initial major release, the goal will be targeted purely at Sqlite pipelines using pandas DataFrames.

## Usage

## ToDo

1. Decouple Api from ApiImp using a Bridge pattern.
2. Configure concrete Endpoints for BittrexEndpointBuilder.
3. Build Endpoint and EndpointBuilder from config.
4. Build abstract ApiFactory and BittrexKit to bundle Bittrex requirements.
