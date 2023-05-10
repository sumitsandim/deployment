
import streamlit as st
import pandas as pd
import pickle
from PIL import Image

primaryColor="blue"

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://thumbs.dreamstime.com/z/text-sign-showing-hand-written-words-loan-eligibility-178226196.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()
Gender=["Female","Male"]
Married=["Yes","No"]
Education=["Graduate","Not Graduate"]
Self_Employed=["Yes","No"]
Property_Area=['Urban', 'Rural', 'Semiurban']
Credit_History=[0.0,1.0]
Dependents=[0.0,1.0,2.0,3.0]
loan= pickle.load(open('loan.pkl','rb'))
st.title('Check your Loan ELgibility')
col1,col2,col3,col4,col5,col6,col7=st.columns(7)
with col1:
    Sex=st.selectbox("select the Gender ",sorted(Gender))
with col2:
    Married=st.selectbox("Are you Married",sorted(Married))
with col3:
    Education=st.selectbox("Are you Graduated",sorted(Education))    
with col4:
    Self_Employed=st.selectbox("you are Self Employed",sorted(Self_Employed))     
with col5:
    Property_Area=st.selectbox("Please Classify your Property Area",sorted(Property_Area))
with col6:
    Credit_History=st.selectbox("select the credit_History 0:No,1:Yes ",sorted(Credit_History))
with col7:
    Dependents=st.selectbox("select the Number family members depends on your income ",sorted(Dependents))    
           
ApplicantIncome = st.number_input('ApplicantIncome')
CoapplicantIncome= st.number_input('CoapplicantIncome')
LoanAmount= st.number_input('LoanAmount')  
Loan_Amount_Term =st.number_input('Loan_Amount_Term');
submitted = st.button('Submit')
if submitted:
    df = pd.DataFrame({
        'Gender': [Sex],
        'Married': [Married],
        'Dependents': [Dependents],
        'Education': [Education],
        'Self_Employed': [Self_Employed],
        'ApplicantIncome': [ApplicantIncome],
        'CoapplicantIncome': [CoapplicantIncome],
        'LoanAmount': [LoanAmount],
        'Dependents': [Dependents],
        'Loan_Amount_Term': [Loan_Amount_Term],
        'Credit_History': [Credit_History],
        'Property_Area': [Property_Area]
        })
    x = pd.DataFrame(df) 
    prediction =loan.predict_proba(x)
    if prediction[0][0] > 0.5:
        st.write('You are elgible')
    else:
        st.write('You are not  elgible')