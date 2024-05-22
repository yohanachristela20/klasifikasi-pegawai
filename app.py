import pickle
import streamlit as st

employee_model = pickle.load(open('model_rf_klasifikasi_sdm_203400014.pkl', 'rb'))

# page title
st.title('Employee Prediction using ML')


# getting the input data from the user
col1, col2, col3 = st.columns(4)

with col1:
    JoiningYear = st.text_input('Joining Year')
    
with col2:
    PaymentTier = st.text_input('Categorization of Salary tiers')

with col3:
    Age = st.text_input('Age of Each Employee')

with col1:
    ExperienceInCurrentDomain = st.text_input('Experience Employees')

with col2:
    GenderMale = st.text_input('Gender Male')

with col3:
   EverBenchedYes = st.text_input('EverBenched Yes')

with col1:
     EducationMasters = st.text_input('Education Masters')

with col2:
    EducationPHD = st.text_input('Education PHD')
    
with col3:
     CityNewDelhi = st.text_input('City New Delhi')

with col1:
    CityPune = st.text_input('City Pune')


# code for Prediction
employee_prediction = ''

# creating a button for Prediction

if st.button('Employee Prediction Result'):
    prediction = employee_model.predict([[JoiningYear, PaymentTier, Age, ExperienceInCurrentDomain, GenderMale, EverBenchedYes, EducationMasters, EducationPHD, CityNewDelhi, CityPune ]])
    
    if (prediction[0] == 1):
      employee_prediction = 'The employee is leave'
    else:
      employee_prediction = 'The employee is not leave'
    
st.success(employee_prediction)
