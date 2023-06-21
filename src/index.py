import streamlit as st
import requests
import os

#set the api url
api_url = os.getenv('API_URL')

def main():
    st.title('Candidate Form')
    first_name = st.text_input('First Name')
    last_name = st.text_input('Last Name')
    email = st.text_input('Email')
    about = st.text_area('About')
    submit_button = st.button('Submit')

    if submit_button:
        payload = {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'about': about
        }
        response = requests.post(api_url, json=payload)
        if response.status_code == 200:
            st.success('Candidate data submitted successfully!')
            # write the code to refresh the browser
        else:
            st.error('Error submitting candidate data.')

if __name__ == '__main__':
    main()