import streamlit as st

st.title("귀납법 프로그램 실행합니다.")
number = st.number_input("개별적 사실 몇개를 입력하시겠습니까?",1,5)
i = 0
if st.button("결정"):
  Ginfer1 = []
  for i in range(number):
    Ginfer1[i] = st.text_input("개별적 사실을 입력 받으세요")
    st.write(Ginfer[i])
  Ginfer2 = st.text_input("소전제")

