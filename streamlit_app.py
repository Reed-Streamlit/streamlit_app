#!/usr/bin/env python
# coding: utf-8

import streamlit as st
import pickle
import pandas as pd

#packages not directly referenced in this script but used by 'rnd_clf_opt_rndcv.sav':
import numpy as np
import sklearn

########## Change ##########
MODEL_NAME = 'rnd_clf_opt_rndcv.sav'
OUTPUT_MSG = 'Lymph node metastasis?'
############################

def create_user_inputs() -> pd.DataFrame:
    """
    Generates and formats all inputs user sees on page, outputs the values as a dataframe to be passed to model for prediction.
    
    Returns:
        a dataframe containing values from the inputs selected by the user
    """
    
    st.title("Numerical Output Prediction")

    _left_buffer, main_col, _right_buffer = st.columns([1,3,1])
    with main_col:
        pirads = st.selectbox("PIRADS score", options=[1, 2, 3, 4, 5])
        age = st.number_input("Age", min_value=0, max_value=120, value=60)
        psa = st.number_input("PSA (ng/mL)", min_value=0.0, value=1.0)
        
        vol = st.number_input("Prostate volume (cm\u00b3)", min_value=10.0, max_value=200.0, value=10.0)
        adeno = st.radio("Adenopathy? (0=No/1=Yes)", options=[0, 1], horizontal = True)
        grade = st.selectbox("Biopsy grade", options=[1, 2, 3, 4, 5])
        white = st.radio("Race: white? (0=No/1=Yes)", options=[0, 1], horizontal = True)
    
    input_dict = {"P_Score": pirads, "age_rp": age, "PSA": psa,
                 "prostate_volume": vol, "adenopathy": adeno, 
                 "grade_prostate_bx": grade, "white_race": white}
    
    return pd.DataFrame([input_dict])

def main():
    #unpickling model
    model = pickle.load(open(MODEL_NAME, 'rb'))
    user_input_df = create_user_inputs()
    center_button = st.button("Estimate")
    
    if center_button: #if button is clicked
        #currently there is a warning that doesn't affect behavior:
        #UserWarning: X has feature names, but RandomForestClassifier was fitted without feature names
        #can change user_input_df to user_input_df.values to remove the warning
        output = model.predict(user_input_df)
        st.write(OUTPUT_MSG, output)

if __name__ == "__main__":
    main()

