import streamlit as st
from streamlit_ace import st_ace
from core.base_module import BaseModule
from utils.piston_api import run_java_code


class JavaPracticeModule(BaseModule):
    def run(self):
        self.show_title()
        st.header("Coming Soon! Sabar ya")
#         st.write("Test your understanding of basic Java syntax and output!")

#         exercises = [
#             {
#                 "title": "1️⃣ Print Text",
#                 "instruction": "Write a Java program that prints `Hello, Streamlit!`",
#                 "expected": "Hello, Streamlit!\n",
#                 "template": """public class Main {
#     public static void main(String[] args) {
#         // Write your code here
#     }
# }""",
#             },
#             {
#                 "title": "2️⃣ Print a Number",
#                 "instruction": "Write a Java program that prints the number `42`",
#                 "expected": "42\n",
#                 "template": """public class Main {
#     public static void main(String[] args) {
#         // Write your code here
#     }
# }""",
#             },
#             {
#                 "title": "3️⃣ Loop Practice",
#                 "instruction": "Write a Java program that prints numbers from 1 to 5 (each on a new line).",
#                 "expected": "1\n2\n3\n4\n5\n",
#                 "template": """public class Main {
#     public static void main(String[] args) {
#         // Write your code here
#     }
# }""",
#             },
#         ]

#         st.sidebar.markdown("---")
#         selected = st.sidebar.selectbox(
#             "Choose Exercise", [e["title"] for e in exercises]
#         )
#         exercise = next(e for e in exercises if e["title"] == selected)

#         st.subheader(exercise["title"])
#         st.write(exercise["instruction"])

#         # --- Use ACE editor instead of text_area ---
#         code = st_ace(
#             value=exercise["template"],
#             language="java",
#             theme="monokai",
#             keybinding="vscode",
#             min_lines=12,
#             max_lines=30,
#             font_size=15,
#             tab_size=4,
#             wrap=True,
#             auto_update=True,
#             key=f"ace_{selected}",
#         )

#         expected_output = exercise["expected"]

#         if "java_scores" not in st.session_state:
#             st.session_state.java_scores = {e["title"]: None for e in exercises}

#         if st.button("▶️ Run Java Code"):
#             output = run_java_code(code)
#             st.subheader("🖥️ Program Output:")
#             st.code(output)

#             if output == expected_output:
#                 st.session_state.java_scores[exercise["title"]] = True
#                 self.success_msg("✅ Correct output! Well done.")
#             else:
#                 st.session_state.java_scores[exercise["title"]] = False
#                 self.error_msg("❌ Output doesn’t match expected result.")
#                 st.info(f"Expected:\n{expected_output}")

#         correct = sum(1 for v in st.session_state.java_scores.values() if v)
#         total = len(exercises)
#         st.markdown("---")
#         self.show_progress(correct, total)

if __name__=='__main__':
    JavaPracticeModule("Tes Praktek IMA!").run()