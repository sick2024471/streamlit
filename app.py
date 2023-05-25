import streamlit as st

st.title("귀납법 프로그램 실행합니다.")
number = st.number_input("개별적 사실 몇개를 입력하시겠습니까?",1,5)
for i in range(number):
  Ginfer1 = st.text_input("개별적 사실", value = "여러 문장 입력시 ,로 구분해서 쓰시오")
Ginfer2 = st.text_input("소전제")

