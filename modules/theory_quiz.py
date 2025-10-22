import streamlit as st
from core.base_module import BaseModule


class SummaryQuizModule(BaseModule):
    def run(self):
        self.clear_feedback()
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

        st.code(
            """
if (5 > 3){
    System.out.println("Benar");
} else {
    System.out.println("Salah");
}""",
            "java",
        )
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
        self.create_question(
            "10. Apa hasil dari kode diatas?",
            ["Excellent", "Invalid", "Error", "Good"],
            4,
            "Karena case 'B' dan nilai var grade sama",
        )

        self.create_question(
            "11. Apa yang terjadi jika kita tidak menggunakan `break` di dalam switch-case?",
            [
                "Program melanjutkan ke case berikutnya",
                "Program berhenti langsung",
                "Error kompilasi",
                "Program tidak berjalan sama sekali",
            ],
            1,
            "Tanpa `break`, eksekusi akan fall through (lanjut) ke case berikutnya",
        )

        self.create_question(
            "12. Tipe data manakah yang hanya dapat menyimpan satu karakter?",
            ["char", "String", "int", "boolean"],
            1,
            "Tipe data char menyimpan satu karakter tunggal, ditulis dengan tanda kutip tunggal ('A').",
        )

        st.code(
            """
int hasil = 5 * 4;
System.out.println(hasil);
""",
            "java",
        )

        self.create_question(
            "13. Apa output dari kode diatas?",
            [
                "10",
                "15",
                "20",
                "Error",
            ],
            3,
            "Karena 5 * 4 = 20.",
        )

        st.code('____ nama = "Revaldo";')
        self.create_question_fill("14. Lengkapi kode di atas dengan tipe data yang sesuai", ["String"],"String menyimpan teks")

        st.code(
            """
int x = 10;
x += 5;
System.out.println(x);
"""
        )
        self.create_question(
            "15. Berapa output dari kode di atas?",
            ["5", "10", "15", "20"],
            3,
            "Operator += menambahkan nilai ke variabel, jadi x menjadi 15.",
        )

        st.code(
            """
int a = 10;
if (a % 2 == 0) {
    System.out.println("Genap");
} else {
    System.out.println("Ganjil");
}
"""
        )
        self.create_question(
            "16. Output yang akan dihasilkan dari kode di atas adalah:",
            ["Genap", "Ganjil", "Error", "10"],
            1,
            "Karena 10 habis dibagi 2, maka Genap.",
        )

        st.code(
            """
int nilai = 80;
if (nilai >= 90) {
    System.out.println("A");
} else if (nilai >= 75) {
    System.out.println("B");
} else {
    System.out.println("C");
}
"""
        )
        self.create_question(
            "17. Apa output program di atas?",
            ["A", "B", "C", "Tidak menampilkan apapun"],
            2,
            "Nilai 80 memenuhi kondisi >= 75, maka output-nya adalah B.",
        )

        st.code(
            """
switch (3) {
    case 1:
        System.out.println("Satu");
        break;
    case 2:
        System.out.println("Dua");
        break;
    default:
        System.out.println("Lainnya");
}
"""
        )
        self.create_question(
            "18. Apa hasil dari switch-case di atas?",
            ["Satu", "Dua", "Lainnya", "Error"],
            3,
            "Tidak ada case dengan nilai 3, maka blok default dijalankan.",
        )

        st.code(
            """
public static void sapa() {
    System.out.println("Halo dunia!");
}

public static void main(String[] args) {
    sapa();
}
"""
        )
        self.create_question(
            "19. Apa output dari program di atas?",
            [
                "Halo dunia!",
                "Error",
                "Tidak menampilkan apa-apa",
                "Main method tidak dipanggil",
            ],
            1,
            "Karena method sapa() dipanggil di main, output-nya adalah 'Halo dunia!'.",
        )

        st.code(
            """
public static int tambah(int a, int b) {
    return a + b;
}

public static void main(String[] args) {
    System.out.println(tambah(3, 2));
}
"""
        )
        self.create_question(
            "20. Apa output dari kode di atas?",
            ["3", "5", "2", "Error"],
            2,
            "Karena 3 + 2 = 5.",
        )

        # Fill in code example (longer)
        st.code(
            """
if (nilai >= 70) {
    System.out.println("Lulus");
} ___ {
    System.out.println("Tidak Lulus");
}
"""
        )
        self.create_question_fill(
            "21. Lengkapi bagian yang kosong agar buisa menampilkan 'Tidak Lulus'",["else"],"Else digunakan jika tidak ada kondisi yang terpenuhi"
        )

        st.code(
            """
switch (hari) {
    case "Senin":
        System.out.println("Awal Minggu");
        break;
    ____:
        System.out.println("Akhir Minggu");
        break;
}
"""
        )
        self.create_question_fill(
            "22. Lengkapi bagian kosong agar mencetak 'Akhir Minggu' saat hari = Minggu:", ["case \"Minggu\""], "Membuat case baru untuk hari minggu"
        )

        st.code(
            """
public static int kuadrat(int x) {
    return ____;
}
"""
        )
        self.create_question_fill(
            "23. Lengkapi bagian kosong agar method mengembalikan hasil kuadrat dari nilai x (tidak pakai Math):", ["x*x", "x * x"], ""
        )

        self.create_question(
            "24. Manakah dari berikut ini yang benar mengenai method dengan parameter?",
            [
                "Tidak bisa mengembalikan nilai",
                "Hanya bisa menerima 1 parameter",
                "Dapat menerima lebih dari satu parameter",
                "Harus bernilai void",
            ],
            3,
            "Method dapat memiliki lebih dari satu parameter yang dipisahkan dengan koma.",
        )

        self.create_question(
            "25. Keyword apa yang digunakan untuk mendefinisikan method yang tidak mengembalikan nilai?",
            ["void", "return", "static", "break"],
            1,
            "Keyword void berarti method tidak mengembalikan nilai apapun.",
        )

        self.create_question(
            "26. Nilai default dari variabel bertipe boolean adalah?",
            ["true", "false", "null", "0"],
            2,
            "Nilai default variabel boolean adalah false.",
        )

        st.code(
            """
int a = 8;
int b = 3;
System.out.println(a / b);
"""
        )
        self.create_question(
            "27. Apa output dari kode di atas?",
            ["2.6", "2", "3", "Error"],
            2,
            "Karena a dan b adalah integer, maka hasilnya adalah pembagian bilangan bulat: 2.",
        )

        st.code(
            """
System.out.println(10 + 20 + "Java");
"""
        )
        self.create_question(
            "28. Apa hasil dari kode di atas?",
            ["Java1020", "30Java", "1020Java", "Error"],
            2,
            "Operator + dievaluasi dari kiri ke kanan, 10+20=30 kemudian digabung dengan 'Java'.",
        )

        st.code(
            """
int a = 5;
int b = 10;
int c = (a > b) ? a : b;
System.out.println(c);
"""
        )
        self.create_question(
            "29. Apa hasil dari kode di atas?",
            ["5", "10", "true", "false"],
            2,
            "Operator ternary memilih nilai setelah ':' karena kondisi (a>b) salah.",
        )

        self.create_question(
            "30. Apa fungsi utama dari keyword 'return' dalam method?",
            [
                "Menutup program",
                "Mengembalikan nilai ke pemanggil method",
                "Menampilkan teks ke layar",
                "Menghentikan loop",
            ],
            2,
            "Keyword return mengembalikan nilai ke pemanggil method di Java.",
        )


if __name__ == '__main__':
    SummaryQuizModule("Tes Teori IMA").run()