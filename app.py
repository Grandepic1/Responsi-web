import streamlit as st
from modules.float_double import FloatDoubleModule
from modules.summary_quiz import SummaryQuizModule
from modules.java_practice import JavaPracticeModule
from modules.variabel_operator_konstanta import tipe_data

st.set_page_config(page_title="Responsi IMA", layout="wide")

st.sidebar.title("📚 Modules")
module = st.sidebar.radio(
    "Choose a module:",
    [
        "1️⃣ Variabel, Operator, dan Konstanta",
        "2️⃣ Float vs Double",
        "3️⃣ Summary Quiz",
        "4️⃣ Java Output Practice",
    ],
)

if module == "1️⃣ Variabel, Operator, dan Konstanta":
    from modules.variabel_operator_konstanta import (
        intro,
        tipe_data,
        operator,
        summary,
    )

    selected = st.sidebar.radio(
        "Pilih subbab:",
        [
            "Variabel dan Algoritma",
            "Tipe Data Prima dan Objek",
            "3.3.2 Operator",
            "3.3.3 Konstanta",
            "Ringkasan",
        ],
    )

    if selected == "Variabel dan Algoritma":
        intro.run()
    elif selected == "Tipe Data Prima dan Objek":
        tipe_data.run()
    elif selected == "3.3.2 Operator":
        operator.run()
    elif selected == "Ringkasan":
        summary.run()

elif module == "2️⃣ Float vs Double":
    FloatDoubleModule("Float vs Double Precision").run()

elif module == "3️⃣ Summary Quiz":
    SummaryQuizModule("Summary Quiz").run()

elif module == "4️⃣ Java Output Practice":
    JavaPracticeModule("Java Output Practice").run()
