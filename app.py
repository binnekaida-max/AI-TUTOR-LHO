import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="AI Tutor Bahasa Indonesia",
    page_icon="🤖",
    layout="wide"
)

# ==============================
# DATABASE
# ==============================

# Lokasi folder utama repositori GitHub
BASE_DIR = Path(__file__).resolve().parent

# Folder database berada satu tingkat dengan app.py
DATABASE_DIR = BASE_DIR / "database"
st.sidebar.write("Lokasi database:", DATABASE_DIR)
st.sidebar.write("Isi folder:", list(DATABASE_DIR.glob("*")))

def baca_file(nama_file):
    file_path = DATABASE_DIR / nama_file

    if file_path.exists():
        return file_path.read_text(encoding="utf-8")

    return f"File belum ditemukan: {file_path}"


materi_lho = baca_file(
    "TEKS LAPORAN HASIL OBSERVASI (LHO).txt"
)

lkpd = baca_file(
    "LEMBAR KERJA PESERTA DIDIK (LKPD).txt"
)


# ==============================
# MENU
# ==============================

st.sidebar.title("🤖 AI Tutor Bahasa Indonesia")

menu = st.sidebar.radio(
    "Menu",
    [
        "🏠 Beranda",
        "📚 Materi LHO",
        "📝 LKPD",
        "🎯 Kuis",
        "🤖 Tutor AI",
        "📖 Panduan"
    ]
)


# ==============================
# BERANDA
# ==============================

if menu == "🏠 Beranda":

    st.title("🤖 AI Tutor Bahasa Indonesia")

    st.subheader("Tutor AI Bahasa Indonesia Kelas X SMA")

    st.write("""
    Selamat datang di aplikasi pembelajaran
    **Teks Laporan Hasil Observasi (LHO)**.

    Aplikasi ini menyediakan materi, LKPD, kuis,
    Tutor AI, dan panduan penggunaan.
    """)

    st.info("""
    💡 **Cara belajar**

    1. Pelajari materi LHO.
    2. Kerjakan LKPD.
    3. Ikuti kuis.
    4. Gunakan Tutor AI jika mengalami kesulitan.
    5. Gunakan AI sebagai pendamping belajar.
    """)


# ==============================
# MATERI
# ==============================

elif menu == "📚 Materi LHO":

    st.title("📚 Materi Teks Laporan Hasil Observasi")

    st.write(
        "Pelajari materi berikut."
    )

    st.markdown(materi_lho)


# ==============================
# LKPD
# ==============================

elif menu == "📝 LKPD":

    st.title("📝 Lembar Kerja Peserta Didik")

    st.write(
        "Gunakan LKPD berikut untuk kegiatan pembelajaran."
    )

    st.markdown(lkpd)


# ==============================
# KUIS
# ==============================

elif menu == "🎯 Kuis":

    st.title("🎯 Kuis Teks Laporan Hasil Observasi")

    st.write("""
    Setelah mempelajari materi dan mengerjakan LKPD,
    silakan mengikuti kuis untuk menguji pemahamanmu.
    """)

    st.info("📌 Klik tombol di bawah untuk mengikuti kuis Kahoot.")

    st.link_button(
        "🎮 MULAI KUIS KAHOOT",
        "https://kahoot.it/challenge/02738889?challenge-id=ac42f31d-3ec7-4486-81ac-0b90d604046d_1791874280699"
    )

# ==============================
# TUTOR AI
# ==============================

