import streamlit as st

st.title('BMI Calculator')

weight=st.number_input("Enter your weight")

status_wt=st.radio("Select unit of weight:",['pound','kgs'])

if(status_wt=='pound'):
    weight=weight/0.454
else:
    weight=weight


height=st.number_input("Enter your height")

status_ht=st.radio("Select unit of height:",['cms','feet','meters'])

if(status_ht=='cms'):
    height=height/100
elif(status_ht=='meters'):
    height=height
else:
    height=height/3.28


bmi=weight/(height)**2

if(st.button('Calculate BMI')):
 
    # print the BMI INDEX
    st.text("Your BMI Index is {}.".format(bmi))
 
    # give the interpretation of BMI index
    if(bmi < 16):
        st.error("You are Extremely Underweight")
    elif(bmi >= 16 and bmi < 18.5):
        st.warning("You are Underweight")
    elif(bmi >= 18.5 and bmi < 25):
        st.success("Healthy")
    elif(bmi >= 25 and bmi < 30):
        st.warning("Overweight")
    elif(bmi >= 30):
        st.error("Extremely Overweight")