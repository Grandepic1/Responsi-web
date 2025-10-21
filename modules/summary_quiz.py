import streamlit as st
from core.base_module import BaseModule


class SummaryQuizModule(BaseModule):
    def run(self):
        self.show_title()
        st.write("Coming soon!")
