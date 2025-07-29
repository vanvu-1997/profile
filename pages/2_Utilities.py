import streamlit as st
import pandas as pd

st.title("Utilities")
st.write("""
These lightweight tools were built to streamline quick data validations during analysis—no need to search online or open separate calculators. 
They help ensure accuracy and save time when double-checking common metrics like percent change.
""")

tab1, tab2 = st.tabs(["Percent Change Calculator", "Other Utilities"])

# Input values
with tab1: 
    try:
        initial_value = float(st.text_input("Enter initial value: ", value="1"))
    except ValueError:
        st.error("Please enter a valid number for the initial value.")
        initial_value = 1

    try:
        final_value = float(st.text_input("Enter final value: ", value="2"))
    except ValueError:
        st.error("Please enter a valid number for the final value.")
        final_value = 1

    # Calculate percent change
    try:
        if initial_value == 0:
            st.error("Initial value cannot be zero for percent change calculation.")
            percent_change = 0
        else:
            percent_change = (final_value - initial_value) / initial_value * 100
    except ZeroDivisionError:
        st.error("Error in calculation: Division by zero.")
        percent_change = 0

    # Output result
    st.write(f"Percent Change: {percent_change:.2f}%")

with tab2:
    st.write("This tab is reserved for additional utilities and features in the future to support daily analysis and automation.")