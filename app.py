import streamlit as st

st.set_page_config(page_title="Divan Arama Sistemi", layout="wide")

st.title("📚 El-Büstî Divanı - Arama Aracı")

st.write("Beyitleri aşağıya yapıştırın (her satır bir beyit)")

text = st.text_area("Metin")

query = st.text_input("🔍 Aranacak kelime")

if text:
    lines = [l for l in text.split("\n") if l.strip()]

    st.write("📄 Toplam beyit:", len(lines))

    if query:
        results = [l for l in lines if query in l]

        st.write("🔎 Sonuç sayısı:", len(results))

        st.subheader("📌 Sonuçlar")
        for r in results:
            st.write(r)
