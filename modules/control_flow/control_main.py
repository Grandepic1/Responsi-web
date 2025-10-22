import streamlit as st
from modules.control_flow import ifElse, switchCase


def run():
    st.title("🔁 Modul 2: Control Flow")
    st.write("""
    Modul ini membahas **struktur kendali (control flow)** di Java seperti `if-else` dan `switch-case`.
    Gunakan menu di bawah untuk memilih subbab pembahasan.
    """)

    # Sidebar or main radio selector
    subbab = st.sidebar.radio("Pilih subbab:", ["If Else", "Switch Case"])

    if subbab == "If Else":
        ifElse.run()
    elif subbab == "Switch Case":
        switchCase.run()

run()