import streamlit as st

st.title('추론하는 프로그램')
st.header('추론 방식을 선택하세요')

btn_clicked1 = st.button("귀납법")
btn_clicked2 = st.button("귀납법")
if btn_clicked1:
  st.write("귀납법 추론을 선택하셨습니다.")

 if btn_clicked2:
  st.write("연역법 추론을 선택하셨습니다.")
