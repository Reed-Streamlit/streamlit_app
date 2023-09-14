#!/usr/bin/env python
# coding: utf-8

import streamlit as st
import pickle
import pandas as pd

#packages not directly referenced in this script but used by 'rnd_clf_opt_rndcv.sav':
import numpy as np
import sklearn

#unpickling model
model = pickle.load(open('rnd_clf_opt_rndcv.sav', 'rb'))

def format_model_input(df):
    #return df.values
    return df

def format_model_output(pred):
    return pred[0]
    
def predict_output(input_df: pd.DataFrame) -> float:
    """
    Args:
        a dataframe containing values from the inputs selected by the user
    Returns:
        output of model prediction as determined by the format_model_output function
    """
    formatted_input = format_model_input(input_df)
    pred = model.predict(formatted_input)
    return format_model_output(pred)

def create_user_inputs():
    """
    Generates and formats all inputs user sees on page, outputs the values to be passed to model for prediction.
    
    Returns:
        a dataframe containing values from the inputs selected by the user
    """
    
    st.title("Numerical Output Prediction")

    pirads = st.selectbox("PIRADS score", options=[1, 2, 3, 4, 5])
    age = st.number_input("Age", min_value=0, max_value=120, value=60)
    psa = st.number_input("PSA (ng/mL)", min_value=0.0, value=1.0)
    vol = st.number_input("Prostate volume (cm^3)", min_value=10.0, max_value=200.0, value=10.0)
    adeno = st.radio("Adenopathy? (0=No/1=Yes)", options=[0, 1])
    grade = st.selectbox("Biopsy grade", options=[1, 2, 3, 4, 5])
    white = st.radio("Race: white? (0=No/1=Yes)", options=[0, 1])
    
    input_dict = {"P_Score": pirads, "age_rp": age, "PSA": psa,
                 "prostate_volume": vol, "adenopathy": adeno, 
                 "grade_prostate_bx": grade, "white_race": white}
    
    return pd.DataFrame([input_dict])



def main():
    user_input_df = create_user_inputs()
    center_button = st.button("Estimate")
    
    if center_button:
        output = predict_output(user_input_df)
        st.write("Lymph node metastasis?", output)

if __name__ == "__main__":
    main()

