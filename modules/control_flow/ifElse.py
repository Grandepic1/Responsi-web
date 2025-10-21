import streamlit as st
from core.base_module import BaseModule
from utils.piston_api import run_java_code


class ifElse(BaseModule):
    def run(self):
        self.show_title()

        st.markdown("## 🧩 Percabangan If-Else di Java")
        st.write("""
        Dalam pemrograman, **percabangan (if-else)** digunakan untuk membuat keputusan.
        Program bisa menjalankan perintah berbeda tergantung kondisi yang terjadi.
        """)

        st.markdown("---")

        # ----------------------------- #
        st.markdown("### 🔹 1. Struktur Dasar If-Else")
        st.write("""
        Bentuk paling sederhana dari `if`:
        """)

        st.code(
            """
if (kondisi) {
    // kode yang dijalankan jika kondisi benar
} else {
    // kode jika kondisi salah
}
""",
            language="java",
        )

        st.write("""
        Contoh:
        """)

        example_code = """public class Main {
    public static void main(String[] args) {
        int angka = 10;

        if (angka > 0) {
            System.out.println("Angka positif");
        } else {
            System.out.println("Angka negatif atau nol");
        }
    }
}"""
        st.code(example_code, language="java")

        if st.button("▶️ Jalankan Contoh If-Else"):
            output = run_java_code(example_code)
            st.subheader("🖥️ Hasil Output:")
            st.code(output)
        st.subheader("Cara Kerja")
        st.write("""
- Pernyataan if: Mengecek sebuah kondisi. Jika kondisi ini bernilai true (benar), maka kode di dalamnya akan dijalankan. \n
- Pernyataan else: Menjalankan kode di dalamnya jika kondisi pada if sebelumnya bernilai false (salah). \n
- Pernyataan else if (atau elif): Digunakan untuk menambahkan kondisi tambahan setelah if. Kode pada else if hanya akan dieksekusi jika kondisi if sebelumnya salah, dan kondisi else if itu sendiri bernilai benar. """)
        st.markdown("---")

        # ----------------------------- #
        st.markdown("### 🔹 2. If-Else dengan Input Pengguna")
        st.write("""
        Kita bisa membaca input dari pengguna menggunakan `Scanner`  
        untuk menentukan kondisi secara dinamis.
        """)

        code_input = """import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Masukkan usia kamu: ");
        int usia = input.nextInt();

        if (usia >= 17) {
            System.out.println("Kamu sudah cukup umur untuk membuat KTP.");
        } else {
            System.out.println("Kamu belum cukup umur untuk membuat KTP.");
        }
    }
}"""

        st.code(code_input, language="java")

        with st.expander("🧩 Coba Sendiri!", expanded=True):
            stdin_data = st.text_input("Masukkan nilai input (contoh: 16):", "16")
            if st.button("▶️ Jalankan Program If-Else dengan Input"):
                output = run_java_code(code_input, stdin_data=stdin_data)
                st.code(output)

        st.markdown("---")

        # ----------------------------- #
        st.markdown("### 🔹 3. Nested If-Else (If di Dalam If)")
        st.write("""
        **Nested if-else** artinya kita menulis percabangan di dalam percabangan lain.
        Ini berguna untuk mengecek kondisi lebih spesifik.
        """)

        st.code(
            """
if (nilai >= 90) {
    System.out.println("A");
} else {
    if (nilai >= 75) {
        System.out.println("B");
    } else {
        System.out.println("C");
    }
}
""",
            language="java",
        )

        nested_example = """import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Masukkan nilai kamu: ");
        int nilai = input.nextInt();

        if (nilai >= 90) {
            System.out.println("Nilai kamu A (Sangat Baik)");
        } else {
            if (nilai >= 75) {
                System.out.println("Nilai kamu B (Cukup Baik)");
            } else {
                System.out.println("Nilai kamu C (Perlu Belajar Lagi)");
            }
        }
    }
}"""

        st.code(nested_example, language="java")

        with st.expander("🧩 Coba Nested If-Else", expanded=True):
            user_input = st.text_input("Masukkan nilai (contoh: 82):", "82")
            if st.button("▶️ Jalankan Nested If-Else"):
                output = run_java_code(nested_example, stdin_data=user_input)
                st.code(output)

        st.markdown("---")

        # ----------------------------- #
        st.markdown("### 🔹 4. Gabungan Else-If (Lebih Rapi dari Nested If)")
        st.write("""
        Kadang, kita bisa menulis percabangan yang lebih rapi menggunakan **else-if**  
        dibanding menumpuk if di dalam if.
        """)

        else_if_example = """import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Masukkan nilai kamu: ");
        int nilai = input.nextInt();

        if (nilai >= 90) {
            System.out.println("Nilai kamu A");
        } else if (nilai >= 75) {
            System.out.println("Nilai kamu B");
        } else if (nilai >= 60) {
            System.out.println("Nilai kamu C");
        } else {
            System.out.println("Nilai kamu D");
        }
    }
}"""

        st.code(else_if_example, language="java")

        with st.expander("🧩 Jalankan Else-If", expanded=True):
            user_score = st.text_input("Masukkan nilai (contoh: 95):", "95")
            if st.button("▶️ Jalankan Else-If"):
                output = run_java_code(else_if_example, stdin_data=user_score)
                st.code(output)

        st.markdown("---")
        st.subheader("Analogi")
        st.write("""Kamu bisa menganggapnya seperti petugas di perlintasan kereta yang mengatur arah kereta berdasarkan kondisi yang ada. Jika kondisi "rel lurus" terpenuhi (if), kereta jalan di jalur itu. Jika kondisi "rel lurus" salah (else), kereta akan mengambil jalur lain. 
""")

def run():
    ifElse("If Else dan Nested If").run()

        