elif menu == "🤖 Tutor AI":

    st.title("🤖 Tutor AI LHO")

    st.write("""
    Halo! 👋 Saya **LHO-AI Tutor**.

    Saya dapat membantu kamu memahami:

    • Pengertian LHO  
    • Tujuan LHO  
    • Struktur LHO  
    • Ciri kebahasaan  
    • Fakta dan opini  
    • Cara menganalisis LHO  
    • Cara membuat LHO
    """)

    st.warning(
        "💡 Gunakan AI sebagai pendamping belajar, "
        "bukan untuk mengerjakan seluruh tugas."
    )

    pertanyaan = st.text_area(
        "💬 Tulis pertanyaan kamu:",
        placeholder="Contoh: Apa itu teks laporan hasil observasi?",
        height=120
    )

    if st.button("🚀 Tanya Tutor AI"):

        if not pertanyaan.strip():

            st.warning(
                "Silakan tuliskan pertanyaan terlebih dahulu."
            )

        else:

            q = pertanyaan.lower()

            if "apa itu" in q or "pengertian" in q:

                jawaban = """
### 📚 Pengertian LHO

Teks Laporan Hasil Observasi (LHO) adalah teks yang
menyajikan informasi mengenai suatu objek berdasarkan
hasil pengamatan.

LHO disusun secara sistematis, objektif, dan berdasarkan fakta.

💭 **Coba pikirkan:**
Objek apa yang dapat kamu amati di lingkungan sekolah?
"""

            elif "tujuan" in q:

                jawaban = """
### 🎯 Tujuan LHO

Tujuan LHO adalah memberikan informasi mengenai suatu
objek berdasarkan hasil pengamatan secara jelas,
sistematis, dan faktual.

💭 **Pertanyaan:**
Mengapa LHO harus berdasarkan fakta?
"""

            elif "struktur" in q:

                jawaban = """
### 🧩 Struktur LHO

Struktur LHO terdiri dari:

**1. Pernyataan Umum**
Berisi pengenalan atau klasifikasi objek.

**2. Deskripsi Bagian**
Berisi ciri-ciri atau bagian-bagian objek.

**3. Deskripsi Manfaat**
Berisi manfaat atau fungsi objek jika relevan.

💭 **Latihan:**
Bagian mana yang menjelaskan ciri-ciri suatu objek?
"""

            elif "kebahasaan" in q or "bahasa" in q:

                jawaban = """
### ✏️ Ciri Kebahasaan LHO

Ciri kebahasaan LHO antara lain:

• kata benda  
• kata kerja  
• istilah khusus  
• kata sifat  
• kalimat definisi  
• kalimat deskripsi

Contoh kalimat definisi:

> Kucing merupakan hewan mamalia.

💭 **Latihan:**
Buat satu contoh kalimat definisi tentang benda di kelasmu.
"""

            elif "fakta" in q or "opini" in q:

                jawaban = """
### 🔎 Fakta dan Opini

**Fakta** adalah informasi yang berdasarkan kenyataan
dan dapat dibuktikan.

Contoh:

> Pohon mangga memiliki batang berkayu.

**Opini** adalah pendapat atau penilaian seseorang.

Contoh:

> Pohon mangga adalah tanaman yang paling indah.

LHO lebih mengutamakan fakta hasil observasi.

💭 **Latihan:**
Menurutmu, kalimat "Bunga itu sangat cantik"
termasuk fakta atau opini?
"""

            elif "cara membuat" in q or "membuat lho" in q:

                jawaban = """
### 📝 Cara Membuat LHO

1. Pilih objek yang akan diamati.
2. Lakukan pengamatan.
3. Catat fakta yang ditemukan.
4. Kelompokkan informasi.
5. Susun sesuai struktur LHO.
6. Periksa kembali tulisan.

⚠️ Jangan membuat data observasi yang sebenarnya
tidak kamu amati.

💭 Sekarang, objek apa yang ingin kamu amati?
"""

            else:

                jawaban = """
### 🤔 Mari kita belajar bersama

Coba tanyakan salah satu pertanyaan berikut:

• Apa itu LHO?
• Apa tujuan LHO?
• Apa struktur LHO?
• Apa ciri kebahasaan LHO?
• Apa perbedaan fakta dan opini?
• Bagaimana cara membuat LHO?

💡 Gunakan hasil pengamatanmu sendiri ketika mengerjakan tugas.
"""

            st.success("💡 Jawaban Tutor AI")

            st.markdown(jawaban)

            st.info(
                "💭 Sekarang coba jelaskan kembali dengan bahasamu sendiri."
            )


# ==============================
# PANDUAN
# ==============================

elif menu == "📖 Panduan":

    st.title("📖 Panduan Penggunaan AI Tutor")

    st.write("""
    ### Cara menggunakan AI Tutor

    **1. Memahami materi**

    Contoh:
    > Jelaskan pengertian teks laporan hasil observasi
    > dengan bahasa sederhana.

    **2. Memahami struktur**

    Contoh:
    > Jelaskan perbedaan pernyataan umum,
    > deskripsi bagian, dan deskripsi manfaat.

    **3. Latihan**

    Contoh:
    > Berikan saya pertanyaan latihan tentang LHO.

    **4. Memeriksa hasil observasi**

    Contoh:
    > Bantu saya mengecek hasil pengamatan saya.

    **5. Memperbaiki tulisan**

    Contoh:
    > Bantu saya menemukan bagian yang perlu diperbaiki
    > dalam teks LHO saya.
    """)

    st.warning(
        "⚠️ Jangan meminta AI mengerjakan seluruh tugas."
    )

    st.success(
        "✅ Gunakan AI sebagai pendamping belajar."
    ) 