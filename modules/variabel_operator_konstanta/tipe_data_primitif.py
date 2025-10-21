import streamlit as st
from core.base_module import BaseModule
from utils.piston_api import run_java_code


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

        with st.expander("🧩 Contoh kode lengkap", expanded=True):
            st.code(
                """
public class ProgramDira {
    public static void main(String[] args) {
        byte iniByte = 100; // Menyimpan angka dari -128 sampai 127
        short iniShort = 1000; // Menyimpan angka dari -32768 sampai 32767
        int iniInt = 1000000; // Menyimpan angka dari -2147483648 sampai 2147483647
        long iniLong = 1000000000L; // Menyimpan angka dari -9223372036854775808 sampai 9223372036854775807
        float iniFloat = 10.10f; // Menyimpan angka desimal dengan 6-7 digit di belakang koma
        double iniDouble = 10.5135; // Menyimpan angka desimal dengan 15 digit di belakang koma
        char iniChar = 'A'; // Menyimpan karakter
        boolean benar = true; // Menyimpan nilai benar atau salah
        boolean salah = false;
    }
}
                """,
                language="java",
            )

        q = st.radio(
            "Tipe data apa yang cocok untuk angka desimal?",
            ["int", "float", "char", "boolean"], index=None
        )
        if st.button("Cek Jawaban", key="2", disabled=(q is None)):
            if q == "float":
                self.success_msg(
                    "✅ Betul! Gunakan `float` atau `double` untuk angka desimal."
                )
            else:
                self.error_msg(
                    "❌ Coba lagi. `float` digunakan untuk angka desimal pendek."
                )
        st.markdown('---')
        st.subheader("Penggunaan boolean")
        st.info(
            "Fact : `boolean` tidak hanya diisikan dengan True dan False, tapi bisa berisi perbandingan yang akan mengembalikan True dan False"
        )
        st.code(
            """boolean isGenap = 4%2 == 0; // Akan mengembalikan nilai True""",
            language="java",
        )
        st.write("Variable boolean ini bisa langsung dipakai di if-else")
        st.code(
            """
int umur = 20;
boolean isOver18 = umur>=18; // akan memberikan nilai True
if (isOver18){
    System.out.println("Kamu sudah bisa bekerja"); // karena isOver18 bernilai True maka line ini akan dieksekusi
} else{
    System.out.println("Kamu belum bisa bekerja");
}
""",
            language="java",
        )
        st.markdown('---')
        st.subheader("Double vs Float")
        st.write("""
        Double dan Float mempunyai fungsi utama yaitu menampilkan atau menyimpan nilai desimal.     
        Lalu apa perbedaanya?   \n
        Double
        - `double` adalah tipe data primitif di Java yang digunakan untuk menyimpan nilai desimal dengan presisi tinggi.
        - Ukuran memori `double` adalah 64 bit (8 byte).
        - `double` dapat menyimpan nilai desimal dengan presisi sekitar 15-16 digit desimal.
        - Rentang nilai `double` adalah dari 4.9E-324 sampai 1.8E308.   \n
        Float
        - `float` adalah tipe data primitif di Java yang digunakan untuk menyimpan nilai desimal dengan presisi rendah.
        - Ukuran memori `float` adalah 32 bit (4 byte).
        - `float` dapat menyimpan nilai desimal dengan presisi sekitar 6-7 digit desimal.
        - Rentang nilai `float` adalah dari 1.4E-45 sampai 3.4E38.

        Perbedaan Utama

        - Presisi: `double` memiliki presisi yang lebih tinggi daripada `float`.
        - Ukuran Memori: `double` memiliki ukuran memori yang lebih besar daripada `float`.
        - Rentang Nilai: `double` memiliki rentang nilai yang lebih luas daripada `float`.

        Kapan Menggunakan Double atau Float?

        - Gunakan `double` ketika Anda memerlukan presisi tinggi, seperti dalam perhitungan ilmiah, keuangan, atau statistik.
        - Gunakan `float` ketika Anda memerlukan presisi rendah, seperti dalam game, grafik, atau aplikasi mobile yang memerlukan penggunaan memori yang efisien.
                 """)
        st.info("Fact: Komputer tidak dapat menyimpan nilai desimal karena angka biner tidak dapat merepresentasikan angka dibelakang koma.")
        floatDoubleCode = """
public class Main {
    public static void main(String[] args) {
        float hasilFloat = 0.1f + 0.2f;
        double hasilDouble = 0.1 + 0.2;
        
        System.out.printf("%.20f\\n",hasilFloat);
        System.out.printf("%.20f",hasilDouble);
    }
}
                """
        
        with st.expander("🧩 Contoh kode lengkap", expanded=True):
            st.code(floatDoubleCode,language="java",)
        
        if st.button("▶️ Run Java Code"):
            output = run_java_code(floatDoubleCode)
            st.subheader("🖥️ Program Output:")
            st.code(output)
            st.write("""
Angka-angka acak di belakang koma yang kamu liat adalah contoh dari kesalahan pembulatan yang terjadi karena representasi biner dari float dan double.
Mengapa ini terjadi?
Komputer menggunakan sistem biner untuk merepresentasikan angka-angka, sedangkan kita menggunakan sistem desimal. Sistem biner menggunakan basis 2, sedangkan sistem desimal menggunakan basis 10. Karena itu, beberapa angka desimal tidak dapat diwakili secara tepat dalam sistem biner.
""")



def run():
    TipeDataModule("Tipe Data Primitif").run()
