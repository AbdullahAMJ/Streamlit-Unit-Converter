import streamlit as st

def length_conversion(value, from_unit, to_unit):
    length_units = {
        "Meters": 1,
        "Kilometers": 0.001,
        "Centimeters": 100,
        "Millimeters": 1000,
        "Inches": 39.3701,
        "Feet": 3.28084,
        "Yards": 1.09361,
        "Miles": 0.000621371
    }
    
    return value * (length_units[to_unit] / length_units[from_unit])

def weight_conversion(value, from_unit, to_unit):
    weight_units = {
        "Grams": 1,
        "Kilograms": 0.001,
        "Pounds": 0.00220462,
        "Ounces": 0.035274
    }
    
    return value * (weight_units[to_unit] / weight_units[from_unit])

def temperature_conversion(value, from_unit, to_unit):
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5/9
    elif from_unit == "Celsius" and to_unit == "Kelvin":
        return value + 273.15
    elif from_unit == "Kelvin" and to_unit == "Celsius":
        return value - 273.15
    elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
        return (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
        return (value - 273.15) * 9/5 + 32
    return value  

st.title("🧮 Unit Converter")
st.write("Convert between different units easily!")

conversion_type = st.selectbox("Select Conversion Type", ["Length", "Weight", "Temperature"])

if conversion_type == "Length":
    units = ["Meters", "Kilometers", "Centimeters", "Millimeters", "Inches", "Feet", "Yards", "Miles"]
    convert_function = length_conversion
elif conversion_type == "Weight":
    units = ["Grams", "Kilograms", "Pounds", "Ounces"]
    convert_function = weight_conversion
elif conversion_type == "Temperature":
    units = ["Celsius", "Fahrenheit", "Kelvin"]
    convert_function = temperature_conversion

value = st.number_input("Enter Value", min_value=0.0, step=0.01)
from_unit = st.selectbox("From Unit", units)
to_unit = st.selectbox("To Unit", units)

if st.button("Convert"):
    result = convert_function(value, from_unit, to_unit)
    st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")
