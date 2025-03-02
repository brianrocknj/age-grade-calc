import streamlit as st
import utils
import ageGrade

st.title("Age Grade Calculator")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

i = 0
a = st.number_input('Age', min_value=20, max_value=79)
g = st.selectbox('Gender',['M', 'W'], index=None)
t = st.selectbox('Race Time:',
                utils.getAllTimes(),
                key=f't{i}',
                index=None,
                placeholder='mm:ss or hh:mm:ss')

st.write("Time:",t)
st.write("Age:",a)
st.write("PLP:",ageGrade.getAgeGrade(t,g,a))
st.write("Age Graded Time:",ageGrade.getAgeGradedTime(t,g,a))