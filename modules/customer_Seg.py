import streamlit as st
import pandas as pd
import plotly.express as px

# Load the data
df = pd.read_excel("C:/Users/Shankar Karande/OneDrive/Desktop/Final Year Project/Import csv/Online Retail.xlsx")

# Preprocess the data and perform customer segmentation
# Ensure to include the necessary preprocessing and segmentation code here

# Define the function to visualize similar purchasing behavior
def visualize_similar_purchasing_behavior(df_customers):
    fig = px.scatter(df_customers, x='Frequency', y='MonetaryValue', color='Recency', 
                     title='Similar Purchasing Behavior', labels={'Frequency': 'Frequency', 
                                                                  'MonetaryValue': 'Monetary Value',
                                                                  'Recency': 'Recency'})
    fig.update_traces(marker=dict(size=12,
                                  line=dict(width=2,
                                            color='DarkSlateGrey')),
                      selector=dict(mode='markers'))
    fig.update_layout(legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01))
    st.plotly_chart(fig)

# Create the Streamlit app
def main():
    st.title('Customer Segmentation App')

    # Dropdown for selecting options
    option = st.selectbox('Select an option:', ['Similar purchasing behavior'])

    if option == 'Similar purchasing behavior':
        st.header('Similar Purchasing Behavior Visualization')
        # This is where you would define df_customers
        # For the sake of example, let's assume df_customers is already defined
        # df_customers = perform_customer_segmentation(df)
        visualize_similar_purchasing_behavior(df_customers)

if __name__ == '__main__':
    main()
