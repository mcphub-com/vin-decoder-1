markdown
# vin-decoder-1 MCP Server

## Overview

**vin-decoder-1** is a Multi-Channel Processing (MCP) server designed to decode Vehicle Identification Numbers (VIN) across North America, Asia, and Europe. It offers a comprehensive toolkit for decoding VINs and retrieving detailed vehicle specifications, including the ability to perform salvage title checks within North America.

### Key Features

- **Universal VIN Decoding**: Supports VIN decoding for vehicles in North America, with additional support for Asian and European vehicles currently in beta.
- **Motorcycle, Boat, and Bike Support**: Capable of decoding VINs for a variety of vehicle types, extending beyond standard automobiles.
- **Salvage Title Check**: Provides access to salvage title information and relevant images, enhancing transparency for North American vehicles.
- **Free Monthly Usage**: Offers 100 free API calls per month, making it accessible for low-volume users.

### Tools and Functionalities

1. **VIN Decoder**: Decodes any 17-character VIN to provide detailed vehicle specifications.
2. **Salvage Check**: Retrieves salvage information based on a VIN, useful for checking vehicle history and condition.
3. **VIN Decoder v1.1**: An incremental update to the standard decoder, adding fields for fuel type and drive type.
4. **USA Plate Number Lookup**: Allows users to input a plate number to retrieve the corresponding VIN.

### Tool Declarations

- **Decode VIN**: 
  - **Function**: `decode_vin`
  - **Description**: Get vehicle specifications by VIN number.
  - **Parameters**: 
    - `vin` (String): A 17-character VIN number.

- **Salvage Check**: 
  - **Function**: `salvage_check`
  - **Description**: Retrieve salvage information based on the VIN number.
  - **Parameters**: 
    - `vin` (String): The VIN number.

- **Decode VIN v1.1**: 
  - **Function**: `decode_vin_v11`
  - **Description**: An incremental update adding fields for fuel type and drive type.

- **USA Plate Number Lookup**: 
  - **Function**: `usaplate_number_lookup`
  - **Description**: Use this tool to look up a plate number and obtain the VIN number.

### Service Level and Performance

- **Popularity**: 9.9
- **Service Level**: 84%
- **Latency**: 531ms

vin-decoder-1 offers a versatile and efficient solution for individuals and businesses needing VIN decoding services, with robust support for various vehicle types and regions.