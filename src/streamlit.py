# Import library
import streamlit as st
import requests
import pandas as pd


# Create the title
st.title("Credit Score Prediction")
# st.subheader("Input the applicant's data and click the "Predict" button")


# Create the form for input
with st.form(key = "applicant_data_form"):

    # Input applicant's name
    app_name = st.text_input('Applicants name', '')

    # Input person_age
    person_age = st.number_input(
        label = "1.\tAge:",
        min_value = 20,
        max_value = 55,
        help = "Value range from 20 to 55"
    )

    # Input person_gender
    person_gender = st.radio(
        label = "2.\tGender:",
        options = ["male", "female"],
        index = 0,
        horizontal = True
    )

    # Input person_job
    person_job = st.radio(
        label = "3.\tJob Category:",
        options = [0, 1, 2, 3],
        captions = ["unskilled and non-resident", "unskilled and resident",
                    "skilled", "highly skilled"],
        index = 0,
        horizontal = True
    )

    # Input saving_acc
    saving_acc = st.radio(
        label = "4.\tSaving Account Type:",
        options = ["little", "moderate", "quite rich", "rich"],
        index = 0,
        horizontal = True
    )

    # Input checking_acc
    checking_acc = st.radio(
        label = "5.\tChecking Account Type:",
        options = ["little", "moderate", "rich"],
        index = 0,
        horizontal = True
    )

    # Input duration
    duration = st.number_input(
        label = "6.\tCredit Duration (month):",
        min_value = 3,
        max_value = 60,
        help = "Value range from 3 to 60 month"
    )

    # Input purpose
    purpose = st.selectbox(
        label = "7.\tCredit Purpose:",
        options = ("car", "furniture/equipment", "radio/TV", 
                   "domestic appliances", "repairs", "education", 
                   "business", "vacation/others")
    )

    # Create the submit button
    submitted = st.form_submit_button("PREDICT")

    # Condition if the input is submitted
    if submitted:
        # Collect the data
        applicant_data_form = {
            "Age": person_age,
            "Sex": person_gender,
            "Job": person_job,
            "Saving_accounts": saving_acc,
            "Checking_account": checking_acc,
            "Duration": duration,
            "Purpose": purpose
        }

        # Create a loading animation to send the data
        with st.spinner("Kirim data untuk diprediksi server ..."):
            res = requests.post("http://localhost:8000/predict",
                                json = applicant_data_form).json()
        # Print the results
        st.write(res)

        st.success(f"""
                Applicant's name: **{app_name}**
                     
                Credit score: **{res['Score']}**  
                Probability of being good: **{res['Proba']}**  
                Recommendation: **{res['Recommendation']}**
            """)
