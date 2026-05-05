st.subheader("🧭 Ahlaki Harita (Ethical Map)")

# حساب التوزيع
if results:
    stats = {}
    for _, c in results:
        stats[c] = stats.get(c, 0) + 1

    total = sum(stats.values())

    percentages = {k: (v / total) * 100 for k, v in stats.items()}

    st.write("📊 Yüzdesel dağılım:")

    for k, v in percentages.items():
        st.write(f"**{k}**: %{v:.2f}")

    st.bar_chart(percentages)
