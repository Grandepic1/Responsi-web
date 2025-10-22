import streamlit as st


def run():
    st.set_page_config(page_title="Responsi IMA - Home", layout="wide")

    # Header Section
    st.title("👋 Selamat Datang di Web Responsi IMA")
    st.subheader("Platform Interaktif Pembelajaran Dasar Pemrograman Java")

    st.write("""
    Halo 👋, selamat datang di aplikasi pembelajaran IMA ini.  
    Platform ini dirancang agar kamu bisa **belajar, mencoba, dan memahami konsep Java** secara langsung.
    """)

    st.markdown("---")


    # About Section
    st.info("""
    🏫 Info terkait Responsi IMA juga akan diposting di sini ya!
    """)



if __name__ == "__main__":
    run()
