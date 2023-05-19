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

        st.sidebar.title("추론하는 프로그램")
        st.sidebar.subheader("어떤법으로 추론하시겠습니까?")
               
        app = st.sidebar.radio(
            '',
            self.apps,
            format_func=lambda app: app['title'])
    
        app['function']()
def g():
    st.title("귀납법 프로그램 실행합니다.")
    Ginfer1 = st.text_input("대전체")
    Ginfer2 = st.text_input
def y():
    st.title("연역법 프로그램 실행합니다.")
    Yinfer1 = st.text_input("대전체")
    Yinfer2 = st.text_input("소전체")
infer = MultiApp()
infer.add_app("귀납법 입력", g)
infer.add_app("연역법 입력", y)
infer.run()
