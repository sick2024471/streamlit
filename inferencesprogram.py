import streamlit as st

st.title('추론하는 프로그램')
st.header('추론 방식을 선택하세요')

if st.button("귀납법"):
  st.write("귀납법 추론을 선택하셨습니다.")

if st.button("연역법"):
  st.write("연역법 추론을 선택하셨습니다.")
