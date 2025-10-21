import streamlit as st
from core.base_module import BaseModule


class SummaryModule(BaseModule):
    def run(self):
        self.show_title()
        st.write("""
        🎯 Selamat! Kamu sudah mempelajari:
        - Apa itu variabel dan tipe data
        - Cara menggunakan operator aritmatika & logika
        - Konsep konstanta `final`

        Sekarang waktunya latihan kecil!
        """)

        st.write(
            "💻 Buat program yang menampilkan hasil luas lingkaran dengan jari-jari 7 menggunakan `PI = 3.14`"
        )

        st.code(
            """
public class Main {
    static final double PI = 3.14;
    public static void main(String[] args) {
        int r = 7;
        double luas = PI * r * r;
        System.out.println(luas);
    }
}
""",
            language="java",
        )

        st.success("✅ Hasil yang benar adalah 153.86")


def run():
    SummaryModule("Ringkasan Modul 3").run()
