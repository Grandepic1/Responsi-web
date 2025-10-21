import streamlit as st
from core.base_module import BaseModule


class TipeDataModule(BaseModule):
    def run(self):
        self.show_title()
        st.subheader("Tipe Data Primitif")
        st.write(
            """
        Tipe Data Primitif adalah jenis data dasar yang tidak dapat dipecah lebih lanjut dan menyimpan nilai sederhana secara langsung di memori    
        Java memiliki **8 tipe data primitif**, yaitu:
        byte, short, int, long, float, double, char, dan boolean.  
        Tipe data ini digunakan untuk menentukan jenis nilai yang disimpan dalam variabel.
        """
        )

        with st.expander("🧩 Contoh kode lengkap",expanded=True):
            st.code(
                """
public class ProgramDira {
    public static void main(String[] args) {
        byte iniByte = 100;
        short iniShort = 1000;
        int iniInt = 1000000;
        long iniLong = 1000000000L;
        float iniFloat = 10.10f;
        double iniDouble = 10.5135;
        char iniChar = 'A';
        boolean benar = true;
        boolean salah = false;
    }
}
""",
                language="java",
            )

        q = st.radio(
            "Tipe data apa yang cocok untuk angka desimal?",
            ["int", "float", "char", "boolean"],
        )
        if st.button("Cek Jawaban", key="2"):
            if q == "float":
                self.success_msg(
                    "✅ Betul! Gunakan `float` atau `double` untuk angka desimal."
                )
            else:
                self.error_msg(
                    "❌ Coba lagi. `float` digunakan untuk angka desimal pendek."
                )
        st.subheader("Penggunaan boolean:")
        st.info(
            "Fact : `boolean` tidak hanya diisikan dengan True dan False, tapi bisa berisi perbandingan atau statement yang akan mengembalikan True dan False"
        )
        st.code(
            """boolean isGenap = 4%2 == 0; // Akan mengembalikan nilai True""",
            language="java",
        )


def run():
    TipeDataModule("Tipe Data Primitif dan Objek").run()
