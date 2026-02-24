\# 🌾 AGRO-LINK BATANG: Sistem Rekomendasi Tanam Berbasis Kecerdasan Buatan



AGRO-LINK BATANG adalah sebuah purwarupa (\*prototype\*) aplikasi \*website\* interaktif yang ditenagai oleh model \*Machine Learning\*. Sistem ini dirancang untuk menganalisis kondisi lahan secara \*real-time\* dan memberikan rekomendasi jenis tanaman pertanian terbaik guna mencegah risiko gagal panen.



\## 🎯 Cara Kerja Sistem

Aplikasi ini membaca 7 parameter utama dari lahan pertanian:

1\. Kandungan Nitrogen (N)

2\. Kandungan Fosfor (P)

3\. Kandungan Kalium (K)

4\. Suhu Udara (°C)

5\. Kelembapan Udara (%)

6\. pH Tanah

7\. Curah Hujan (mm)



Berdasarkan data input tersebut, "otak" AI (yang dilatih menggunakan algoritma \*\*C4.5 Decision Tree\*\* dengan akurasi \*\*98.4%\*\*) akan memproses pola lingkungan dan secara instan merekomendasikan tanaman yang paling optimal untuk ditanam di lahan tersebut.



\## 🛠️ Teknologi yang Digunakan

\* \*\*Bahasa Pemrograman:\*\* Python 3

\* \*\*Machine Learning:\*\* Scikit-learn (DecisionTreeClassifier)

\* \*\*Manipulasi Data:\*\* Pandas

\* \*\*Web Framework:\*\* Streamlit

\* \*\*Penyimpanan Model:\*\* Joblib



\## 🚀 Cara Menjalankan Aplikasi Secara Lokal

Jika Anda ingin menjalankan aplikasi ini di komputer Anda sendiri, ikuti langkah berikut:



1\. \*Clone\* repositori ini:

&nbsp;  `git clone https://github.com/Ubaidillah-24/agrolink-batang.git`

2\. Masuk ke dalam folder proyek:

&nbsp;  `cd agrolink-batang`

3\. Install semua \*library\* pendukung:

&nbsp;  `pip install -r requirements.txt`

4\. Jalankan aplikasi web:

&nbsp;  `streamlit run app\_agrolink.py`



---

\*Dibuat dengan ☕ dan 💻 untuk memajukan sektor pertanian.\*

