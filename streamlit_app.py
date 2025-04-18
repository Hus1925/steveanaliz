
import streamlit as st
from utils import calculate_score

st.set_page_config(page_title="SteveAnaliz Radar", page_icon="🚀")

st.title("🚀 SteveAnaliz – Yatırım Radar Paneli")

companies = [
    {"name": "TechNova", "revenue": 120, "growth": 0.25, "rd_spending": 15},
    {"name": "DataWave", "revenue": 80, "growth": 0.32, "rd_spending": 12},
    {"name": "NextAI", "revenue": 95, "growth": 0.29, "rd_spending": 18},
]

st.subheader("📊 Şirket Skorları")
for c in companies:
    score = calculate_score(c)
    st.success(f"**{c['name']}** → Skor: **{score:.2f}**")

st.divider()
st.subheader("📁 Kendi Verinizi Yükleyin")
uploaded = st.file_uploader("Bir CSV dosyası seçin", type="csv")
if uploaded:
    st.info("🧠 Bu özellik v2 sürümünde aktif olacak.")
