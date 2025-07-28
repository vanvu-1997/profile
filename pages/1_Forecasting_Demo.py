import streamlit as st
import pandas as pd
import altair as alt

# Load data
df = pd.read_csv('Data/forecast_df_demo.csv')
df['Date'] = pd.to_datetime(df['Date'])

# Page title and intro
st.title("📈 Rossmann Store Sales Forecast")

st.markdown("""
Welcome to the **Sales Forecasting Visualization Tool**.  
This dashboard uses historical data from the Rossmann Store dataset to predict future sales using a **Random Forest** model.

The model is trained on date-driven features to forecast daily sales for retail stores.  
You can explore actual vs. predicted values for a given time period to evaluate forecasting performance.
""")

# Layout: Filters on left (1/3), chart on right (2/3)
st.subheader("🗓️ Date Range Filter")
col1, col2 = st.columns([1, 2])

with col1:
    st.markdown("**Set your custom date range to visualize sales forecasts.**")
    initial_data = st.text_input("Start Date (YYYY-MM-DD):", value="2015-01-03")
    st.markdown("Data after **July 31, 2015** is forecasted based on the model.")
    end_data = st.text_input("End Date (YYYY-MM-DD):", value="2015-10-31")

    try:
        filtered_df = df[(df['Date'] >= initial_data) & (df['Date'] <= end_data)]
    except Exception:
        st.error("Please enter valid dates in the format YYYY-MM-DD.")
        filtered_df = df

with col2:
    st.markdown("### 📊 Forecast Chart")
    chart = alt.Chart(filtered_df).mark_line().encode(
        x=alt.X('Date:T', title='Date'),
        y=alt.Y('Sales:Q', title='Sales'),
        color=alt.Color('actual_vs_predicted:N', title='Legend')
    ).properties(
        width=550,
        height=350,
        title='Actual vs Predicted Sales Over Time'
    )
    st.altair_chart(chart, use_container_width=True)

# Optional: see raw data
with st.expander("🔍 View Full Dataset"):
    st.write("Explore the full dataset including actual and forecasted values.")
    st.dataframe(df)