import streamlit as st
import joblib
import pandas as pd
import plotly.express as px

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
if 'no_hp' not in st.session_state:
    st.session_state['no_hp'] = ""

# TRIK PRESENTASI: Data awal sudah ditambah kolom "Nomor WA"
if 'database_pasar' not in st.session_state:
    data_awal = {
        "Pasar": ["Pasar Limpung", "Pasar Induk Kabupaten Batang", "Pasar Bawang", "Pasar Bandar"],
        "Pedagang": ["Haji Somad", "Bu Tejo", "Pak Slamet", "Koh Ahong"],
        "Nomor WA": ["081234567890", "081987654321", "085612341234", "082199998888"],
        "Komoditas": ["Padi / Beras", "Kopi", "Jagung", "Kacang Merah"],
        "Harga Beli/Kg (Rp)": [12500, 35000, 8000, 22000],
        "Stok Tersedia (Kg)": [500, 150, 800, 300]
    }
    st.session_state['database_pasar'] = pd.DataFrame(data_awal)


# ==========================================
# HALAMAN 1: LANDING PAGE & FORM LOGIN
# ==========================================
def halaman_login():
# --- BAGIAN 0: NAVIGATION BAR (NAVBAR BACKGROUND HIJAU MENTOK ATAS) ---
    st.markdown("""
        <style>
        /* 1. Menghilangkan ruang kosong (padding) di paling atas layar */
        .block-container {
            padding-top: 0rem !important;
        }
        /* 2. Menghapus / menyembunyikan header putih bawaan Streamlit */
        header {
            visibility: hidden !important;
        }
        </style>
        
        <div style="
            background-color: #2e7d32; 
            padding: 15px 50px; 
            width: 100vw; 
            position: relative; 
            left: 50%; 
            right: 50%; 
            margin-left: -50vw; 
            margin-right: -50vw; 
            margin-top: 0px; /* 🔧 PERBAIKAN: Diubah jadi 0 agar tidak terbang ke luar layar */
            display: flex; 
            justify-content: space-between; 
            align-items: center;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            z-index: 100;
        ">
            <div style="font-weight: 800; font-size: 20px; color: white; letter-spacing: 1px;">🌾 AGRO-LINK</div>
            <div style="font-size: 15px;">
                <span style="color: white; margin-left: 20px; font-weight: 700; cursor: pointer; border-bottom: 2px solid white; padding-bottom: 2px;">Beranda</span>
                <span style="color: #c8e6c9; margin-left: 20px; font-weight: 600; cursor: pointer;">Tentang Kami</span>
                <span style="color: #c8e6c9; margin-left: 20px; font-weight: 600; cursor: pointer;">Fitur</span>
                <span style="color: #c8e6c9; margin-left: 20px; font-weight: 600; cursor: pointer;">Kontak</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # --- BAGIAN 1: HERO SECTION (JUDUL BACKGROUND PUTIH) ---
    st.markdown("""
        <style>
        .block-container { overflow-x: hidden; }
        </style>
        
        <div style="
            background-color: white; 
            padding: 60px 20px 40px 20px; 
            width: 100vw; 
            position: relative; 
            left: 50%; 
            right: 50%; 
            margin-left: -50vw; 
            margin-right: -50vw; 
        ">
            <h1 style='text-align: center; color: #2e7d32; font-size: 45px; margin-bottom: 10px;'>🌾 AGRO-LINK BATANG</h1>
            <h4 style='text-align: center; color: #555; margin-top: 0; font-weight: normal;'>Revolusi Pertanian Digital Kabupaten Batang Berbasis Kecerdasan Buatan</h4>
        </div>
    """, unsafe_allow_html=True)

# --- BAGIAN 2: PENJELASAN APLIKASI (BACKGROUND HIJAU FULL) ---
    st.markdown("""
    <div style="background-color: #2e7d32; padding: 60px 10%; width: 100vw; position: relative; left: 50%; right: 50%; margin-left: -50vw; margin-right: -50vw; color: white; margin-bottom: 40px; box-shadow: inset 0 4px 6px rgba(0,0,0,0.05);">
        <h2 style='text-align: center; color: white; margin-bottom: 30px;'>🌍 Mengapa AGRO-LINK Hadir di Batang?</h2>
        <div style="display: flex; gap: 20px; margin-bottom: 50px; flex-wrap: wrap;">
            <div style="flex: 1; min-width: 250px; background-color: rgba(255,255,255,0.1); padding: 25px; border-radius: 10px; border-left: 6px solid #ff5252;">
                <h4 style="margin-top: 0; color: #ffeb3b;">📉 Masalah Saat Ini:</h4>
                <p style="font-size: 15px; margin-bottom: 0;">Petani Batang sering mengalami kerugian akibat salah prediksi komoditas tanam dan harga jual yang anjlok karena rantai distribusi yang panjang (permainan tengkulak).</p>
            </div>
            <div style="flex: 1; min-width: 250px; background-color: rgba(255,255,255,0.1); padding: 25px; border-radius: 10px; border-left: 6px solid #69f0ae;">
                <h4 style="margin-top: 0; color: #69f0ae;">📈 Solusi AGRO-LINK:</h4>
                <p style="font-size: 15px; margin-bottom: 0;">Memberikan rekomendasi tanam presisi berbasis AI dan membuka transparansi harga pasar agar petani mendapatkan keuntungan finansial yang maksimal.</p>
            </div>
        </div>
        <h3 style='text-align: center; color: white; margin-bottom: 25px;'>Tiga Pilar Utama Inovasi Kami</h3>
        <div style="display: flex; gap: 20px; flex-wrap: wrap; text-align: center;">
            <div style="flex: 1; min-width: 200px; background-color: white; color: #333; padding: 25px; border-radius: 12px; box-shadow: 0 4px 8px rgba(0,0,0,0.2);">
                <h1 style="margin:0; font-size: 45px;">🤖</h1>
                <h4 style="color: #2e7d32; margin-bottom: 10px;">Smart Farming AI</h4>
                <p style="font-size: 14px; margin: 0; color: #555;">Analisis cerdas kondisi tanah dan cuaca untuk rekomendasi tanaman paling kebal & menguntungkan.</p>
            </div>
            <div style="flex: 1; min-width: 200px; background-color: white; color: #333; padding: 25px; border-radius: 12px; box-shadow: 0 4px 8px rgba(0,0,0,0.2);">
                <h1 style="margin:0; font-size: 45px;">📊</h1>
                <h4 style="color: #2e7d32; margin-bottom: 10px;">Transparansi Pasar</h4>
                <p style="font-size: 14px; margin: 0; color: #555;">Pantauan harga beli dan kebutuhan stok riil dari berbagai pasar di Batang secara terbuka.</p>
            </div>
            <div style="flex: 1; min-width: 200px; background-color: white; color: #333; padding: 25px; border-radius: 12px; box-shadow: 0 4px 8px rgba(0,0,0,0.2);">
                <h1 style="margin:0; font-size: 45px;">🤝</h1>
                <h4 style="color: #2e7d32; margin-bottom: 10px;">Potong Rantai Pasok</h4>
                <p style="font-size: 14px; margin: 0; color: #555;">Fitur kontak WhatsApp untuk negosiasi langsung antara petani dan pedagang pasar.</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # --- BAGIAN 3: FORM LOGIN ---
    st.write("<h3 style='text-align: center;'>Masuk ke Ekosistem</h3>", unsafe_allow_html=True)
    st.write("<p style='text-align: center;'>Silakan pilih peran Anda untuk memulai.</p>", unsafe_allow_html=True)
    
    col_kiri, col_tengah, col_kanan = st.columns([1, 2, 1])
    with col_tengah:
        with st.container(border=True):
            peran_input = st.radio("Masuk Sebagai:", ["Pilih Peran...", "👨‍🌾 Petani", "🛒 Penjual (Pedagang Pasar)"])
            
            if peran_input != "Pilih Peran...":
                st.markdown("<hr>", unsafe_allow_html=True)
                nik_input = st.text_input("Nomor Induk Kependudukan (NIK)*", placeholder="Masukkan 16 digit angka", max_chars=16)
                nama_input = st.text_input("Nama Lengkap*")
                hp_input = st.text_input("Nomor HP / WhatsApp*", placeholder="Contoh: 081234567890")
                
                if peran_input == "👨‍🌾 Petani":
                    kecamatan = ["Pilih Kecamatan...", "Bandar", "Bawang", "Blado", "Batang Kota", "Gringsing", "Limpung", "Pecalungan", "Reban", "Subah", "Tersono", "Tulis", "Warungasem"]
                    lokasi_input = st.selectbox("Domisili Lahan (Kecamatan)*:", kecamatan)
                else:
                    pasar = ["Pilih Pasar...", "Pasar Induk Kabupaten Batang", "Pasar Limpung", "Pasar Bandar", "Pasar Bawang", "Pasar Subah", "Pasar Tersono"]
                    lokasi_input = st.selectbox("Lokasi Pasar*:", pasar)
                
                if st.button("Masuk ke Dashboard", type="primary", use_container_width=True):
                    if len(nik_input) != 16 or not nik_input.isdigit():
                        st.error("⚠️ Gagal: NIK harus berupa tepat 16 digit angka!")
                    elif nama_input == "" or hp_input == "" or "Pilih" in lokasi_input:
                        st.error("⚠️ Gagal: Pastikan Nama, Nomor HP, dan Lokasi sudah terisi!")
                    else:
                        st.session_state['sudah_login'] = True
                        st.session_state['nama_user'] = nama_input
                        st.session_state['peran'] = peran_input
                        st.session_state['lokasi'] = lokasi_input
                        st.session_state['no_hp'] = hp_input
                        st.rerun()


# ==========================================
# HALAMAN 2: DASHBOARD PETANI
# ==========================================
def dashboard_petani():
    model_agrolink = joblib.load('model_cerdas_agrolink.joblib')

    st.sidebar.markdown(f"""
        <div style="
            background-color: #2e7d32; 
            padding: 15px; 
            border-radius: 10px; 
            color: white; 
            margin-bottom: 15px; 
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        ">
            <span style="font-size: 18px;">👋</span> Halo, Bapak/Ibu <b>{st.session_state['nama_user']}</b>!
        </div>
    """, unsafe_allow_html=True)
    st.sidebar.write(f"📍 Lahan: **Kec. {st.session_state['lokasi']}**")
    st.sidebar.write(f"📞 Kontak: **{st.session_state['no_hp']}**")
    st.sidebar.markdown("---")
    
    st.sidebar.header("Sensor Lahan (Input)")
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

    if st.button("Analisis Lahan Sekarang 🚀", type="primary", use_container_width=True):
        rekomendasi = model_agrolink.predict([[n, p, k, suhu, kelembapan, ph, hujan]])
        hasil_inggris = rekomendasi[0].lower() 
        
        kamus_tanaman = {
            "rice": "PADI / BERAS", "maize": "JAGUNG", "kidneybeans": "KACANG MERAH",
            "coffee": "KOPI", "orange": "JERUK", "apple": "APEL", "watermelon": "SEMANGKA",
            "banana": "PISANG", "grapes": "ANGGUR", "mango": "MANGGA", "cotton": "KAPAS",
            "mothbeans": "KACANG MOTH", "mungbean": "KACANG HIJAU", "blackgram": "KACANG HITAM",
            "lentil": "LENTIL", "pomegranate": "DELIMA", "papaya": "PEPAYA", "coconut": "KELAPA",
            "jute": "GONI", "chickpea": "KACANG ARAB", "pigeonpeas": "KACANG GUDE", "muskmelon": "BLEWAH"
        }
        hasil_indonesia = kamus_tanaman.get(hasil_inggris, hasil_inggris.upper())
        
        st.success(f"🌟 Tanaman yang Paling Direkomendasikan: **{hasil_indonesia}**")
        st.balloons() 
    
    st.markdown("---")
    st.write("### 📊 Pantauan Harga Pasar di Kabupaten Batang")
    st.info("Arahkan kursor atau sentuh diagram batang di bawah ini untuk melihat detail harga.")
    
    st.markdown("""
        <style>
        [data-testid="stPlotlyChart"] { overflow-x: auto; }
        </style>
    """, unsafe_allow_html=True)
    
    if not st.session_state['database_pasar'].empty:
        df = st.session_state['database_pasar']
        
        fig = px.bar(df, x="Komoditas", y="Harga Beli/Kg (Rp)", color="Pasar", barmode="group",
                     title="Perbandingan Harga Beli Komoditas Tertinggi", text_auto='.2s')
        fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
        fig.update_layout(width=900, height=500) 
        st.plotly_chart(fig, use_container_width=False)
        
        with st.expander("Klik di sini untuk melihat Tabel Detail Kontak & Harga"):
            st.dataframe(df, use_container_width=True)
    else:
        st.warning("Belum ada data pasar yang diunggah.")


# ==========================================
# HALAMAN 3: DASHBOARD PENJUAL
# ==========================================
def dashboard_penjual():
    st.sidebar.markdown(f"""
        <div style="background-color: #2e7d32; padding: 15px; border-radius: 10px; color: white; margin-bottom: 15px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
            <span style="font-size: 18px;">👋</span> Halo, Juragan <b>{st.session_state['nama_user']}</b>!
        </div>
    """, unsafe_allow_html=True)
    st.sidebar.write(f"📍 Pasar: **{st.session_state['lokasi']}**")
    st.sidebar.write(f"📞 Kontak WA: **{st.session_state['no_hp']}**")
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
                "Nomor WA": st.session_state['no_hp'], # Memasukkan Nomor HP ke tabel
                "Komoditas": komoditas,
                "Harga Beli/Kg (Rp)": harga,
                "Stok Tersedia (Kg)": stok
            }])
            st.session_state['database_pasar'] = pd.concat([st.session_state['database_pasar'], data_baru], ignore_index=True)
            st.success("✅ Data dan kontak Anda berhasil diumumkan ke seluruh petani Batang!")

    st.markdown("---")
