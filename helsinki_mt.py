import streamlit as st
import requests

language = st.sidebar.selectbox(
    "Hangi çeviriyi istersiniz",
    ("tr-en","en-tr")
)


if language == "tr-en":
    st.header("TÜRKÇE-İNGİLİZCE ÇEVİRİ")

    col1,col2 = st.columns([2,2])

    text = col1.text_area('Türkçe Cümle',"test")
    

    req = requests.post("http://127.0.0.1:5000/", json={'source':'tr-en', 'text':text})

    rs = req.json()

    col2.text_area("İngilizce Çeviri ", rs['çeviri'])


else:
    st.header("İNGİLİZCE-TÜRKÇE ÇEVİRİ")

    col1,col2 = st.columns([2,2])
    text = col1.text_area('İngilizce Cümle',"test")

    req = requests.post("http://127.0.0.1:5000/", json={'source':'en-tr', 'text':text})

    rs = req.json()

    col2.text_area("Türkçe Çeviri: ", rs['çeviri'])


