# World University Rankings Explorer (2016-2025)

Selamat datang di **World University Rankings Explorer**! 🎓 Aplikasi ini dirancang untuk mengeksplorasi data peringkat universitas dunia berdasarkan berbagai metrik selama periode 2016 hingga 2025. Dengan fitur interaktif dan visualisasi yang menarik, Anda dapat menjelajahi tren pendidikan tinggi global, menganalisis kinerja universitas, dan membandingkan institusi akademis secara menyeluruh. 🌍✨

---

## **Fitur Utama**

1. **Pratinjau Dataset**:

   - Lihat pratinjau dataset peringkat universitas dunia.
   - Periksa atribut seperti peringkat, populasi mahasiswa, skor penelitian, dan lainnya.

2. **10 Universitas Terbaik**:

   - Eksplorasi universitas terbaik berdasarkan tahun tertentu.
   - Visualisasi interaktif menggunakan grafik batang horizontal.

3. **Kinerja Universitas**:

   - Analisis tren peringkat universitas dari waktu ke waktu.
   - Lacak perubahan peringkat dan kinerja keseluruhan.

4. **Distribusi Universitas Berdasarkan Negara**:

   - Peta distribusi universitas berdasarkan negara.
   - Perbandingan jumlah universitas di berbagai negara dengan animasi tahunan.

5. **Pertumbuhan Populasi Mahasiswa**:

   - Visualisasi pertumbuhan populasi mahasiswa dari tahun ke tahun.
   - Analisis tren aksesibilitas pendidikan tinggi.

6. **Perbandingan Antar Universitas**:
   - Bandingkan dua universitas berdasarkan metrik seperti pengajaran, penelitian, dan kualitas penelitian.

---

## **Persiapan Sebelum Menjalankan**

### **Prasyarat**

- **Python 3.8+**
- **Streamlit** (versi terbaru)
- **Plotly** untuk visualisasi data
- **Pandas** untuk manipulasi data

### **Instalasi**

1. Pastikan Anda memiliki Python versi 3.8 atau lebih baru di sistem Anda.
2. Instal pustaka yang diperlukan dengan perintah berikut:

   ```bash
   pip install streamlit pandas plotly
   ```

3. Pastikan dataset **"THE World University Rankings 2016-2025.csv"** tersedia di direktori kerja Anda.

### **Sumber Dataset**

Dataset yang digunakan dalam aplikasi ini berasal dari [Kaggle: The World University Rankings 2016-2024](https://www.kaggle.com/datasets/raymondtoo/the-world-university-rankings-2016-2024). Harap unduh dataset ini dan pastikan formatnya sesuai dengan yang dijelaskan dalam dokumen ini.

---

## **Menjalankan Aplikasi**

1. Simpan kode aplikasi ini dalam file bernama `app.py`.
2. Pastikan file dataset **"THE World University Rankings 2016-2025.csv"** berada di direktori yang sama dengan `app.py`.
3. Jalankan aplikasi dengan perintah berikut di terminal atau command prompt:
   ```bash
   streamlit run app.py
   ```
4. Browser Anda akan otomatis membuka aplikasi. Jika tidak, buka URL yang ditampilkan di terminal (biasanya `http://localhost:8501`).

---

## **Catatan Penting**

- **Dataset**: Pastikan dataset sudah bersih dan berformat sesuai dengan kolom yang disebutkan di dalam kode. Jika ada kolom yang hilang, aplikasi akan memberikan pesan kesalahan.
- **Portabilitas**: Aplikasi ini dapat dijalankan di berbagai platform selama prasyaratnya terpenuhi.

---

## **Kontribusi**

Jika Anda ingin meningkatkan aplikasi ini, jangan ragu untuk membuat pull request atau melaporkan masalah di repositori proyek ini.

---

Nikmati eksplorasi data pendidikan tinggi global Anda! 🌟
