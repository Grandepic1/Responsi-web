import streamlit as st

st.set_page_config(page_title="Responsi IMA", layout="wide")

# --- Modul Utama ---

home = st.Page("main.py", title="Home", icon="🏠")

# Modul 1 - Variabel, Operator, dan Konstanta
modul1_page = st.Page(
    "modules/variabel_operator_konstanta/var_main.py",
    title="1️⃣ Variabel, Operator, dan Konstanta",
    icon="🧩",
)

# Modul 2 - Control Flow (berisi radio di dalamnya)
control_flow_page = st.Page(
    "modules/control_flow/control_main.py", title="2️⃣ Control Flow", icon="🔁"
)

method = st.Page("modules/method.py", title="3️⃣ Method", icon="🔧")

theory_page = st.Page("modules/theory_quiz.py", title="Tes Teori", icon="🧠")

practice_page = st.Page("modules/java_practice.py", title="Tes Praktek", icon="💻")

# --- Navigation setup ---
pg = st.navigation(
    {   "Home": [home],
        "Modul": [
            modul1_page,
            control_flow_page,
            method
        ],
        "Tes": [
            theory_page,
            practice_page,
        ],
    }
)

pg.run()
