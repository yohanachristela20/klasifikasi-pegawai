import pickle
import streamlit as st

employee_model = pickle.load(open('model_rf_klasifikasi_sdm_203400014.pkl', 'rb'))

# page title
st.title('Employee Prediction using ML')


# getting the input data from the user
col1, col2, col3 = st.columns(3)

with col1:
    Education = st.text_input('Educational Qualifications of Employee')
    
with col2:
    JoiningYear = st.text_input('Joining Year Each Employee in Company')

with col3:
    City = st.text_input('Location Employee')

with col1:
    PaymentTier = st.text_input('Categorization of Salary tiers')

with col2:
    Age = st.text_input('Age of Each Employee')

with col3:
    Gender = st.text_input('Gender Identity of Employee')

with col1:
    EverBenched = st.text_input('Condition when employee has ever been temporarily without assigned work')

with col2:
    ExperienceInCurrentDomain = st.text_input('Experience Employees Have in Their Current Field.')


# code for Prediction
employee_prediction = ''

# creating a button for Prediction

if st.button('Employee Prediction Result'):
    prediction = employee_model.predict([[Education, JoiningYear, City, PaymentTier, Age, Gender, EverBenched, ExperienceInCurrentDomain]])
    
    if (prediction[0] == 1):
      employee_prediction = 'The employee is leave'
    else:
      employee_prediction = 'The employee is not leave'
    
st.success(employee_prediction)
