import streamlit as st
import joblib
import pandas as pd
import plotly.express as px # <-- Ini alat sihir visual interaktifnya!

# 1. Mengatur Judul Tab Browser
st.set_page_config(page_title="AGRO-LINK BATANG", page_icon="🌾", layout="wide")

# --- INISIALISASI MEMORI APLIKASI ---
if 'sudah_login' not in st.session_state:
    st.session_state['sudah_login'] = False
if 'nama_user' not in st.session_state:
    st.session_state['nama_user'] = ""
if 'peran' not in st.session_state:
    st.session_state['peran'] = ""
if 'lokasi' not in st.session_state:
    st.session_state['lokasi'] = ""

# TRIK PRESENTASI: Mengisi data awal agar grafik tidak kosong saat didemokan ke Juri
if 'database_pasar' not in st.session_state:
    data_awal = {
        "Pasar": ["Pasar Limpung", "Pasar Induk Kabupaten Batang", "Pasar Bawang", "Pasar Bandar"],
        "Pedagang": ["Haji Somad", "Bu Tejo", "Pak Slamet", "Koh Ahong"],
        "Komoditas": ["Padi / Beras", "Kopi", "Jagung", "Kacang Merah"],
        "Harga Beli/Kg (Rp)": [12500, 35000, 8000, 22000],
        "Stok Tersedia (Kg)": [500, 150, 800, 300]
    }
    st.session_state['database_pasar'] = pd.DataFrame(data_awal)


# ==========================================
# HALAMAN 1: FORM LOGIN (Dengan Validasi NIK)
# ==========================================
def halaman_login():
    st.title("🌾 Masuk ke Ekosistem AGRO-LINK BATANG")
    st.write("Sistem terintegrasi untuk Petani dan Pedagang Pasar di Kabupaten Batang.")
    st.markdown("---")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        peran_input = st.radio("Masuk Sebagai:", ["Pilih Peran...", "👨‍🌾 Petani", "🛒 Penjual (Pedagang Pasar)"])
        
        if peran_input != "Pilih Peran...":
            if st.button("🌐 Lanjutkan dengan Akun Google", use_container_width=True):
                st.info("Fitur Single Sign-On (SSO) Google sudah disiapkan dan akan aktif setelah integrasi Database Awan selesai.")
            
            st.markdown("<p style='text-align: center;'>— ATAU DAFTAR MANUAL —</p>", unsafe_allow_html=True)
            
            nik_input = st.text_input("Nomor Induk Kependudukan (NIK)*", placeholder="Masukkan 16 digit angka NIK", max_chars=16)
            nama_input = st.text_input("Nama Lengkap*")
            
            if peran_input == "👨‍🌾 Petani":
                kecamatan = ["Pilih Kecamatan...", "Bandar", "Bawang", "Blado", "Batang Kota", "Gringsing", "Limpung", "Pecalungan", "Reban", "Subah", "Tersono", "Tulis", "Warungasem"]
                lokasi_input = st.selectbox("Domisili Lahan (Kecamatan)*:", kecamatan)
            else:
                pasar = ["Pilih Pasar...", "Pasar Induk Kabupaten Batang", "Pasar Limpung", "Pasar Bandar", "Pasar Bawang", "Pasar Subah", "Pasar Tersono"]
                lokasi_input = st.selectbox("Lokasi Pasar*:", pasar)
            
            if st.button("Masuk ke Dashboard 🚀", type="primary", use_container_width=True):
                if len(nik_input) != 16 or not nik_input.isdigit():
                    st.error("⚠️ Gagal: NIK harus berupa tepat 16 digit angka!")
                elif nama_input == "" or "Pilih" in lokasi_input:
                    st.error("⚠️ Gagal: Pastikan Nama dan Lokasi sudah terisi!")
                else:
                    st.session_state['sudah_login'] = True
                    st.session_state['nama_user'] = nama_input
                    st.session_state['peran'] = peran_input
                    st.session_state['lokasi'] = lokasi_input
                    st.rerun()


