import streamlit as st 
import joblib 

# Load the trained model
model = joblib.load('house_model.pkl')

# title of the web app
st.title("House Price Prediction App") 
st.write("Enter house detail to predict the price.") 


# user input for house features
size = st.number_input("House size in square feet:")
bedrooms = st.number_input("Number of bedrooms")
age = st.number_input("Age of the house in years")

# Prediction Button
if st.button("Predict Price"):
    #
    input_data = [[size,bedrooms , age]]
    #
    predicted_price = model.predict(input_data)
    #
    st.success(f"The predicted price of the house is: ${predicted_price[0]:,.2f}")