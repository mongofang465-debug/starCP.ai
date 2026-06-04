import streamlit as st

from search import search_person
from analyzer import analyze_single
from analyzer import analyze_cp

st.title("AI明星CP分析师")

person1 = st.text_input("姓名1")

person2 = st.text_input("姓名2（可选）")

if st.button("开始分析"):

    if person1 and not person2:

        profile = search_person(person1)

        result = analyze_single(profile)

        st.markdown(result)

    elif person1 and person2:

        profile1 = search_person(person1)

        profile2 = search_person(person2)

        result = analyze_cp(profile1, profile2)

        st.markdown(result)