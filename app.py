import streamlit as st

st.set_page_config(page_title="Divan Analiz Sistemi", layout="wide")

st.title("📚 El-Büstî Divanı Ahlaki Analiz Sistemi")

st.write("Beyitleri aşağıya yapıştırın:")

text = st.text_area("Metin")

if text:
    lines = text.split("\n")
    st.write("Toplam beyit sayısı:", len(lines))
