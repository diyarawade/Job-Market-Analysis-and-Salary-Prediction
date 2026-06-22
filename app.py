import streamlit as st
import joblib
import pandas as pd
st.set_page_config(
    page_title="Salary Predictor",
    page_icon="💼",
    layout="wide"
)

#Load model
model=joblib.load('salary_model.joblib')
cols=joblib.load('model_columns.joblib')

#Title
st.markdown("<h1 style='text-align:center; color:#4CAF50;'>💼 Job Salary Prediction App</h1>",unsafe_allow_html=True)
st.write("### Predict salaries base on job details")
st.markdown("---")

#User inputs
work_year=st.number_input("Work Year",2020,2030)
experience_level=st.selectbox("Experience Level",["Entry-Level","Mid-Level","Senior","Executive"])
employment_type=st.selectbox("Employment Type",["Full-Time","Part-Time","Contract","Freelance"])
job_title=st.selectbox("Job Title",["Data Scientist","Data Engineer","Data Analyst","Research Scientist","Big Data Engineer","Machine Learning Scientist","AI Scientist","ML Engineer","Data Architect","Machine Learning Developer","Data Specialist","Data Analytics Engineer","Data Science Consultant"])
employee_residence=st.selectbox("Employee Residence",["US","IN","DE","CA","NZ","FR","AS","IR"])
remote_ratio=st.slider("Remote Ratio",0,100)
company_location=st.selectbox("Company Location",["US","IN","DE","CA","NZ","FR","AS","IR"])
company_size=st.selectbox("Company Size",["Small","Medium","Large"])

#Prediction button
if st.button("Predict Salary"):
    input_df=pd.DataFrame(columns=cols)
    input_df.loc[0]=0
    input_df['work_year']=work_year
    input_df['remote_ratio']=remote_ratio
try:
    input_df[f'experience_level_{experience_level}']=1
    input_df[f'employment_type_{employment_type}']=1
    input_df[f'company_size_{company_size}']=1
    input_df[f'job_title_{job_title}']=1
    input_df[f'company_location_{company_location}']=1
    input_df[f'employee_residence_{employee_residence}']=1
    prediction=model.predict(input_df)
    st.success(f"Estimated Salary:${prediction[0]:,.2f}")
except:
    st.error("Something went wrong.Please select valid inputs")