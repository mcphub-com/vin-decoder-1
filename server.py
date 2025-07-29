import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/vinfreecheck/api/vin-decoder-1'

mcp = FastMCP('vin-decoder-1')

@mcp.tool()
def decode_vin(vin: Annotated[str, Field(description='17 characters vin numbers')]) -> dict: 
    '''Get Vehicle Specification by VIN Number'''
    url = 'https://vindecoder.p.rapidapi.com/decode_vin'
    headers = {'x-rapidapi-host': 'vindecoder.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'vin': vin,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def salvage_check(vin: Annotated[str, Field(description='vin number')]) -> dict: 
    '''Retrieve Salvage Information based on VIN Number'''
    url = 'https://vindecoder.p.rapidapi.com/salvage_check'
    headers = {'x-rapidapi-host': 'vindecoder.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'vin': vin,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def decode_vin_v11() -> dict: 
    '''Incremental update to the decoding vin api - two new field. fuel_type and drive_type'''
    url = 'https://vindecoder.p.rapidapi.com/v1.1/decode_vin'
    headers = {'x-rapidapi-host': 'vindecoder.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def usaplate_number_lookup(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''Use this api to lookup a Plate number - and get the VIN number'''
    url = 'https://vindecoder.p.rapidapi.com/api/v4/decode_plate'
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'x-rapidapi-host': 'vindecoder.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
