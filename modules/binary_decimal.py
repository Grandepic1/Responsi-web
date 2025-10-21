import streamlit as st
from core.base_module import BaseModule


class BinaryDecimalModule(BaseModule):
    def run(self):
        self.show_title()
        st.subheader("Explanation")
        st.write("""
        Computers use binary (0 and 1) to represent data...
        Here's how to convert 13 to binary:
        13 = 8 + 4 + 1 = 1101₂
        """)

        with st.expander("Try it yourself!"):
            num = st.number_input("Enter a number:", min_value=0, step=1)
            st.write(f"Binary: {bin(num)[2:]}")
