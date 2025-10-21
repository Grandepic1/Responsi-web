import streamlit as st
from core.base_module import BaseModule


class FloatDoubleModule(BaseModule):
    def run(self):
        self.show_title()
        st.write("""
        Floating-point numbers represent decimals in binary fractions.
        ...
        """)

        st.subheader("Mini Quiz")
        answer = st.radio("Which type has higher precision?", ["float", "double"])
        if st.button("Submit"):
            if answer == "double":
                self.success_msg("✅ Correct! Double uses 64-bit precision.")
            else:
                self.error_msg("❌ Nope. Float is 32-bit only!")
