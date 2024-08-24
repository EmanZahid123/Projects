#Streamlit Code

import streamlit as st
import pandas as pd
import pickle
import warnings
warnings.filterwarnings("ignore")

with open(r'c:\Users\Dell\OneDrive\Documents\FYP_ArifButt\practice\mini_proj_streamlit\amnesia_model.pkl', 'rb') as f:
    model = pickle.load(f)
st.title("AMNESIA PREDICTION")


Sex = st.text_input("Sex")
Red_pixel = st.text_input("Red_pixel")
Green_pixel = st.text_input("Green_pixel")
Blue_pixel = st.text_input("Blue_pixel")
Hb = st.text_input("Hb")

data = pd.DataFrame({'Sex':[Sex],'Red_pixel':[Red_pixel],'Green_pixel':[Green_pixel],'Blue_pixel':[Blue_pixel],'Hb':[Hb]})

result=""
if st.button("PREDICT"):
    result = model.predict(data)
    st.subheader("RESULT: " + str(result[0]))
else:
    st.subheader("Enter all the details and press PREDICT button")