import streamlit as st 
import requests

st.title("Temperature Conversion App")

temperature = st.number_input("Enter temperature", step=1.0) 
unit = st.selectbox("Convert from", ["Celsius", "Fahrenheit"]) 

if st.button("Convert"):
    response = requests.post(
        "https://ff73-116-254-103-54.ngrok-free.app/convert",
        json={"temperature": temperature, "unit": unit}
    )

    if response.status_code == 200:

        result = response.json()
        st.success(f"{temperature} {unit} is {result['temperature']}{result['unit']}")
    else:
        st.error("Error in conversion")