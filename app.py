import streamlit as st

st.title("Unit Converter")
st.selectbox("Select Unit Measurement",["Length"])
unit_options = ["Metre", "Centimetre", "Kilometre", "Millimetre", "Inch", "Foot", "Yard", "Mile"]

value = st.number_input("Enter Length Value", min_value = 0.0, step = 0.1)
from_unit = st.selectbox("From Unit", unit_options)
to_unit = st.selectbox("To Unit", unit_options)

conversion_dict = {"Metre": 1, "Centimetre": 100, "Kilometre": 0.001, "Millimetre": 1000, "Inch": 39.3701, "Foot": 3.28084, "Yard": 1.09361, "Mile": 0.000621371}

if from_unit in conversion_dict and to_unit in conversion_dict:
    result = value * (conversion_dict[to_unit] / conversion_dict[from_unit])
    st.write(f"### {value} {from_unit} = {result:.2f} {to_unit}")

st.warning(f"Formula: multiply the length value by {conversion_dict[to_unit]}")