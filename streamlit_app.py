import streamlit as st
import utils
import ageGrade
import pandas as pd

# st.title("Age Grade Calculator")
# st.write("Enter the details below to calculate the age grade and percentile.")

i = 0

age = st.number_input('Age', min_value=20, max_value=79)
gender = st.selectbox('Gender',['Male', 'Female'], index=None)
time = st.selectbox('Race Time:',
                    utils.getAllTimes(),
                    key=f't{i}',
                    index=None,
                    placeholder='mm:ss or hh:mm:ss')

if age and gender and time:
    plp = ageGrade.getAgeGrade(time, gender, age)
    ageTime = ageGrade.getAgeGradedTime(time, gender, age)
    perc = ageGrade.getPercentile(time, gender, age)

    result = {'Age' : age,
              'Gender' : gender,
              'Time' : time,
              'PLP' : f'{plp}%',
              'Age Graded Time' : ageTime,
              'Percentile' : f'{perc}%'}
    result = pd.DataFrame([result]).T
    result.rename(columns={0 : 'Result'}, inplace=True)
    st.write(result)