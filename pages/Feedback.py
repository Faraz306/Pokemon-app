import streamlit as st

st.title('What problem do you have?')
with st.form(key='form'):
    it1 = st.text_input("Enter your E-mail.")
    it = st.text_area("Enter your problem here.")
    button = st.form_submit_button("Submit")
    if button:
        send_email(it)
        st.success("Email sent!")