# --- SIHIR CSS UNTUK FORM HIJAU & INPUT PUTIH (REVISI WARNA HITAM) ---
    st.markdown("""
        <style>
        /* 1. Menyulap Kotak Form Utama menjadi Hijau Pekat */
        [data-testid="stForm"] {
            background-color: #2e7d32 !important;
            padding: 25px !important;
            border-radius: 15px !important;
            border: none !important;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1) !important;
        }
        
        /* 2. Mengubah tulisan Label & Judul menjadi Putih */
        [data-testid="stForm"] p, 
        [data-testid="stForm"] h3, 
        [data-testid="stForm"] label {
            color: white !important;
        }

        /* 3. Memaksa Kotak Input menjadi Putih Bersih */
        [data-testid="stForm"] div[data-baseweb="base-input"],
        [data-testid="stForm"] div[data-baseweb="select"] > div {
            background-color: white !important;
            border: none !important;
            border-radius: 8px !important;
        }
        
        /* 4. MENGUBAH WARNA ANGKA & TEKS INPUT MENJADI HITAM PEKAT */
        [data-testid="stForm"] input, 
        [data-testid="stForm"] div[data-baseweb="select"] span {
            color: #000000 !important; 
            -webkit-text-fill-color: #000000 !important;
            font-weight: 900 !important;
        }
        
        /* 5. MEMUNCULKAN KEMBALI TULISAN DI TOMBOL SIMPAN (HITAM PEKAT) */
        [data-testid="stForm"] button p {
            color: #000000 !important; 
            font-weight: bold !important;
        }
        [data-testid="stForm"] button {
            border: 2px solid #e0e0e0 !important;
        }
        
        /* 6. Mengubah warna ikon plus/minus & panah menjadi hitam */
        [data-testid="stForm"] svg {
            fill: #000000 !important; 
        }
        </style>
    """, unsafe_allow_html=True)
    st.write("### 📋 Semua Permintaan Komoditas Aktif")
    st.dataframe(st.session_state['database_pasar'], use_container_width=True)


