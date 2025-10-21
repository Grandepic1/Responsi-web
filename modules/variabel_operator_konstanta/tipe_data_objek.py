import streamlit as st
from core.base_module import BaseModule

class tipeDataObjek(BaseModule):
    def run(self):
        self.show_title()
        st.header("Tipe Data Objek : String")
        st.write("""

String adalah sebuah kelas di Java yang digunakan untuk merepresentasikan teks. String dapat berupa kata, kalimat, atau bahkan paragraf.

Karakteristik String

- String adalah immutable, artinya bahwa nilai String tidak dapat diubah setelah dibuat.
- String dapat diwakili dengan menggunakan tanda kutip ("...").
                 
Mengapa String bukan termasuk tipe data primitif?   
Karena String ini sebenarnya
merupakan sebuah kelas yang memiliki atribut yang bisa menyimpan banyak karakter. Atribut tersebut
memiliki tipe data \"array\",
""")
        st.write("Yang kita liat dan Yang sebenarnya terjadi")
        st.code("\"Hallo\" -> ['H','a','l','l','o']")
        st.info("String adalah kelas yang membantu mengolah kumpulan karakter")


def run():
    tipeDataObjek("Tipe Data Objek").run()