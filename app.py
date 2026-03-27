import streamlit as st
import plotly.express as px
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

import plotly.graph_objects as go

# Function to display options based on selected operation
def display_options(operation):
    if operation == 'Market Basket Analysis':
        st.subheader('Select Operation')
        options = [
            'Number of Sales Weekly',
            'Number of Customers Weekly',
            'Sales per Customer Weekly',
            'Frequency of the Items Sold',
            'Top Customers regarding Number of Items bought',
            'Number of Sales per Discrete Week Days',
            'Number of Sales per Discrete Months',
            'Number of Sales per Discrete Month Days',  
            'Recency Distribution of the Customers',
            'Visit Frequency Distribution of the Customers',
            'Monetary Distribution of the Customers',
            'RFM Scores/RFM Segments',
            'Relationship between Visit_Frequency and Recency'
        ]
        selected_operation = st.selectbox('Select Operation', options)
        st.write('You selected:', selected_operation)

        # Load dataset
        data = pd.read_csv('.\Groceries_dataset.csv')
        data.columns = ['memberID', 'Date', 'itemName']
        data.memberID = data['memberID'].astype('str')
        data['Date'] = pd.to_datetime(data['Date'])


        # Lets Start with the calculate the Recency

        # Finding last purchase date of each customer
        Recency = data.groupby(by='memberID')['Date'].max().reset_index()
        Recency.columns = ['memberID', 'LastDate']
        Recency.head()

                # Finding last date for our dataset
        last_date_dataset = Recency['LastDate'].max()
        last_date_dataset

        # Lets Start with the calculate the Recency

        # Finding last purchase date of each customer

        # If the selected operation is 'Number of Sales Weekly'
        if selected_operation == 'Number of Sales Weekly':
            # Calculate number of sales weekly
            sales_weekly = data.resample('W', on='Date').size().reset_index(name='Number of Sales')

            # Plot the graph
            fig = px.line(sales_weekly, x='Date', y='Number of Sales', labels={'Number of Sales': 'Number of Sales Weekly'})
            st.plotly_chart(fig)

        # If the selected operation is 'Number of Customers Weekly'    
        elif selected_operation == 'Number of Customers Weekly':
    # Calculate number of unique customers weekly
            unique_customers_weekly = data.resample('W', on='Date')['memberID'].nunique().to_frame(name='Number of Customers')
    # Plot the graph
            fig = px.line(unique_customers_weekly, x=unique_customers_weekly.index, y='Number of Customers', labels={'Number of Customers': 'Number of Customers Weekly'})
            st.plotly_chart(fig)


        elif selected_operation == 'Sales per Customer Weekly':
    # Calculate number of sales weekly
            sales_weekly = data.resample('W', on='Date').size()

        # Calculate number of unique customers weekly
            unique_customers_weekly = data.resample('W', on='Date')['memberID'].nunique()

        # Calculate Sales per Customer Weekly
            sales_per_customer_weekly = sales_weekly / unique_customers_weekly

        # Plot the graph
            fig = px.line(sales_per_customer_weekly, x=sales_per_customer_weekly.index, y=sales_per_customer_weekly,
                    labels={'y': 'Sales per Customer Ratio'})
            fig.update_layout(title_text='Sales per Customer Weekly',
                        title_x=0.5, title_font=dict(size=18))
            fig.update_yaxes(rangemode="tozero")
            st.plotly_chart(fig)

        elif selected_operation == 'Frequency of the Items Sold':
    # Calculate frequency of items sold
            frequency_of_items = data.groupby('itemName').size().reset_index(name='count')

            # Plot the graph
            fig = px.treemap(frequency_of_items, path=['itemName'], values='count')
            fig.update_layout(title_text='Frequency of the Items Sold', title_x=0.5, title_font=dict(size=18))
            fig.update_traces(textinfo="label+value")
            st.plotly_chart(fig)

        elif selected_operation == 'Top Customers regarding Number of Items bought':
            # Calculate number of items bought by each customer
            user_item = data.groupby('memberID').size().reset_index(name='count').sort_values(by='count', ascending=False)
            
            # Plot the graph
            fig = px.bar(user_item.head(20), x='memberID', y='count',
                        labels={'y': 'Number of Items Bought', 'count': 'Number of Sales'},
                        color='count')
            fig.update_layout(title_text='Top 20 Customers regarding Number of Items Bought',
                            title_x=0.5, title_font=dict(size=18))
            fig.update_traces(marker=dict(line=dict(color='#E0FF43', width=1)))
            st.plotly_chart(fig)

        elif selected_operation == 'Number of Sales per Discrete Week Days':
            # Calculate number of sales per discrete week days
            day = data.groupby(data['Date'].dt.strftime('%A'))['itemName'].count()
            
            # Plot the graph
            fig = px.bar(day, x=day.index, y=day, color=day,
                        labels={'y': 'Number of Sales', 'Date': 'Week Days'})
            fig.update_layout(title_text='Number of Sales per Discrete Week Days',
                            title_x=0.5, title_font=dict(size=18))
            fig.update_traces(marker=dict(line=dict(color='#000000', width=1)))
            st.plotly_chart(fig)

        elif selected_operation == 'Number of Sales per Discrete Months':
            # Calculate number of sales per discrete months
            month = data.groupby(data['Date'].dt.strftime('%m'))['itemName'].count()
            
            # Plot the graph
            fig = px.bar(month, x=month.index, y=month, color=month,
                        labels={'y': 'Number of Sales', 'Date': 'Months'})
            fig.update_layout(title_text='Number of Sales per Discrete Months',
                            title_x=0.5, title_font=dict(size=18))
            fig.update_traces(marker=dict(line=dict(color='#000000', width=1)))
            st.plotly_chart(fig)

        elif selected_operation == 'Number of Sales per Discrete Month Days':
    # Calculate number of sales per discrete month days
            month_day = data.groupby(data['Date'].dt.strftime('%d'))['itemName'].count()
            
            # Plot the graph
            fig = px.bar(month_day, x=month_day.index, y=month_day, color=month_day,
                        labels={'y': 'Number of Sales', 'Date': 'Month Days'})
            fig.update_layout(title_text='Number of Sales per Discrete Month Days',
                            title_x=0.5, title_font=dict(size=18))
            fig.update_traces(marker=dict(line=dict(color='#000000', width=1)))
            st.plotly_chart(fig)


        elif selected_operation == 'Recency Distribution of the Customers':
    # Assuming you have a DataFrame named Recency containing the recency values
    # You need to replace Recency with your actual DataFrame name
            Recency = data.groupby(by='memberID')['Date'].max().reset_index()
            Recency.columns = ['memberID', 'LastDate']
            Recency.head()

            # Finding last date for our dataset
            last_date_dataset = Recency['LastDate'].max()
            last_date_dataset

            # Calculating Recency by subtracting (last transaction date of dataset) and (last purchase date of each customer)
            Recency['Recency'] = Recency['LastDate'].apply(lambda x: (last_date_dataset - x).days)
            Recency.head()
    
            # Plot the histogram
            fig = px.histogram(Recency, x='Recency', opacity=0.85, marginal='box')
            fig.update_traces(marker=dict(line=dict(color='#000000', width=1)))
            fig.update_layout(title_text='Recency Distribution of the Customers', title_x=0.5, title_font=dict(size=20))
            st.plotly_chart(fig)


        elif selected_operation == 'Visit Frequency Distribution of the Customers':
            # Assuming you have a DataFrame named Frequency containing the visit frequency values
            # You need to replace Frequency with your actual DataFrame name
            # Frequency of the customer visits
            Frequency = data.drop_duplicates(['Date', 'memberID']).groupby(by=['memberID'])['Date'].count().reset_index()
            Frequency.columns = ['memberID', 'Visit_Frequency']
            Frequency.head()
        
            # Plot the histogram
            fig = px.histogram(Frequency, x='Visit_Frequency', opacity=0.85, marginal='box')
            fig.update_traces(marker=dict(line=dict(color='#000000', width=1)))
            fig.update_layout(title_text='Visit Frequency Distribution of the Customers', title_x=0.5, title_font=dict(size=20))
            st.plotly_chart(fig)


        elif selected_operation == 'Monetary Distribution of the Customers':
            # Assuming you have a DataFrame named Monetary containing the monetary values
            # You need to replace Monetary with your actual DataFrame name
            Monetary = data.groupby(by="memberID")['itemName'].count().reset_index()
            Monetary.columns = ['memberID', 'Monetary']
            Monetary.head()

                        # I assumed each item has equal price and price is 10
            Monetary['Monetary'] = Monetary['Monetary'] * 10
            Monetary.head()
                        
            # Plot the histogram
            fig = px.histogram(Monetary, x='Monetary', opacity=0.85, marginal='box',
                            labels={'Monetary': 'Monetary'})
            fig.update_traces(marker=dict(line=dict(color='#000000', width=1)))
            fig.update_layout(title_text='Monetary Distribution of the Customers', title_x=0.5, title_font=dict(size=20))
            st.plotly_chart(fig)

        elif selected_operation == 'RFM Scores/RFM Segments':
            # Calculate Recency
            Recency = data.groupby(by='memberID')['Date'].max().reset_index()
            Recency.columns = ['memberID', 'Recency']
            
            # Calculate Frequency
            # You need to calculate Frequency based on your dataset
            # Frequency of the customer visits
            Frequency = data.drop_duplicates(['Date', 'memberID']).groupby(by=['memberID'])['Date'].count().reset_index()
            Frequency.columns = ['memberID', 'Visit_Frequency']
    
            # Calculate Monetary
            # You need to calculate Monetary based on your dataset.

            Monetary = data.groupby(by="memberID")['itemName'].count().reset_index()
            Monetary.columns = ['memberID', 'Monetary']
            Monetary['Monetary'] = Monetary['Monetary'] * 10
            
            
            
            # Combine all scores into one DataFrame
            RFM = pd.concat([Recency['memberID'], Recency['Recency'], Frequency['Visit_Frequency'], Monetary['Monetary']], axis=1)
            
            # Calculate RFM Quartiles and RFM Score
            # You need to calculate RFM quartiles and score based on your business logic

            # 5-5 score = the best customers
            RFM['Recency_quartile'] = pd.qcut(RFM['Recency'], 5, [5, 4, 3, 2, 1])
            RFM['Frequency_quartile'] = pd.qcut(RFM['Visit_Frequency'], 5, [1, 2, 3, 4, 5])

            RFM['RF_Score'] = RFM['Recency_quartile'].astype(str) + RFM['Frequency_quartile'].astype(str)
            RFM.head()
            
            # Map RFM Score to RFM Segment
            # You need to define your RFM segments mapping logic
                        
            segt_map = {  # Segmentation Map [Ref]
                r'[1-2][1-2]': 'hibernating',
                r'[1-2][3-4]': 'at risk',
                r'[1-2]5': 'can\'t loose',
                r'3[1-2]': 'about to sleep',
                r'33': 'need attention',
                r'[3-4][4-5]': 'loyal customers',
                r'41': 'promising',
                r'51': 'new customers',
                r'[4-5][2-3]': 'potential loyalists',
                r'5[4-5]': 'champions'
            }

            RFM['RF_Segment'] = RFM['RF_Score'].replace(segt_map, regex=True)
            RFM.head()
            
            # Count the occurrences of each RFM segment
            x = RFM['RF_Segment'].value_counts()
            
            # Plot the treemap
            fig = px.treemap(x, path=[x.index], values=x)
            fig.update_layout(title_text='Distribution of the RFM Segments', title_x=0.5, title_font=dict(size=20))
            fig.update_traces(textinfo="label+value+percent root")
            st.plotly_chart(fig)
            

        elif selected_operation == 'Relationship between Visit_Frequency and Recency':
            # Plot the scatter plot
            # Combining all scores into one DataFrame
            # Finding the last purchase date of each customer
            Recency = data.groupby(by='memberID')['Date'].max().reset_index()
            Recency.columns = ['memberID', 'Recency']

            # Frequency of the customer visits
            Frequency = data.drop_duplicates(['Date', 'memberID']).groupby(by=['memberID'])['Date'].count().reset_index()
            Frequency.columns = ['memberID', 'Visit_Frequency']
            # Frequency.head()

            Monetary = data.groupby(by="memberID")['itemName'].count().reset_index()
            Monetary.columns = ['memberID', 'Monetary']
            # Monetary.head()

            # I assumed each item has equal price and price is 10
            Monetary['Monetary'] = Monetary['Monetary'] * 10
            Monetary.head()

            RFM = pd.concat([Recency['memberID'], Recency['Recency'], Frequency['Visit_Frequency'], Monetary['Monetary']], axis=1)
            # RFM.head()

            # 5-5 score = the best customers
            RFM['Recency_quartile'] = pd.qcut(RFM['Recency'], 5, [5, 4, 3, 2, 1])
            RFM['Frequency_quartile'] = pd.qcut(RFM['Visit_Frequency'], 5, [1, 2, 3, 4, 5])

            RFM['RF_Score'] = RFM['Recency_quartile'].astype(str) + RFM['Frequency_quartile'].astype(str)
            # RFM.head()

            
            segt_map = {  # Segmentation Map [Ref]
                r'[1-2][1-2]': 'hibernating',
                r'[1-2][3-4]': 'at risk',
                r'[1-2]5': 'can\'t loose',
                r'3[1-2]': 'about to sleep',
                r'33': 'need attention',
                r'[3-4][4-5]': 'loyal customers',
                r'41': 'promising',
                r'51': 'new customers',
                r'[4-5][2-3]': 'potential loyalists',
                r'5[4-5]': 'champions'
            }

            RFM['RF_Segment'] = RFM['RF_Score'].replace(segt_map, regex=True)
            # RFM.head()
            fig = px.scatter(RFM, x="Visit_Frequency", y="Recency", color='RF_Segment',
                            labels={"Visit_Frequency": "Visit Frequency", "Recency": "Recency"})
            fig.update_layout(title_text='Relationship between Visit Frequency and Recency', title_x=0.5, title_font=dict(size=20))
            st.plotly_chart(fig)

            

    elif operation == 'Price Prediction':
        data = pd.read_csv(".\Train.csv")
                        # Function to get the first 20 unique values from the first column
        def get_unique_values():
            unique_values = data.iloc[:20, 0].unique()
            return unique_values
        # Function to filter dataframe based on selected unique ID
        def filter_data(selected_value):
            filtered_df = data[data.iloc[:, 0] == selected_value].dropna()
            return filtered_df
        

        
        
        # Function to draw graph
        # def draw_graph(data):
        #     fig = px.line(data, x=data.index, y='Item_Outlet_Sales', title='Item Outlet Sales Variation')
        #     st.plotly_chart(fig)

        # Function to train linear regression model and predict prices
        def predict_prices(data, target_column):
            X = data[['Item_Weight', 'Item_Visibility', 'Outlet_Establishment_Year']]
            y = data[target_column]

            # Split the data into training and testing sets
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

            # Train the linear regression model
            model = LinearRegression()
            model.fit(X_train, y_train)

            # Predict prices
            y_pred = model.predict(X)

            # Calculate RMSE (Root Mean Squared Error)
            rmse = mean_squared_error(y, y_pred, squared=False)
            st.write("RMSE:", rmse)

            return y_pred  # Predict prices for all data points

        # Function to draw graph of predicted values
