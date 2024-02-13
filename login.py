import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import fuzzywuzzy as fw 
from st_pages import hide_pages, Page, show_pages
st.set_page_config(
    page_title="Interview AI"
)
# show_pages(
#     [
        
#         Page(path="pages/HRpage.py", name="HR Inputs", icon="🏠"),
#     ]
# )

if 'question' not in st.session_state:
    st.session_state['question']='''What is Machine Learning?'''
if 'ideal_ans' not in st.session_state:
    st.session_state['ideal_ans']='''Machine learning, a specialized domain within artificial intelligence, 
revolves around crafting algorithms and models that empower computers to discern
 patterns and formulate decisions autonomously, without the need for explicit
 programming instructions. '''

# show_pages(
#     [
#         Page("login.py", "Candidate Login", "👤"),
#         #Page("other_pages/page2.py", "Page 2", ":books:"),
#     ]
# )

hide_pages([
    
    'interview',
    'results'])


st.title("Login Page")
with st.form("login"):
   st.write("**Eligibility Check**")
   experience = st.slider("Experience",0,5,1)
   
   education=st.radio("Education ",['Intermediate',"Graduate","Master's"])
   

   # Every form must have a submit button.
   submitted = st.form_submit_button("Submit")
   if submitted:
        if (experience>2) and (education=='Graduate' or education=="Master's"):
            switch_page("interview")
        else:
            st.write("Sorry, you don't meet the eligibility criteria. Please try next time.")
       
    #    st.write("slider", experience, "checkbox", degree)



#TO DO make another where the HR can enter these critirion using session_state_variables


#st.sidebar.success("Select a page above:")
