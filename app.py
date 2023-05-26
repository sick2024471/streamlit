import streamlit as st

st.title("귀납법 프로그램 실행합니다.")

Ginfer1 = []
number = st.number_input("개별적 사실 몇개 입력하시겠습니까?",1,5)
for i in range(number):
    fact = st.text_input("개별적 사실을 입력하세요", key = i)
    Ginfer1.append(fact)

Ginfer2 = st.text_input("소전제")
if button ("-"):
    st.write("-")
