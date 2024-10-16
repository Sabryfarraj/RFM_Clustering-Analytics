import pandas as pd
import streamlit as st
import plotly.express as px

# Page config
st.set_page_config(
    page_title="Customer Recommendations",
    page_icon="🎯",
    layout="wide"
)

# Load data
@st.cache_data
def load_data():
    return pd.read_csv("rfm_values.csv")

df = load_data()

def get_personal_favorites(user_data):
    """Get customer's personal favorite merchant and category"""
    favorite_merchant = user_data.groupby("MerchantName")["TransactionValue"].sum().nlargest(1)
    favorite_category = user_data.groupby("Category")["TransactionValue"].sum().nlargest(1)
    
    return {
        'merchant': favorite_merchant.index[0],
        'merchant_spend': favorite_merchant.values[0],
        'category': favorite_category.index[0],
        'category_spend': favorite_category.values[0]
    }

def get_recommendations(user, num_of_recom):
    try:
        user_id = int(user)
        
        if user_id not in df['CustomerID'].values:
            st.error(f"Customer ID {user_id} not found in our database.")
            return
        
        # Get user's data and cluster
        user_data = df[df["CustomerID"] == user_id]
        cluster = user_data["Cluster"].unique()[0]
        df_cluster = df[df["Cluster"] == cluster]
        
        # Get personal favorites
        favorites = get_personal_favorites(user_data)
        
        # Display personal insights
        st.markdown("### 👤 Customer Profile")
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown(
                f"""
                <div style='
                    padding: 20px;
                    background-color: #262730;
                    border-radius: 5px;
                    border: 1px solid #444;
                '>
                    <h4 style='color: #fff; margin: 0;'>Favorite Merchant</h4>
                    <p style='color: #FF4B4B; font-size: 20px; margin: 10px 0;'>{favorites['merchant']}</p>
                    <p style='color: #aaa; margin: 0;'>Total Spent: ${favorites['merchant_spend']:,.2f}</p>
                </div>
                """,
                unsafe_allow_html=True
            )
            
        with col2:
            st.markdown(
                f"""
                <div style='
                    padding: 20px;
                    background-color: #262730;
                    border-radius: 5px;
                    border: 1px solid #444;
                '>
                    <h4 style='color: #fff; margin: 0;'>Favorite Category</h4>
                    <p style='color: #FF4B4B; font-size: 20px; margin: 10px 0;'>{favorites['category']}</p>
                    <p style='color: #aaa; margin: 0;'>Total Spent: ${favorites['category_spend']:,.2f}</p>
                </div>
                """,
                unsafe_allow_html=True
            )
        
        # Get and display cluster-based recommendations
        st.markdown("### 🎯 Recommended Merchants")
        st.markdown(f"Based on similar customers in Cluster {cluster}")
        
        top_merchants = df_cluster.groupby("MerchantName")["TransactionValue"].sum().nlargest(num_of_recom)
        
        for i, (merchant, value) in enumerate(top_merchants.items(), 1):
            highlight = merchant == favorites['merchant']
            st.markdown(
                f"""
                <div style='
                    padding: 15px;
                    background-color: {'#3B3B3B' if highlight else '#262730'};
                    border-radius: 5px;
                    margin: 10px 0;
                    border: {'2px solid #FF4B4B' if highlight else '1px solid #444'};
                '>
                    <h4 style='color: #fff; margin: 0;'>#{i} {merchant} {' ⭐' if highlight else ''}</h4>
                    <p style='color: #aaa; margin: 5px 0 0 0;'>Cluster spending: ${value:,.2f}</p>
                    {f"<p style='color: #FF4B4B; margin: 5px 0 0 0;'>Your favorite merchant!</p>" if highlight else ""}
                </div>
                """,
                unsafe_allow_html=True
            )
        
        # Display category distribution
        st.markdown("### 📊 Spending Distribution")
        user_categories = user_data.groupby("Category")["TransactionValue"].sum().reset_index()
        user_categories = user_categories.sort_values("TransactionValue", ascending=True)
        
        fig = px.bar(
            user_categories,
            x="TransactionValue",
            y="Category",
            orientation='h',
            title=f'Personal Spending Distribution',
            labels={'TransactionValue': 'Total Spending ($)', 'Category': 'Merchant Category'}
        )
        fig.update_traces(marker_color='#FF4B4B')
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font_color='white'
        )
        st.plotly_chart(fig, use_container_width=True)
        
    except ValueError:
        st.error("Please enter a valid Customer ID (numbers only)")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

def main():
    st.title("🎯 Customer Recommendations")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        user = st.text_input("Customer ID", placeholder="Enter customer ID...")
    with col2:
        num_of_recom = st.selectbox(
            "Number of recommendations",
            options=list(range(1, 10)),
            index=4
        )
    
    if st.button("Get Recommendations"):
        if user:
            get_recommendations(user, num_of_recom)
        else:
            st.warning("Please enter a Customer ID")

if __name__ == "__main__":
    main()
