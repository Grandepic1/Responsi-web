import streamlit as st
import streamlit.components.v1 as components
from core.base_module import BaseModule
from PIL import Image
import re

img = Image.open(r"images/algoritma.png")


class IntroModule(BaseModule):
    def run(self):
        self.show_title()
        st.write(
            """
        Halo! 👋  
        Di subbab ini kita akan belajar tentang **algoritma** dan **variabel**.  
        Anggap saja kamu lagi belajar membuat resep kue 🍰 — algoritma adalah langkah-langkahnya,  
        dan variabel adalah wadah untuk menyimpan bahan-bahannya.
        """
        )
        st.subheader("🧠 Apa itu Algoritma?")
        st.write("""
        Algoritma adalah serangkaian instruksi atau langkah-langkah logis dan sistematis yang berurutan untuk menyelesaikan suatu masalah atau mencapai tujuan tertentu.
        """)
        st.image(img, caption="Contoh Algoritma")
        st.markdown('---')
        st.subheader("📦 Apa itu Variabel?")
        st.write(
            """
        Variabel adalah tempat menyimpan data.  
        Misalnya kamu ingin menyimpan umurmu:
        """
        )
        st.code("""int umur = 19;""", language="java")
        st.info(
            "`int` adalah tipe data (bilangan bulat), `umur` adalah nama variabel, dan `19` nilainya."
        )

        st.write(
            """
        Variabel adalah tempat penyimpanan data sementara, diibaratkan sebagai wadah yang menampung "sesuatu" (data) sesuai tipenya.    
        Sebuah variabel terdiri dari tipe data (misalnya int untuk bilangan bulat), nama variabel (identifier), operator penugasan (=), dan nilai (value) yang disimpan.    
        Java memiliki reserved keywords yang tidak bisa digunakan sebagai nama variabel. Variabel bisa dideklarasikan (hanya mendefinisikan) dan di-assign (memberi nilai) secara terpisah. 
        Penamaan variabel disarankan menggunakan camelCase.
        """
        )

        q = st.radio(
            "Manakah yang merupakan deklarasi variabel yang benar?",
            ["int angka = 10;", "integer angka = 10;", "num angka = 10;"], index=None
        )
        if st.button("Cek Jawaban", key="1", disabled=(q is None)):
            if q == "int angka = 10;":
                self.success_msg("✅ Betul! `int` adalah tipe data bawaan Java.")
            else:
                self.error_msg(
                    "❌ Salah. Java tidak mengenal `integer` atau `num` sebagai keyword."
                )
        st.markdown('---')
        st.subheader('Praktik Variable')
        st.write("""
Tulislah kode untuk membuat variabel **String** bernama `kelas` dan isi dengan kelasmu (nilai bebas).
""")
        code1 = st.text_area(
            "Tulis kode Java di sini:",
            height=100,
        )
        if st.button("✅ Periksa Jawaban"):
    # Hapus spasi berlebih dan newline
            code_clean = code1.strip()

            # Pola regex untuk cek sintaks: String kelas = "isi";
            pattern = r'^String\s+kelas\s*=\s*".*"\s*;$'

            # Cek kosong
            if not code_clean:
                st.warning("⚠️ Kamu belum menulis kode apa pun.")
            # Cek sesuai format
            elif re.match(pattern, code_clean):
                st.success("✅ Hebat! Kode kamu sudah benar dan sesuai sintaks Java.")
            # Cek kalau lupa titik koma
            elif re.match(r'^String\s+kelas\s*=\s*".*"$', code_clean):
                st.warning("⚠️ Hampir benar! Jangan lupa titik koma (;) di akhir baris.")
            # Cek kalau nama variabel salah
            elif "String" in code_clean and "kelas" not in code_clean:
                st.error("❌ Nama variabel harus `kelas`, bukan nama lain.")
            # Cek kalau tipe data bukan String
            elif "String" not in code_clean:
                st.error("❌ Gunakan tipe data `String` untuk membuat variabel teks.")
            else:
                st.error("❌ Format belum sesuai. Pastikan menggunakan tanda kutip ganda dan titik koma.")

        st.caption(
            "💡 Gunakan format: [Tipe data] [nama variable terserah kalian] = [isi];"
        )
        st.markdown('---')
        st.subheader("Mindmap by Keyla")

        figma = """
        <iframe style="border: 1px solid rgba(0, 0, 0, 0.1);" width="800" height="450" src="https://embed.figma.com/board/oQRm1qM0lDgeLLLLy5HvBU/Mindmap-Responsi-IMA?node-id=0-1&embed-host=share" allowfullscreen></iframe>"""
        components.html(figma, height=450, scrolling=True)
        


def run():
    IntroModule("Variabel dan Algoritma").run()
