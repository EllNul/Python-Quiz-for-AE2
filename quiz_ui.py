import tkinter as tk # Importing the Tkinter module for the quiz UI
from start_screen import StartScreen # This is importing start_screen for the page that comes before the main quiz
from ending_screen import EndScreen # This is importing ending_screen for the page that come after the main quiz
from results import append_result # Function that saves name, score, etc. to a CSV

# The colour palette that matches the figma design.
BG_DARK   = "#1F2630"
WHITE     = "#E2E2E2"
ACCENT    = "#F86153"
GREY      = "#5E5757"
BORDER    = "#000000"
BLUE      = "#4D91EA"

class QuizUI:
    def __init__(self, root, engine, messages):
        self.root = root
        self.engine = engine
        self.messages = messages
        self.selected = tk.IntVar()
        # self.user_name = "Analyst" # if I would like add the feature where if no name is put it just puts "Analyst"

        # Window styling
        self.root.title("Databricks Quiz") # Title
        self.root.configure(bg=BG_DARK) # Backbround colour
        self.root.geometry("900x620") # Where the quiz pops up within your display
        self.root.minsize(800, 560) # Minimum size - users can't minimise its size by a cirtain amount otherwise visuals break

        # Start screen
        self.start_screen = StartScreen(root, on_start=self._on_start_clicked)

        # Quiz frame
        self.quiz_frame = tk.Frame(root, bg=BG_DARK)

        # Question row: "Q1:" in ACCENT + question text in white
        self.question_row = tk.Frame(self.quiz_frame, bg=BG_DARK)
        self.question_prefix = tk.Label(
            self.question_row, text="", font=("Arial", 14, "bold"),
            fg=ACCENT, bg=BG_DARK # This makes sure that the "Q1" part of the text comes up as the accent colour (orange/red)
        )
        self.question_text = tk.Label(
            self.question_row, text="", font=("Arial", 14),
            fg=WHITE, bg=BG_DARK, justify="left", wraplength=760 # Adds the rest of text in the white colour
        )

        # Options buttons that will be places on the left hand side
        self.options_frame = tk.Frame(self.quiz_frame, bg=BG_DARK)
        self.option_buttons = []

        # Submit/Next button, styled like your mock (grey with blue border)
        self.button_border = tk.Frame(self.quiz_frame, bg=BLUE)  # border holder
        self.submit_next_button = tk.Button(
            self.button_border,
            text="Click to submit answer",
            font=("Arial", 13, "bold"),
            fg=WHITE,
            bg=GREY,
            activebackground=GREY,
            activeforeground=WHITE,
            relief="flat",
            bd=0,
            padx=18, pady=10,
            command=self._on_submit_or_next
        )

        # Internal state: whether we’re waiting to submit or to go next
        self.awaiting_submit = True # If set to false then the user is moving to the next question

    # Start the quiz
    def _on_start_clicked(self, name: str):
        self.user_name = name # or "Analyst" # If we would like to add a default name if no name is inputted (however we will add Regex to solve this on start screen)
        self.start_screen.hide() # Hide the start screen now that we are on the main quiz screen

        # Starts displaying the quiz!

        # Pack quiz layout
        self.quiz_frame.pack(fill="both", expand=True)

        # Question row
        self.question_row.pack(padx=16, pady=(20, 14), fill="x")
        self.question_prefix.pack(side="left")
        self.question_text.pack(side="left")

        # Options list
        self.options_frame.pack(padx=16, pady=(0, 16), fill="both", expand=True)

        # Button with blue border
        self.button_border.pack(pady=(0, 10))
        self.submit_next_button.pack(padx=2, pady=2)  # blue frame gives the border

        self.show_question() # Load in the first question!

    # Render a question
    def show_question(self):
        q_index = self.engine.index + 1
        q = self.engine.current_question()

        # Set the colored prefix and question text
        self.question_prefix.config(text=f"Q{q_index}: ")
        self.question_text.config(text=q["question"].split(": ", 1)[-1] if q["question"].startswith("Q") else q["question"]) # Updating the question text

        # Clear old options/ radiobuttons
        for rb in self.option_buttons:
            rb.destroy()
        self.option_buttons.clear()
        self.selected.set(-1)

        # Build new Radiobuttons that match the figma colour scheme
        for i, opt in enumerate(q["options"]):
            rb = tk.Radiobutton(
                self.options_frame,
                text=opt,
                variable=self.selected,
                value=i,
                font=("Arial", 14),
                fg=WHITE,
                bg=BG_DARK,
                activebackground=BG_DARK,
                activeforeground=WHITE,
                selectcolor=BG_DARK,     # keeps indicator background matching the dark bg
                anchor="w",
                justify="left",
                wraplength=720
            )
            rb.pack(anchor="w", fill="x", pady=8)
            self.option_buttons.append(rb)

        # Reset button to "submit" state
        self.awaiting_submit = True
        self.submit_next_button.config(text="Click to submit answer", state="normal")

    # submit or next, whiching from one button to the other when a question in answered or submitted
    def _on_submit_or_next(self):
        if self.awaiting_submit:
            self._submit_answer()
        else:
            self._next_step()

    def _submit_answer(self):
        choice = self.selected.get()
        if choice == -1:
            self.messages.warn_no_selection() # If no answer is selected then it outputs the didn't choose anything warning message
            return

        q = self.engine.current_question()
        explanation = q.get(
            "explanation",
            "This answer aligns with Databricks & Medallion best practices." # This gives a failsafe, if no explainataion is given then it just gives this general reason so the code dosen't break
        )
        is_correct = self.engine.check_answer(choice) # This updates the score and results list

        # Explanations
        if hasattr(self.messages, "show_correct_with_explanation") and hasattr(self.messages, "show_incorrect_with_explanation"):
            if is_correct:
                self.messages.show_correct_with_explanation(explanation)
            else:
                self.messages.show_incorrect_with_explanation(explanation, self.engine.correct_answer_text())
        else:
            if is_correct:
                self.messages.show_correct()
            else:
                self.messages.show_incorrect()

       # This sections adds the explainations and changes the wording slightly depanding on if the user got the question correct or incorrect.

        # Switch to "Next question" mode
        self.awaiting_submit = False
        self.submit_next_button.config(text="Next question")

    def _next_step(self):
        # Move to next question or end
        if self.engine.next_question():
            self.show_question()

        else:
        # Save result to CSV (name, score, total, timestamp) right at the end of the quiz loop before we get to the end screen.
            append_result(self.user_name, self.engine.score, len(self.engine.questions))

        # End of quiz: go to EndScreen
            self.quiz_frame.pack_forget()
            self.end_screen = EndScreen(
                self.root,
                self.engine.results,            # list of (question_text, is_correct)
                self.engine.score,
                len(self.engine.questions),
                on_restart=self.restart_to_start
        )


    # Fully return to start screen
    def restart_to_start(self):
        self.engine.restart()
        if hasattr(self, "end_screen") and self.end_screen:
            self.end_screen.hide()
        self.start_screen.show()