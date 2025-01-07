from streamlit import st
import pandas as pd
from models.model import load_model, predict
from utils.helpers import preprocess_input

# Load the classification model
model = load_model()

# Set up the Streamlit interface
st.title("Hoax Classification App")
st.write("Enter the text you want to classify as hoax or not hoax:")

# User input
user_input = st.text_area("Input Text")

if st.button("Classify"):
    if user_input:
        # Preprocess the input
        processed_input = preprocess_input(user_input)
        
        # Make prediction
        prediction = predict(model, processed_input)
        
        # Display the result
        st.write("Prediction:", "Hoax" if prediction == 1 else "Not Hoax")
    else:
        st.write("Please enter some text to classify.")