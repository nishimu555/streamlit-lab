import streamlit as st

class st_session:
    session_list=["name","age"]
    
    def __init__(self):
        for item in self.session_list:
            if item not in st.session_state:
                st.session_state[item] = ""
            else:
                st.session_state[item] = st.session_state[item]
