import streamlit as st

# =========================
# CONFIG
# =========================
st.set_page_config(page_title="Divan Ahlaki Corpus", layout="wide")

st.title("📚 El-Büstî Divanı - Akademik Ahlaki Analiz Sistemi")

st.write("Bu sistem: arama + ahlaki sınıflandırma + haritalama yapar.")

# =========================
# INPUT
# =========================
text = st.text_area("📜 Beyitler (her satır bir beyit)")

query = st.text_input("🔍 Arama kelimesi")

# =========================
# AHLÂKÎ SINIFLANDIRMA MODELİ
# =========================
def classify(line):
    t = line.lower()

    if any(w in t for w in ["sabır", "tahammül", "dayan"]):
        return "Sabır"
    elif any(w in t for w in ["adalet", "hak", "insaf", "zulüm"]):
        return "Adalet"
    elif any(w in t for w in ["kerem", "ihsan", "cömert", "bağış"]):
        return "Cömertlik"
    elif any(w in t for w in ["dünya", "fani", "zühd", "ahiret"]):
        return "Zühd"
    elif any(w in t for w in ["öfke", "hiddet", "gazap"]):
        return "Öfke kontrolü"
    elif any(w in t for w in ["hikmet", "akıl", "ibret"]):
        return "Hikmet"
    else:
        return "Genel"

# =========================
# PROCESSING
# =========================
if text:
    lines = [l for l in text.split("\n") if l.strip()]

    st.subheader("📄 Veri Analizi")

    st.write("Toplam beyit:", len(lines))

    filtered = []

    for l in lines:
        if query and query not in l:
            continue

        category = classify(l)
        filtered.append((l, category))

    # =========================
    # RESULTS
    # =========================
    st.subheader("📌 Sonuçlar")

    for line, cat in filtered:
        st.write(f"**{cat}** → {line}")

    # =========================
    # ETHICAL MAP
    # =========================
    if filtered:
        st.subheader("🧭 Ahlaki Harita")

        stats = {}
        for _, cat in filtered:
            stats[cat] = stats.get(cat, 0) + 1

        total = sum(stats.values())

        percent = {k: (v / total) * 100 for k, v in stats.items()}

        st.write("📊 Yüzdesel dağılım")

        for k, v in percent.items():
            st.write(f"{k}: %{v:.2f}")

        st.bar_chart(percent)
