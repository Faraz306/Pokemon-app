import streamlit as st
from my_email import send_email

with st.form(key='my_form'):
    Email = st.text_input("Enter your Email...")
    RAW_description = st.text_area("Enter your description...")
    description = f"""\
Subject: new email from {Email}
From: {Email}
{RAW_description}
"""
    button = st.form_submit_button("Submit")

    if button:
        send_email(description)
        st.success("Email sent!")