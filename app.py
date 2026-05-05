import streamlit as st

st.set_page_config(page_title="Divan Ahlaki Analiz", layout="wide")

st.title("📚 El-Büstî Divanı - Ahlaki Analiz ve Arama")

st.write("Her satır bir beyit olacak şekilde metni giriniz")

text = st.text_area("Metin")

query = st.text_input("🔍 Arama")

# -------------------------
# Ahlaki sınıflandırma modeli (basit kural tabanlı)
# -------------------------
def classify(line):
    line_lower = line.lower()

    if any(word in line_lower for word in ["sabır", "sabret", "tahammül"]):
        return "Sabır"
    elif any(word in line_lower for word in ["adalet", "hak", "insaf"]):
        return "Adalet"
    elif any(word in line_lower for word in ["cömert", "ihsan", "kerem"]):
        return "Cömertlik"
    elif any(word in line_lower for word in ["dünya", "zühd", "fani"]):
        return "Zühd"
    elif any(word in line_lower for word in ["öfke", "hiddet"]):
        return "Öfke kontrolü"
    else:
        return "Genel / Diğer"

# -------------------------
# Processing
# -------------------------
if text:
    lines = [l for l in text.split("\n") if l.strip()]

    st.write("📄 Toplam beyit:", len(lines))

    results = []

    for l in lines:
        if query:
            if query not in l:
                continue

        category = classify(l)
        results.append((l, category))

    st.subheader("📊 Sonuçlar")

    for r, c in results:
        st.write(f"**{c}** → {r}")

    # İstatistik
    if results:
        st.subheader("📈 Dağılım")
        stats = {}
        for _, c in results:
            stats[c] = stats.get(c, 0) + 1

        st.bar_chart(stats)