# Function to draw graph of actual vs predicted values
        # Function to draw graph of actual vs predicted values
       # Function to draw graph of actual vs predicted values
        def draw_actual_vs_predicted(actual_values, predicted_values):
            fig = go.Figure()
            fig.add_trace(go.Bar(x=actual_values.index, y=actual_values.values, name='Actual Values'))
            fig.add_trace(go.Bar(x=actual_values.index, y=predicted_values, name='Predicted Values'))
            fig.update_layout(barmode='group', title='Actual vs Predicted Prices', xaxis_title='Index', yaxis_title='Price')
            st.plotly_chart(fig)


        operation = st.sidebar.selectbox("Select Operation", ["Price Prediction", "Analysis", "Customer Segmentation"])

        if operation == "Price Prediction":
            st.write("Select a value from the dropdown:")
            selected_value = st.selectbox("Values", get_unique_values())
            st.write("You selected:", selected_value)


            if selected_value:
                st.write("Data corresponding to selected value:")
                filtered_data = filter_data(selected_value)
                st.write(filtered_data)
                
                item_types = filtered_data['Item_Type'].unique()
                selected_item_type = st.selectbox("Item Type", item_types)
                
                establishment_years = filtered_data['Outlet_Establishment_Year'].unique()
                selected_establishment_year = st.selectbox("Outlet Establishment Year", establishment_years)
                
                outlet_sizes = filtered_data['Outlet_Size'].unique()
                selected_outlet_size = st.selectbox("Outlet Size", outlet_sizes)
                
                location_types = filtered_data['Outlet_Location_Type'].unique()
                selected_location_type = st.selectbox("Outlet Location Type", location_types)
                
                outlet_types = filtered_data['Outlet_Type'].unique()
                selected_outlet_type = st.selectbox("Outlet Type", outlet_types)
                
                final_output_options = ["Item_Outlet_Sales", "Item_MRP"]
                selected_output = st.selectbox("Final Output", final_output_options)
                
                if st.button("Predict"):
                    predicted_values = predict_prices(filtered_data, "Item_Outlet_Sales")
                    actual_values = filtered_data["Item_Outlet_Sales"]
                    st.write("Predicted Values:", predicted_values)
                    st.write("Actual Values:", actual_values)
                    draw_actual_vs_predicted(actual_values, predicted_values)

                elif operation == "Price Prediction (Item_MRP)":
                    st.write("Select a value from the dropdown:")
                    selected_value = st.selectbox("Item Identifier", get_unique_values())
                    
                    if selected_value:
                        st.write("Data corresponding to selected value:")
                        filtered_data = filter_data(selected_value)
                        st.write(filtered_data)
                        
                        if st.button("Predict"):
                            predicted_values = predict_prices(filtered_data, "Item_MRP")
                            actual_values = filtered_data["Item_MRP"]
                            st.write("Predicted Values:", predicted_values)
                            st.write("Actual Values:", actual_values)
                            draw_actual_vs_predicted(actual_values, predicted_values)

        elif operation == "Analysis":
            st.write("Select an ID:")
            selected_id = st.selectbox("Item_Identifier", data.iloc[:20, 0].unique())

            if selected_id:
                st.write("Data corresponding to selected ID:")
                filtered_data = data[data.iloc[:, 0] == selected_id].dropna()

                unique_columns = filtered_data.columns
                # selected_column = st.selectbox("Select a column:", unique_columns)

                        # Display graphs for each column
                # Display graphs for each specified column
                # Display graphs for each specified column
                # Display graphs for each specified column
                selected_column = st.selectbox("Select a column:", ['Item_Fat_Content', 'Outlet_Establishment_Year', 'Outlet_Size', 'Outlet_Location_Type', 'Outlet_Type', 'Item_Outlet_Sales'])
                if selected_column:
                    st.write(f"Visualization for {selected_column}:")
                    if selected_column == 'Item_Fat_Content':
                        fat_content_counts = filtered_data[selected_column].value_counts()
                        fig = px.pie(names=fat_content_counts.index, values=fat_content_counts.values, title=f'{selected_column} Distribution')
                    elif selected_column == 'Outlet_Establishment_Year':
                        fig = px.histogram(filtered_data, x=selected_column, title=f'{selected_column} Distribution')
                    elif selected_column == 'Item_Outlet_Sales':
                        fig = px.line(filtered_data, x=filtered_data.index, y=selected_column, title=f'{selected_column} Variation')
                    else:
                        fig = px.bar(filtered_data, x=selected_column, title=f'{selected_column} Distribution')

                    st.plotly_chart(fig)
                
                for column in ['Item_Fat_Content', 'Outlet_Establishment_Year', 'Outlet_Size', 'Outlet_Location_Type', 'Outlet_Type', 'Item_Outlet_Sales']:
                    st.write(f"Visualization for {column}:")
                    if column == 'Item_Fat_Content':
                        fat_content_counts = filtered_data[column].value_counts()
                        fig = px.pie(names=fat_content_counts.index, values=fat_content_counts.values, title=f'{column} Distribution')
                    elif column == 'Outlet_Establishment_Year':
                        fig = px.histogram(filtered_data, x=column, title=f'{column} Distribution')
                    elif column == 'Item_Outlet_Sales':
                        fig = px.line(filtered_data, x=filtered_data.index, y=column, title=f'{column} Variation')
                    else:
                        fig = px.bar(filtered_data, x=column, title=f'{column} Distribution')

                    st.plotly_chart(fig)
        

            # if selected_value:
            #     st.write("Data corresponding to selected value:")
            #     filtered_data = filter_data(selected_value)
            #     st.write(filtered_data)
            #     st.write("Graph of Item Outlet Sales:")
            #     draw_graph(filtered_data)



        
        # Add code for price prediction operation
        pass
    elif operation == 'Others':
        # Add code for other operations
        pass

# Main function to run the Streamlit app
def main():
    st.title('Grocery Store Analysis')
    st.sidebar.header('Options')
    operation = st.sidebar.selectbox('Operation', ['Market Basket Analysis', 'Price Prediction', 'Prodcut Recommendation '])
    display_options(operation)

if __name__ == '__main__':
    main()
