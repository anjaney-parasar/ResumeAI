import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from st_pages import hide_pages, Page, show_pages

hide_pages([
    
    'interview',
    'results'])


st.title("HR Input")
with st.form("login"):
    question=st.text_input("Enter Interview Question")
    ideal_ans=st.text_area("Enter Ideal Answer")
    submitted = st.form_submit_button("Submit")

    if submitted:
        if question and ideal_ans:
            st.session_state['question']=question
            st.session_state['ideal_ans']=ideal_ans
            switch_page('login')
        else:
            st.write("Please update the Question or Ideal Answer.")


    