# ==========================================
# PENGATUR LALU LINTAS HALAMAN
# ==========================================
if st.session_state['sudah_login'] == False:
    halaman_login()
elif st.session_state['peran'] == "👨‍🌾 Petani":
    dashboard_petani()
elif st.session_state['peran'] == "🛒 Penjual (Pedagang Pasar)":
    dashboard_penjual()

# ==========================================
# FOOTER APLIKASI (FULL WIDTH & MENTOK BAWAH)
# ==========================================
st.markdown("<br><br>", unsafe_allow_html=True) 
st.markdown("""
    <style>
    /* 1. Menghilangkan watermark bawaan Streamlit di paling bawah */
    footer {visibility: hidden;}
    
    /* 2. Menghapus ruang kosong (padding) bawaan Streamlit di dasar layar */
    .block-container {
        padding-bottom: 0px !important;
    }
    </style>
    
    <div style="
        background-color: #1b5e20; 
        padding: 40px 20px 60px 20px; /* Padding bawah diperbesar agar tebal ke dasar */
        text-align: center; 
        color: white; 
        margin-top: 40px;
        width: 100vw; 
        position: relative; 
        left: 50%; 
        right: 50%; 
        margin-left: -50vw; 
        margin-right: -50vw;
        margin-bottom: -100px; /* Sihir untuk menarik kotak menembus batas bawah */
    ">
        <p style="margin: 0; font-size: 15px; font-weight: bold;">© 2026 AGRO-LINK BATANG</p>
        <p style="margin: 5px 0; font-size: 14px; color: #c8e6c9;">Mewujudkan Ekosistem Pertanian Digital yang Cerdas dan Transparan.</p>
        <p style="margin: 0; font-size: 12px; color: #a5d6a7;"><i>Dikembangkan oleh Mahasiswa Institut Widya Pratama untuk KRENOVA Kabupaten Batang 2026</i></p>
    </div>
""", unsafe_allow_html=True)