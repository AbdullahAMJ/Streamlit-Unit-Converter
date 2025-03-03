# Unit Converter

## Overview

This **Unit Converter** is a simple web application built using **Streamlit** that allows users to convert between different units of length measurements.

## Features

- User-friendly interface
- Supports various length units including:
  - Metre
  - Centimetre
  - Kilometre
  - Millimetre
  - Inch
  - Foot
  - Yard
  - Mile
- Real-time conversion based on user input
- Formula display to help users understand the conversion process

## Benefits

- Easy to use without any prior technical knowledge
- Quick and accurate conversions
- Lightweight application with fast performance
- Cross-platform compatibility
- Open-source and customizable

## Usage

1. Run the application:

```bash
streamlit run app.py
```

2. Enter the length value you want to convert.
3. Select the unit to convert from and the unit to convert to.
4. View the result and the conversion formula displayed on the screen.

## Conversion Formula

The conversion is based on the following formula:

```
Result = Input Value * (Converted to / Converted from)
```

## Example

If you want to convert **1 Metre** to **Centimetre**, the result will be:

```
1 Metre = 100.00 Centimetre
```

## Technologies Used

- Python
- Streamlit

