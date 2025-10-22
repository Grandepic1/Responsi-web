import streamlit as st


class BaseModule:
    def __init__(self, title: str, description: str = ""):
        self.title = title
        self.description = description

        if "module_scores" not in st.session_state:
            st.session_state.module_scores = {}

        if "wrong_attempts" not in st.session_state:
            st.session_state.wrong_attempts = {}
    def create_question(self, question:str, choices:list, answer:int, explanation:str):
        
        key_feedback = f"feedback_{question}"
        q = st.radio(
            question,
            choices,
            index=None,
        )
        if key_feedback not in st.session_state:
            st.session_state[key_feedback] = None
        if st.button("Cek Jawaban", key=question, disabled=(q is None)):
            if q == choices[answer-1]:
                st.session_state[key_feedback] = f"✅ Betul! {explanation}"
            else:
                st.session_state[key_feedback] = "❌ Salah. Coba cek kembali!"
        feedback = st.session_state.get(key_feedback)

        if feedback:
            if feedback.startswith("✅"):
                self.success_msg(feedback)
            elif feedback.startswith("❌"):
                self.error_msg(feedback)

        st.markdown("---")

    def create_question_fill(self, question:str, answer:list, explanation:str):
        
        st.write(question)
        user_answer = st.text_input("Jawaban: ", key=question)
        if st.button(
            "Cek Jawaban", key=f"btn_{question}", disabled=(not user_answer.strip())):
            normalized = user_answer.strip().replace("“", '"').replace("”", '"')
            normalized_lower = normalized.lower()

            correct = any(
                normalized_lower == a.strip().lower().replace("“", '"').replace("”", '"')
                for a in answer
            )
            if correct:
                self.success_msg(f"✅ Betul! {explanation}")
            else:
                self.error_msg("❌ Salah. Coba cek kembali!")
        st.markdown("---")

    def clear_feedback(self):
        for key in list(st.session_state.keys()):
            if key.startswith("feedback_") or key.startswith("input_"):
                del st.session_state[key]

    def show_title(self):
        st.title(self.title)
        if self.description:
            st.write(self.description)
        st.markdown("---")

    def show_progress(self, current: int, total: int):
        st.subheader("🏁 Progress Summary")
        st.write(f"You’ve completed **{current} / {total}** correctly.")
        st.progress(current / total if total else 0)

    def update_score(self, module_name: str, correct: bool):
        st.session_state.module_scores[module_name] = correct

    def get_score(self, module_name: str) -> bool:
        return st.session_state.module_scores.get(module_name, False)

    def success_msg(self, msg="✅ Correct!"):
        st.success(msg)

    def error_msg(self, msg="❌ Try again!"):
        st.error(msg)

    # 🧩 --- NEW SECTION: Solution Reveal System ---
    def track_attempt(self, exercise_title: str, correct: bool):
        """Track user attempts per exercise."""
        if exercise_title not in st.session_state.wrong_attempts:
            st.session_state.wrong_attempts[exercise_title] = 0

        if not correct:
            st.session_state.wrong_attempts[exercise_title] += 1
        else:
            st.session_state.wrong_attempts[exercise_title] = 0  # reset if correct

    def can_show_solution(self, exercise_title: str) -> bool:
        """Show solution button after 3 wrong attempts."""
        return st.session_state.wrong_attempts.get(exercise_title, 0) >= 3

    def show_solution_button(self, exercise_title: str, solution_code: str):
        """Display the reveal solution button."""
        if self.can_show_solution(exercise_title):
            st.markdown("### 💡 Need help?")
            if st.button("Reveal Solution"):
                st.code(solution_code, language="java")
                st.info(
                    "✅ Review this solution, then try to retype and run it yourself!"
                )
