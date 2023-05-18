import streamlit as st

class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):

        self.apps.append({
            "title": title,
            "function": func
        })

    def run(self):

        st.sidebar.title("Python Stat Tools v3.2")
        st.sidebar.subheader("by Ken Harmon")
        st.session_state.gs_URL = st.sidebar.text_input("Public Google Sheet URL:","https://docs.google.com/spreadsheets/d/1Fx7f6rM5Ce331F9ipsEMn-xRjUKYiR3R_v9IDBusUUY/edit#gid=0") 
               
        app = st.sidebar.radio(
            '',
            self.apps,
            format_func=lambda app: app['title'])

        app['function']()
def g():
  st.title("귀납법 프로그램 실행합니다.")

def y():
  st.title("연역법 프로그램 실행합니다.")
infer = MultiApp()
infer.add_app("귀납법 입력",g.app)
infer.add_app("귀납법 입력",y.app)
