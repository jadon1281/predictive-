import numpy as np
import pandas as pd
import streamlit as st
import pickle

# Load the model (replace 'your_model_file.pkl' with your actual model file)
model = pickle.load(open('model.pkl', 'rb'))

def main():
    st.title("Predictive Maintenance for Wind Energy Production")
    html_temp = """
    <div style="background:#025246 ;padding:10px">
    <h3 style="color:white;text-align:center;">Enter Values of Sensors</h3>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    # Create 40 input fields for decimal values
    input_values = []
    for i in range(40):
        value=st.number_input(f"Enter value {i+1}",step=1.,format="%.4f") 
        input_values.append(value)



    # Button styling
    st.markdown('''
            <style>
            .stButton>button {
                color: #037bfc;
                border-color: #037bfc;
            }
            .stButton>button:hover {
                background-color: #037bfc;
                color: white;
            }
            </style>
            ''', unsafe_allow_html=True)

    if st.button("Predict"):
        # Convert input to DataFrame
        input_df = pd.DataFrame([input_values])
        
        # Make prediction
        result = model.predict(input_df)
        
        if result[0] == 1:
            st.markdown('''
            <style>
            .element-container:has(.stError) {
                background-color: #911919;
                padding: 10px;
                border-radius: 5px;
            }
            </style>
            ''', unsafe_allow_html=True)
            st.error("Failure predicted.")
        else:
            st.markdown('''
            <style>
            .element-container:has(.stSuccess) {
                background-color: #1e8f1e;
                padding: 10px;
                border-radius: 5px;
            }
            </style>
            ''', unsafe_allow_html=True)
            st.success("No failure predicted.")

if __name__ == '__main__':
    main()