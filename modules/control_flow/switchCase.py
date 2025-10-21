import streamlit as st
from streamlit_ace import st_ace
from core.base_module import BaseModule
from utils.piston_api import run_java_code


class SwitchCaseModule(BaseModule):
    def run(self):
        self.show_title()

        st.markdown("## 🔀 Percabangan Switch Case di Java")
        st.write("""
        Selain `if-else`, Java juga menyediakan cara lain untuk menangani banyak pilihan yaitu **switch-case**.  
        `switch` cocok digunakan ketika kita ingin membandingkan satu variabel dengan banyak nilai kemungkinan.
        """)

        st.markdown("---")

        # ----------------------------- #
        st.markdown("### 🔹 1. Struktur Dasar Switch Case")
        st.write("Struktur umum switch case adalah seperti berikut:")

        st.code(
            """
switch (variabel) {
    case nilai1:
        // kode jika cocok dengan nilai1
        break;
    case nilai2:
        // kode jika cocok dengan nilai2
        break;
    default:
        // kode jika tidak ada yang cocok
        break;
}
""",
            language="java",
        )
        st.subheader("Cara Kerja")
        st.write("""
        - `switch` memeriksa nilai variabel.  
        - Jika cocok dengan `case`, blok kode di dalamnya dijalankan.  
        - Gunakan `break` agar tidak lanjut ke case berikutnya.  
        - `default` digunakan jika tidak ada case yang cocok.
        """)

        st.markdown("---")

        # ----------------------------- #
        st.markdown("### 🔹 2. Contoh Sederhana Switch Case")
        simple_example = """public class Main {
    public static void main(String[] args) {
        int hari = 3;

        switch (hari) {
            case 1:
                System.out.println("Senin");
                break;
            case 2:
                System.out.println("Selasa");
                break;
            case 3:
                System.out.println("Rabu");
                break;
            case 4:
                System.out.println("Kamis");
                break;
            case 5:
                System.out.println("Jumat");
                break;
            default:
                System.out.println("Akhir pekan!");
                break;
        }
    }
}"""
        st.code(simple_example, language="java")

        if st.button("▶️ Jalankan Contoh Switch Case"):
            output = run_java_code(simple_example)
            st.subheader("🖥️ Output:")
            st.code(output)

        st.markdown("---")

        # ----------------------------- #
        st.markdown("### 🔹 3. Switch dengan Input Pengguna")
        st.write("""
        Kita bisa juga menerima input dari user menggunakan `Scanner`.  
        Misalnya untuk menentukan nama hari berdasarkan angka.
        """)

        input_example = """import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Masukkan angka hari (1-7): ");
        int hari = input.nextInt();

        switch (hari) {
            case 1:
                System.out.println("Senin");
                break;
            case 2:
                System.out.println("Selasa");
                break;
            case 3:
                System.out.println("Rabu");
                break;
            case 4:
                System.out.println("Kamis");
                break;
            case 5:
                System.out.println("Jumat");
                break;
            case 6:
                System.out.println("Sabtu");
                break;
            case 7:
                System.out.println("Minggu");
                break;
            default:
                System.out.println("Angka tidak valid!");
                break;
        }
    }
}"""
        st.code(input_example, language="java")

        with st.expander("🧩 Coba Sendiri!", expanded=True):
            hari_input = st.text_input("Masukkan angka hari (1-7):", "3")
            if st.button("▶️ Jalankan Switch Input"):
                output = run_java_code(input_example, stdin_data=hari_input)
                st.code(output)

        st.markdown("---")

        # ----------------------------- #
        st.markdown("### 🔹 4. Nested Switch Case")
        st.write("""
        Seperti `if`, switch juga bisa **di-nested** atau disarang di dalam switch lain.  
        Misalnya, kita ingin menentukan nama mata kuliah berdasarkan hari dan sesi kuliah.
        """)

        nested_switch = """import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Masukkan hari (1=Senin, 2=Selasa): ");
        int hari = input.nextInt();

        System.out.print("Masukkan sesi (1=Pagi, 2=Siang): ");
        int sesi = input.nextInt();

        switch (hari) {
            case 1:
                switch (sesi) {
                    case 1:
                        System.out.println("Matkul: Algoritma");
                        break;
                    case 2:
                        System.out.println("Matkul: Pemrograman Dasar");
                        break;
                }
                break;
            case 2:
                switch (sesi) {
                    case 1:
                        System.out.println("Matkul: Basis Data");
                        break;
                    case 2:
                        System.out.println("Matkul: Struktur Data");
                        break;
                }
                break;
            default:
                System.out.println("Hari tidak valid!");
        }
    }
}"""
        st.code(nested_switch, language="java")

        with st.expander("🧩 Jalankan Nested Switch", expanded=True):
            hari_val = st.text_input("Masukkan hari (1/2):", "1")
            sesi_val = st.text_input("Masukkan sesi (1/2):", "2")
            combined_input = f"{hari_val}\n{sesi_val}"
            if st.button("▶️ Jalankan Nested Switch"):
                output = run_java_code(nested_switch, stdin_data=combined_input)
                st.code(output)

        st.markdown("---")

        # ----------------------------- #
        st.markdown("### 🧠 5. Mini Quiz: Switch Case Interaktif (Dengan st_ace)")
        st.write("""
        Buat program untuk menentukan **bulan berdasarkan angka (1–12)**  
        menggunakan **switch-case**. Jika angkanya di luar 1–12, tampilkan “Bulan tidak valid”.
        """)

        default_code = """import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Masukkan angka bulan (1-12): ");
        int bulan = input.nextInt();

        // TODO: Lengkapi logika switch-case di bawah ini
        
    }
}"""

        user_code = st_ace(
            value=default_code,
            language="java",
            theme="dracula",
            height=300,
            key="ace_switchcase_quiz",
            font_size=14,
            show_gutter=True,
            wrap=True,
            auto_update=True,
        )

        bulan_input = st.text_input("Masukkan angka untuk diuji:", "5")

        if st.button("▶️ Jalankan Kode Saya"):
            output = run_java_code(user_code, stdin_data=bulan_input)
            st.subheader("🖥️ Output:")
            st.code(output)

       


def run():
    SwitchCaseModule("Switch Case").run()
