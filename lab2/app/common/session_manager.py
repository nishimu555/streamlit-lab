import streamlit as st

class st_session:
    # ページ間でセッション情報を引き継ぐために、対象のキーと初期値を二重配列定義する。
    session_list=\
        [\
            ["name",""],\
            ["age",25],\
            ["chk1",False]\
        ]
    
    def __init__(self):
        for item in self.session_list:
            if item[0] not in st.session_state:
                st.session_state[item[0]] = item[1]
            else:
                st.session_state[item[0]] = st.session_state[item[0]]
    
    def write_session_info(self):
        st.write("#session info#")
        for item in st.session_state:
            st.write(item,"=",st.session_state[item])
