from tkinter import messagebox

class MessageService:
    def warn_no_selection(self):
        messagebox.showwarning("Warning", "Pick an option.")

    def show_correct_with_explanation(self, explanation: str):
        messagebox.showinfo("Correct ✅", f"That’s right!\n\nWhy:\n{explanation}")

    def show_incorrect_with_explanation(self, explanation: str, correct_text: str):
        messagebox.showinfo(
            "Incorrect ❌",
            f"The correct answer is: {correct_text}\n\nWhy:\n{explanation}"
        )

    def show_final_score(self, score, total):
        messagebox.showinfo("Done", f"You scored {score} out of {total}.")