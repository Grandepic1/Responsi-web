import streamlit as st
from core.base_module import BaseModule
from utils.piston_api import run_java_code


class VariabelOperatorKonstantaModule(BaseModule):
    def run(self):
        self.show_title()
        st.write(
            "Halo! 👋 Selamat datang di modul *Variabel, Operator, dan Konstanta*."
        )
        st.write("""
        Modul ini akan membantu kamu memahami dasar pemrograman Java:
        - Apa itu **variabel**,  
        - Bagaimana menggunakan **operator**,  
        - Dan apa itu **konstanta**.  
        Yuk kita mulai!
        """)

        # ---------------- VARIABEL SECTION ----------------
        st.header("🧠 Apa itu Variabel?")
        st.write("""
        Bayangkan variabel seperti **wadah** yang bisa menyimpan data sementara.  
        Misalnya kamu punya kotak bernama `angka`, dan kamu simpan nilai 10 di dalamnya:
        """)
        st.code("""int angka = 10;""", language="java")
        st.info(
            "👉 `int` menunjukkan tipe data (bilangan bulat), `angka` adalah nama variabel, dan `10` adalah nilainya."
        )

        st.subheader("Latihan Cepat")
        q1 = st.radio(
            "Manakah yang benar untuk mendeklarasikan variabel umur bernilai 20?",
            [
                "int umur = 20;",
                "integer umur = 20;",
                "num umur = 20;",
                "var umur = 20;",
            ],
        )
        if st.button("Cek Jawaban 1"):
            if q1 == "int umur = 20;":
                self.success_msg("✅ Betul! `int` adalah tipe data yang benar di Java.")
            else:
                self.error_msg("❌ Salah. Gunakan `int` untuk bilangan bulat.")

        # ---------------- OPERATOR SECTION ----------------
        st.header("➕ Operator Aritmatika")
        st.write("""
        Operator digunakan untuk melakukan operasi matematika sederhana seperti tambah, kurang, kali, dan bagi:
        """)
        st.code(
            """
int a = 10;
int b = 5;
int hasil = a + b;
System.out.println("Hasil: " + hasil);
        """,
            language="java",
        )

        q2 = st.radio(
            "Apa output dari kode di atas?",
            ["Hasil: 15", "Hasil: 105", "Hasil: 5", "Error"],
        )
        if st.button("Cek Jawaban 2"):
            if q2 == "Hasil: 15":
                self.success_msg("✅ Tepat sekali! 10 + 5 = 15.")
            else:
                self.error_msg(
                    "❌ Coba hitung lagi deh, hasil penjumlahan yang benar 15."
                )

        # ---------------- KODE PRAKTIK ----------------
        st.header("💻 Coba Sendiri: Buat Programmu!")
        st.write("""
        Tulis program Java yang menampilkan hasil penjumlahan dari dua variabel `x` dan `y`  
        dengan nilai `x = 7` dan `y = 3`.
        """)

        default_code = """public class Main {
    public static void main(String[] args) {
        int x = 7;
        int y = 3;
        // Tulis kode untuk menampilkan hasil penjumlahan
    }
}"""
        code = st.text_area("✍️ Tulis kode di sini:", default_code, height=220)
        expected_output = "10\n"

        if st.button("▶️ Jalankan Program"):
            output = run_java_code(code)
            st.subheader("🖥️ Output Program:")
            st.code(output)
            if output == expected_output:
                self.success_msg("✅ Hebat! Kamu berhasil menampilkan hasil 10.")
            else:
                self.error_msg(
                    "❌ Output belum sesuai. Pastikan kamu menjumlahkan `x` dan `y` dan mencetak hasilnya."
                )
                st.info("Hint: Gunakan `System.out.println(x + y);`")

        # ---------------- KONSTANTA ----------------
        st.header("📏 Konstanta (final)")
        st.write("""
        Konstanta mirip variabel, tapi nilainya **tidak bisa diubah**.  
        Kita gunakan keyword `final` untuk mendeklarasikannya:
        """)
        st.code("""final double PI = 3.14;""", language="java")
        st.info(
            "💡 Biasanya nama konstanta ditulis dengan huruf besar semua, seperti `PI`."
        )

        st.success(
            "🎉 Bagus! Kamu sudah mempelajari dasar variabel, operator, dan konstanta di Java!"
        )
