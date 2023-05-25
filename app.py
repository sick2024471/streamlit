import streamlit as st

st.title("귀납법 프로그램 실행합니다.")
number = st.number_input("개별적 사실 몇개를 입력하시겠습니까?",1,5)
i = 0
if st.button("결정"):
  Ginfer1 = []
  while i < number:
    Ginfer1.append(st.text_input("개별적 사실"))
    i++
  Ginfer2 = st.text_input("소전제")

