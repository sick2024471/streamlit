import streamlit as st

st.title("귀납법 프로그램 실행합니다.")
Ginfer1 = []
for i in range(5):
  fact = st.text_input("개별적 사실을 입력 받으세요")
  Ginfer1.append(fact)
Ginfer2 = st.text_input("소전제")

