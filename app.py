import streamlit as st
from modules.theory_quiz import SummaryQuizModule
from modules.java_practice import JavaPracticeModule

st.set_page_config(page_title="Responsi IMA", layout="wide")

st.sidebar.title("📚 Modul")
module = st.sidebar.radio(
    "Pilih modul:",
    [
        "1️⃣ Variabel, Operator, dan Konstanta",
        "2️⃣ Control Flow",
        "3️⃣ Tes Teori",
        "4️⃣ Tes Praktek",
    ],
)

if module == "1️⃣ Variabel, Operator, dan Konstanta":
    from modules.variabel_operator_konstanta import (
        intro,
        operator,
        tipe_data_primitif,
        tipe_data_objek
    )

    selected = st.sidebar.radio(
        "Pilih subbab:",
        [
            "Variabel dan Algoritma",
            "Tipe Data Primitif",
            "Tipe Data Objek",
            "Operator",
        ],
    )

    if selected == "Variabel dan Algoritma":
        intro.run()
    elif selected == "Tipe Data Primitif":
        tipe_data_primitif.run()
    elif selected == "Tipe Data Objek":
        tipe_data_objek.run()
    elif selected == "Operator":
        operator.run()

elif module == "2️⃣ Control Flow":
    from modules.control_flow import(
        switchCase,
        ifElse
    )
    selected = st.sidebar.radio(
        "Pilih subbab:",
        [
            "If Else",
            "Switch Case"
        ],
    )
    if selected == "If Else":
        ifElse.run()
    elif selected == "Switch Case":
        switchCase.run()

elif module == "3️⃣ Tes Teori":
    SummaryQuizModule("Tes Teori IMA").run()

elif module == "4️⃣ Tes Praktek":
    JavaPracticeModule("Tes Praktek IMA").run()


