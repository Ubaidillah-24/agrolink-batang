import streamlit as st
import joblib

# 1. Mengatur Judul Tab Browser
st.set_page_config(page_title="AGRO-LINK BATANG", page_icon="🌾", layout="wide")

# 2. Membangunkan "Otak" AI
model_agrolink = joblib.load('model_cerdas_agrolink.joblib')

# --- MEMBUAT PANEL SAMPING (SIDEBAR) ---
st.sidebar.header("⚙️ Pengaturan Lahan")
st.sidebar.write("Masukkan kondisi tanah dan cuaca saat ini:")

# Semua input dipindah ke sidebar
n = st.sidebar.number_input("Kandungan Nitrogen (N)", value=90)
p = st.sidebar.number_input("Kandungan Fosfor (P)", value=42)
k = st.sidebar.number_input("Kandungan Kalium (K)", value=43)
st.sidebar.markdown("---")
suhu = st.sidebar.number_input("Suhu Udara (°C)", value=28.0)
kelembapan = st.sidebar.number_input("Kelembapan Udara (%)", value=82.0)
ph = st.sidebar.number_input("pH Tanah", value=6.5)
hujan = st.sidebar.number_input("Curah Hujan (mm)", value=200.0)

# --- BAGIAN UTAMA (TENGAH) ---
st.title("🌾 Dashboard Cerdas AGRO-LINK BATANG")
st.write("Sistem rekomendasi tanam berbasis *Artificial Intelligence*. Dirancang untuk membantu petani mengambil keputusan terbaik agar terhindar dari risiko gagal panen.")
st.markdown("---")

st.write("### 🤖 Hasil Analisis Kecerdasan Buatan")

# Membuat Tombol Eksekusi
if st.button("Cek Rekomendasi Tanaman 🚀"):
    # AI mengambil data dari isian sidebar, lalu memprediksi
    data_lahan_petani = [[n, p, k, suhu, kelembapan, ph, hujan]]
    rekomendasi = model_agrolink.predict(data_lahan_petani)
    
    # Menampilkan hasil dengan ukuran font yang lebih besar
    st.success(f"🌟 Berdasarkan data tersebut, tanaman yang Paling Direkomendasikan adalah: **{rekomendasi[0].upper()}**")
    st.balloons() 
else:
    # Pesan default sebelum tombol ditekan
    st.info("👈 Silakan atur kondisi lahan di panel sebelah kiri, lalu tekan tombol **Cek Rekomendasi**.")