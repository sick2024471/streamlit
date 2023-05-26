import streamlit as st

st.title("귀납법 프로그램 실행합니다.")

Ginfer1 = []
number = st.number_input("개별적 사실 몇개 입력하시겠습니까?",1,5)
for i in range(number):
    fact = st.text_input("개별적 사실을 입력하세요", key = i)
    if st.button("∧(and)", key="and"):
    st.text_input(label="", value="∧", key="and_in")

    if st.button("∨(or)", key="or"):
    st.text_input(label="", value=str("∨"), key="or_in")
    
    if st.button("¬(not)", key="not"):
    st.text_input(label="", value=str("¬"), key="not_in")

    if st.button("→(imply)", key="imply"):
    st.text_input(label="", value=str("→"), key="imply_in")

    if st.button("↔(equal)", key="equal"):
    st.text_input(label="", value=str("↔"), key="equal_in")

Ginfer2 = st.text_input("소전제")
if button ("-"):
    st.write("-")