# ==========================================
# HALAMAN 2: DASHBOARD PETANI (AI + Grafik Pasar + Terjemahan)
# ==========================================
def dashboard_petani():
    model_agrolink = joblib.load('model_cerdas_agrolink.joblib')

    st.sidebar.success(f"👋 Halo, Bapak/Ibu **{st.session_state['nama_user']}**!")
    st.sidebar.write(f"📍 Area Lahan: **Kec. {st.session_state['lokasi']}**")
    st.sidebar.markdown("---")
    
    st.sidebar.header("⚙️ Sensor Lahan (Input)")
    n = st.sidebar.number_input("Nitrogen (N)", value=90)
    p = st.sidebar.number_input("Fosfor (P)", value=42)
    k = st.sidebar.number_input("Kalium (K)", value=43)
    suhu = st.sidebar.number_input("Suhu (°C)", value=28.0)
    kelembapan = st.sidebar.number_input("Kelembapan (%)", value=82.0)
    ph = st.sidebar.number_input("pH Tanah", value=6.5)
    hujan = st.sidebar.number_input("Curah Hujan (mm)", value=200.0)
    
    st.sidebar.markdown("---")
    if st.sidebar.button("Keluar (Logout)", type="primary"):
        st.session_state['sudah_login'] = False
        st.rerun()

    st.title("🌾 Dashboard Kecerdasan Buatan (Petani)")
    st.write(f"Rekomendasi tanam cerdas untuk wilayah **{st.session_state['lokasi']}**.")
    st.markdown("---")

    if st.button("Analisis Lahan Sekarang 🚀"):
        rekomendasi = model_agrolink.predict([[n, p, k, suhu, kelembapan, ph, hujan]])
        hasil_inggris = rekomendasi[0].lower() 
        
        # --- KAMUS PENERJEMAH OTOMATIS (KOMPLIT 22 TANAMAN) ---
        kamus_tanaman = {
            "rice": "PADI / BERAS",
            "maize": "JAGUNG",
            "kidneybeans": "KACANG MERAH",
            "coffee": "KOPI",
            "orange": "JERUK",
            "apple": "APEL",
            "watermelon": "SEMANGKA",
            "banana": "PISANG",
            "grapes": "ANGGUR",
            "mango": "MANGGA",
            "cotton": "KAPAS",
            "mothbeans": "KACANG MOTH",
            "mungbean": "KACANG HIJAU",
            "blackgram": "KACANG HITAM",
            "lentil": "LENTIL",
            "pomegranate": "DELIMA",
            "papaya": "PEPAYA",
            "coconut": "KELAPA",
            "jute": "GONI",
            "chickpea": "KACANG ARAB",
            "pigeonpeas": "KACANG GUDE",
            "muskmelon": "BLEWAH"
        }
        
        hasil_indonesia = kamus_tanaman.get(hasil_inggris, hasil_inggris.upper())
        
        st.success(f"🌟 Tanaman yang Paling Direkomendasikan: **{hasil_indonesia}**")
        st.balloons() 
    
    st.markdown("---")
    st.write("### 📊 Pantauan Harga Pasar di Kabupaten Batang")
    st.info("Arahkan kursor Anda ke diagram batang di bawah ini untuk melihat detail harga per pasar.")
    
    if not st.session_state['database_pasar'].empty:
        df = st.session_state['database_pasar']
        fig = px.bar(df, x="Komoditas", y="Harga Beli/Kg (Rp)", color="Pasar", barmode="group",
                     title="Perbandingan Harga Beli Komoditas Tertinggi Saat Ini",
                     text_auto='.2s')
        fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
        st.plotly_chart(fig, use_container_width=True)
        
        with st.expander("Klik di sini untuk melihat Tabel Detail Harga"):
            st.dataframe(df, use_container_width=True)
    else:
        st.warning("Belum ada data pasar yang diunggah.")

# ==========================================
# HALAMAN 3: DASHBOARD PENJUAL (Input Pasar)
# ==========================================
def dashboard_penjual():
    st.sidebar.success(f"👋 Halo, Juragan **{st.session_state['nama_user']}**!")
    st.sidebar.write(f"📍 Lokasi: **{st.session_state['lokasi']}**")
    st.sidebar.markdown("---")
    if st.sidebar.button("Keluar (Logout)", type="primary"):
        st.session_state['sudah_login'] = False
        st.rerun()

    st.title("🛒 Dashboard Pengepul & Pasar")
    st.write("Perbarui harga beli dan kuota stok agar petani tahu tanaman apa yang sedang Anda butuhkan.")
    st.markdown("---")

    with st.form("form_pasar"):
        st.write("### ➕ Tambah Permintaan Komoditas")
        col1, col2, col3 = st.columns(3)
        with col1:
            komoditas = st.selectbox("Jenis Tanaman", ["Padi / Beras", "Jagung", "Kacang Merah", "Kopi", "Jeruk", "Lainnya"])
        with col2:
            harga = st.number_input("Harga Beli / Kg (Rp)", min_value=0, step=500, value=12000)
        with col3:
            stok = st.number_input("Kebutuhan Stok (Kg)", min_value=0, step=10, value=100)
            
        tombol_simpan = st.form_submit_button("Simpan ke Database Pasar")
        
        if tombol_simpan:
            data_baru = pd.DataFrame([{
                "Pasar": st.session_state['lokasi'],
                "Pedagang": st.session_state['nama_user'],
                "Komoditas": komoditas,
                "Harga Beli/Kg (Rp)": harga,
                "Stok Tersedia (Kg)": stok
            }])
            st.session_state['database_pasar'] = pd.concat([st.session_state['database_pasar'], data_baru], ignore_index=True)
            st.success("✅ Data berhasil diumumkan ke seluruh petani Batang!")

    st.markdown("---")
    st.write("### 📋 Semua Permintaan Komoditas Aktif")
    st.dataframe(st.session_state['database_pasar'], use_container_width=True)


# ==========================================
# PENGATUR LALU LINTAS HALAMAN (ROUTER)
# ==========================================
if st.session_state['sudah_login'] == False:
    halaman_login()
elif st.session_state['peran'] == "👨‍🌾 Petani":
    dashboard_petani()
elif st.session_state['peran'] == "🛒 Penjual (Pedagang Pasar)":
    dashboard_penjual()