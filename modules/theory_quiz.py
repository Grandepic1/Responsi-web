import streamlit as st
from core.base_module import BaseModule


class SummaryQuizModule(BaseModule):
    def run(self):
        st.header("Nanti soalnya ditambahin lagi")
        self.show_title()
        self.create_question(
            "1. String termasuk tipe data apa?",
            ["Tipe Data list", "Tipe Data prima", "Tipe Data objek"],
            3,
            "String adalah sebuah kelas di Java yang memiliki metode dan atribut.",
        ) 

        self.create_question(
            "2. Manakah deklarasi variabel yang benar dalam bahasa Java?",
            [
                "int = umur 20;",
                "int umur = 20;",
                "umur int = 20;",
                "integer umur = 20;",
            ],
            2,
            "Format deklarasi yang benar adalah tipe_data nama_variabel = nilai;",
        )

        self.create_question(
            "3. Tipe data manakah yang digunakan untuk menyimpan nilai desimal di Java?",
            ["int", "char", "double", "boolean"],
            3,
            "Tipe data float digunakan untuk angka pecahan, contoh: float pi = 3.14f;",
        )

        st.code("int a = 7 % 3; \nSystem.out.println(a);")
        self.create_question(
            "4. Apa Output dari kode diatas?",
            ["0", "1", "2", "3"],
            2,
            "7 dibagi 3 sisanya 1 → hasil dari 7 % 3 adalah 1.",
        )

        self.create_question(
            "5. Manakah dari berikut ini yang merupakan operator perbandingan?",
            ["+", "is", "=", "=="],
            4,
            "Operator == digunakan untuk membandingkan dua nilai.",
        )

        self.create_question(
            "6. Apa fungsi utama dari pernyataan if dalam Java?",
            [
                "Mengulang perintah",
                "Menyimpan nilai",
                "Mengecek kondisi logika",
                "Mengimpor library",
            ],
            3,
            "if digunakan untuk mengevaluasi kondisi dan menjalankan blok kode tertentu jika kondisi benar/true.",
        )
        
        st.code("""
if (5 > 3){
    System.out.println("Benar");
} else {
    System.out.println("Salah");
}""","java")
        self.create_question(
            "7. Apa hasil dari ekspresi di atas?",
            ["Benar", "Salah", "Tidak menampilkan apa-apa", "Error"],
            1,
            "Karena 5 lebih besar dari 3, maka kondisi true dan akan melakukan print `Benar`.",
        )

        st.code(
            """
int a = 10;
if (a == 5){
    System.out.println("Benar");
} else {
    System.out.println("Salah");
}""",
            "java",
        )
        self.create_question(
            "8. Apa hasil dari ekspresi di atas?",
            ["Benar", "Salah", "Tidak menampilkan apa-apa", "Error"],
            2,
            "Karena a bernilai 10, kondisi a == 5 salah.",
        )

        self.create_question(
            "9. Manakah yang benar tentang switch-case di Java?",
            [
                "Nilai case harus konstan",
                "Nilai case boleh tipe boolean",
                "Boleh ada dua case dengan nilai sama",
                "Tidak perlu break",
            ],
            1,
            "Nilai case harus konstan (konstanta literal atau final).",
        )

        st.code("""
char grade = 'B';
switch (grade) {
    case 'A':
        System.out.println("Excellent");
        break;
    case 'B':
        System.out.println("Good");
        break;
    default:
        System.out.println("Invalid");
}
""")
        self.create_question("10. Apa hasil dari kode diatas?", ["Excellent", "Invalid", "Error", "Good"], 4, "Karena case 'B' dan nilai var grade sama")





        
