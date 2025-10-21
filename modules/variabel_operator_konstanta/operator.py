import streamlit as st
from core.base_module import BaseModule
from utils.piston_api import run_java_code


class operator(BaseModule):
    def run(self):
        self.show_title()
        st.markdown("### 🔢 Operator Aritmatika")
        st.write("""
Operator Aritmatika adalah operator yang digunakan untuk operasi matematika.    
Dengan simbol :\n- \* (perkalian)\n- \- (Pengurangan) \n - \+ (Pertambahan) \n - / (Pembagian) \n - \% (Modulo)
""")
        code = """
public class Main {
    public static void main(String[] args) {
        int a = 20;
        int b = 5;
        // Pertambahan
        int pertambahan = a + b;
        System.out.println("Hasil pertambahan: " + pertambahan);
        // Pengurangan
        int pengurangan = a - b;
        System.out.println("Hasil pengurangan: " + pengurangan);
        // Perkalian
        int perkalian = a * b;
        System.out.println("Hasil perkalian: " + perkalian);
        // Pembagian
        int pembagian = a / b;
        System.out.println("Hasil pembagian: " + pembagian);
        // Sisa bagi (modulus)
        int modulus = a % b;
        System.out.println("Hasil modulus: " + modulus);
    }
}"""
        with st.expander("🧩 Contoh kode lengkap", expanded=True):
            st.code(
                code,
                language="java",
            )

            if st.button("▶️ Jalankan Operator"):
                output = run_java_code(code)
                st.code(output)
        
        st.markdown("### Operator Increment dan Decrement")
        st.write("""
        Operator **increment** (`++`) menambah 1 ke nilai variabel,  
        sedangkan **decrement** (`--`) mengurangi 1 dari nilai variabel.

        Ada dua jenis:
        - **Post-increment/decrement** → dilakukan **setelah** nilai digunakan.  
        - **Pre-increment/decrement** → dilakukan **sebelum** nilai digunakan.
        """)
        st.code(
            """
int a = 5;
int b = a++; // Post-increment: b=5, a=6
int c = 5;
int d = ++c; // Pre-increment: c=6, d=6
""",
            language="java",
        )

        with st.expander("💡 Penjelasan", expanded=True):
            st.write("""
            Pada `a++`, nilai `a` bertambah setelah digunakan,  
            sedangkan `++a` bertambah terlebih dahulu sebelum digunakan.
            """)

        with st.expander("🧩 Coba Sendiri!", expanded=True):
            st.write("Prediksi hasil dari kode berikut sebelum dijalankan:")
            user_code = """public class Main {
    public static void main(String[] args) {
        int x = 5;
        System.out.println(x++);
        System.out.println(++x);
    }
}"""
            st.code(user_code, language="java")
            if st.button("▶️ Jalankan Increment/Decrement"):
                output = run_java_code(user_code)
                st.code(output)

        st.markdown("---")

        # ----------------------------- #
        st.markdown("### 📝 Operator Penugasan (Assignment Operator)")
        st.write("""
        Operator penugasan digunakan untuk **memberi nilai ke variabel**.
        Operator ini memakai tanda sama dengan `=`.
        """)

        st.code(
            """
int x = 10; // x diberi nilai 10
x = x + 5;  // x sekarang bernilai 15
""",
            language="java",
        )

        st.markdown("---")

        # ----------------------------- #
        st.markdown("### Operator Perbandingan (Comparison Operator)")
        st.write("""
        Operator ini digunakan untuk membandingkan dua nilai dan menghasilkan **boolean** (`true` atau `false`).
        """)

        st.code(
            """
int a = 10, b = 10, c = 5;

System.out.println(a == b); // true
System.out.println(a != c); // true
System.out.println(a > c);  // true
System.out.println(a < c);  // false
System.out.println(a >= b); // true
System.out.println(a <= c); // false
""",
            language="java",
        )

        with st.expander("🧩 Jalankan Contoh", expanded=True):
            code_compare = """public class Main {
    public static void main(String[] args) {
        int a = 10, b = 10, c = 5;
        System.out.println(a == b);
        System.out.println(a != c);
        System.out.println(a > c);
        System.out.println(a < c);
        System.out.println(a >= b);
        System.out.println(a <= c);
    }
}"""
            if st.button("▶️ Run Comparison Operator"):
                output = run_java_code(code_compare)
                st.code(output)

        st.markdown("---")

        # ----------------------------- #
        st.markdown("### 🔀 Operator Logika (Logical Operator)")
        st.write("""
        Operator logika digunakan untuk menggabungkan dua atau lebih ekspresi boolean.

        | Operator | Nama | Arti |
        |-----------|------|------|
        | `&&` | AND | true jika **semua** kondisi true |
        | `\|\|` | OR | true jika **salah satu** kondisi true |
        | `!` | NOT | membalikkan nilai true/false |
        """)

        st.code(
            """
boolean benar = true;
boolean salah = false;

System.out.println(benar || salah); // true
System.out.println(benar && salah); // false
System.out.println(!benar);         // false
""",
            language="java",
        )

        with st.expander("🧩 Jalankan Contoh", expanded=True):
            code_logic = """public class Main {
    public static void main(String[] args) {
        boolean benar = true;
        boolean salah = false;

        System.out.println(benar || salah);
        System.out.println(benar && salah);
        System.out.println(!benar);
    }
}"""
            if st.button("▶️ Run Logical Operator"):
                output = run_java_code(code_logic)
                st.code(output)


def run():
    operator("Operator").run()
