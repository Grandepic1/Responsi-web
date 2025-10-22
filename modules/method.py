import streamlit as st
from core.base_module import BaseModule
from utils.piston_api import run_java_code


class MethodModule(BaseModule):
    def run(self):
        st.title("🧩 Modul: Method (Fungsi) di Java")
        st.write("""
        Dalam pemrograman Java, **method** (atau fungsi) adalah blok kode yang digunakan untuk menjalankan tugas tertentu.  
        Dengan menggunakan method, kita bisa **mengorganisasi kode agar lebih rapi, efisien, dan mudah dibaca.**

        Secara sederhana, method membantu kita **menghindari penulisan ulang kode yang sama berulang kali.**
        """)

        st.markdown("---")

        # ----------------------------- #
        st.markdown("### 🔹 1. Struktur Dasar Method di Java")
        st.write("""
        Bentuk umum sebuah method di Java seperti berikut:
        """)

        st.code(
            """
returnType namaMethod(parameter1, parameter2, ...) {
    // isi method
    return nilai; // jika ada nilai balik
}
""",
            language="java",
        )

        st.write("""
        - **returnType** → Jenis data yang dikembalikan oleh method (`int`, `String`, `void`, dll)  
        - **namaMethod** → Nama dari method (biasanya diawali huruf kecil)  
        - **parameter** → Data yang dikirimkan ke method saat dipanggil  
        - **return** → Nilai yang dikembalikan ke pemanggil method  
        """)

        st.markdown("---")

        st.markdown("### 🔹 2. Contoh Method Sederhana")
        example_code = """public class Main {
    // method dengan return type int
    static int tambah(int a, int b) {
        return a + b;
    }

    public static void main(String[] args) {
        int hasil = tambah(5, 3);
        System.out.println("Hasil penjumlahan: " + hasil);
    }
}"""

        st.code(example_code, language="java")

        if st.button("▶️ Jalankan Contoh Method"):
            output = run_java_code(example_code)
            st.subheader("🖥️ Output:")
            st.code(output)

        st.info("""
        Pada contoh di atas:
        - Kita membuat method `tambah()` yang menerima dua parameter `a` dan `b`.  
        - Method tersebut mengembalikan hasil `a + b`.  
        - Di dalam `main()`, kita memanggil method `tambah(5, 3)` dan menampilkannya.
        """)

        st.markdown("---")

        # ----------------------------- #
        st.markdown("### 🔹 3. Method dengan Parameter dan Nilai Balik (Interaktif)")

        test_code_1 = """import java.util.Scanner;

public class Main {
    static int kali(int x, int y) {
        return x * y;
    }

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int a = input.nextInt();
        int b = input.nextInt();

        System.out.println("Hasil perkalian: " + kali(a, b));
    }
}"""

        with st.expander(
            "🧪 Coba Sendiri - Latihan 1 (Method dengan Parameter)", expanded=True
        ):
            st.code(test_code_1)
            st.write("Masukkan dua angka untuk dikalikan menggunakan method:")
            a = st.text_input("Angka pertama:", "4")
            b = st.text_input("Angka kedua:", "7")

            if st.button("▶️ Jalankan Latihan 1"):
                stdin_data = f"{a}\n{b}\n"
                output = run_java_code(test_code_1, stdin_data=stdin_data)
                st.subheader("🖥️ Output:")
                st.code(output)

        st.markdown("---")

        # ----------------------------- #
        st.markdown("### 🔹 4. Method Tanpa Nilai Balik (`void`) (Interaktif)")

        test_code_2 = """public class Main {
    static void sapa(String nama) {
        System.out.println("Halo, " + nama + "! Selamat belajar Java!");
    }

    public static void main(String[] args) {
        java.util.Scanner input = new java.util.Scanner(System.in);
        String nama = input.nextLine();

        sapa(nama);
    }
}"""
        with st.expander("🧪 Coba Sendiri - Latihan 2 (Method Void)", expanded=True):
            st.code(test_code_2)
            st.write("Masukkan nama kamu untuk disapa oleh program:")
            nama = st.text_input("Nama:")

            if st.button("▶️ Jalankan Latihan 2"):
                output = run_java_code(test_code_2, stdin_data=f"{nama}\n")
                st.subheader("🖥️ Output:")
                st.code(output)

        st.markdown("---")
        st.subheader("🧠 Ringkasan")
        st.write("""
        - **Method** digunakan untuk mengelompokkan logika dalam satu tempat agar mudah digunakan ulang.  
        - **Method dengan return** mengembalikan nilai menggunakan kata kunci `return`.  
        - **Method void** tidak mengembalikan nilai, biasanya hanya menampilkan hasil di layar.  
        - Parameter pada method membantu kita membuat fungsi yang dinamis dan fleksibel.
        """)


# agar otomatis dijalankan di Page Navigation
if __name__ == "__main__":
    MethodModule("Method di Java").run()
