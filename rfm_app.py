import streamlit as st
import pandas as pd

# Load the rfm_values DataFrame from the CSV file
rfm_values = pd.read_csv("rfm_values.csv")

# Streamlit app
st.title("Personalized Offer Recommendations")

# Dropdown to select CustomerID
customer_ids = rfm_values['CustomerID'].unique()
selected_id = st.selectbox("Select a Customer ID", customer_ids)

# Fetching customer data
customer_data = rfm_values[rfm_values['CustomerID'] == selected_id]

if not customer_data.empty:
    # Display customer information
    st.write(f"**Customer ID:** {customer_data['CustomerID'].values[0]}")

    # Get the row with the highest RFM Score
    best_offer = customer_data.loc[customer_data['RFM_Score'].idxmax()]

    # Display the best recommendation
    st.write(f"**Best RFM Score:** {best_offer['RFM_Score']}")
    st.write(f"**Recommended Category:** {best_offer['Category']}")
    st.write(f"**Recommended Merchant:** {best_offer['MerchantName']}")
else:
    st.write("No data available for the selected Customer ID.")
