import streamlit as st
import sklearn
import numpy as np
import pickle

# Load the model
with open ("house_pricing.pkl", "rb") as file:
    final_model=pickle.load(file)

# Streamlit UI
st.title("Housing Price Prediction App")
st.write("This app predicts the Price of a House")
st.write("Please input the following parameters:")

# Input 
br=st.number_input('Number of Bedrooms. Between 1-5')
bth=st.number_input('Numer of Bathrooms. Between 1-5')
tilt=st.number_input('Number of Toilets. Between 1-5')
ps=st.number_input('Number of Packing Space. Between 1-5')
db=st.selectbox("Is it a Detached Bongalo 0 for No and 1 for Yes:", [0, 1])
dd=st.selectbox("Is it a Detached Duplex 0 and No and 1 for Yes:", [0, 1])

if st.button("Predict"):
    user_input=np.array([[br,bth,tilt,ps,db,dd]])
    prediction=final_model.predict(user_input)
    st.write(f"From the Input you Gave The Price of The House is Predicted {round(prediction[0])} Naira.")
