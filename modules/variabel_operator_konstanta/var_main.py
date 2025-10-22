import streamlit as st
from modules.variabel_operator_konstanta import (
    intro,
    tipe_data_primitif,
    tipe_data_objek,
    operator,
)


def run():
    st.title("🧩 Modul 1: Variabel, Operator, dan Konstanta")

    subbab = st.sidebar.radio(
        "Pilih subbab:",
        ["Variabel dan Algoritma", "Tipe Data Primitif", "Tipe Data Objek", "Operator"],
    )

    if subbab == "Variabel dan Algoritma":
        intro.run()
    elif subbab == "Tipe Data Primitif":
        tipe_data_primitif.run()
    elif subbab == "Tipe Data Objek":
        tipe_data_objek.run()
    elif subbab == "Operator":
        operator.run()

if __name__ == "__main__":
    run()