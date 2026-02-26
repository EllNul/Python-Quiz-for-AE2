# start_screen.py
import tkinter as tk
from tkinter import messagebox      # NEW: for popups
import re                            # NEW: for name validation

#PALETTE KEY
BG_DARK   = "#1F2630"
WHITE     = "#E2E2E2"
ACCENT    = "#F86153"
GREY      = "#5E5757"
BORDER    = "#000000"
BLUE      = "#4D91EA"

# Compile once at module load (fast & clean):
# Letters and hyphens only, 3–15 chars, must start/end with a letter
NAME_REGEX = re.compile(r"^[A-Za-z](?:[A-Za-z\- ]{1,20})[A-Za-z]$")


class StartScreen:

    def __init__(self, root, on_start):
        self.root = root
        self.on_start = on_start  # callback(name: str)

        # MAIN BACKGROUND 
        self.frame = tk.Frame(root, bg=BG_DARK)
        self.frame.pack(fill="both", expand=True)

        # Center container
        self.center_frame = tk.Frame(self.frame, bg=BG_DARK)
        self.center_frame.place(relx=0.5, rely=0.5, anchor="center")

        # TITLE 
        title_frame = tk.Frame(self.center_frame, bg=BG_DARK)
        title_frame.pack(pady=(0, 20))

        tk.Label(title_frame, text="Welcome to the ",
                 font=("Arial", 20, "bold"),
                 fg=WHITE, bg=BG_DARK).pack(side="left")

        tk.Label(title_frame, text="Databricks",
                 font=("Arial", 20, "bold"),
                 fg=ACCENT, bg=BG_DARK).pack(side="left")

        tk.Label(title_frame, text=" Quiz",
                 font=("Arial", 20, "bold"),
                 fg=WHITE, bg=BG_DARK).pack(side="left")

        # SUBTITLE 
        tk.Label(self.center_frame, text="What’s your name?",
                 font=("Arial", 16, "bold"),
                 fg=WHITE, bg=BG_DARK).pack(pady=(10, 8))

        # NAME ENTRY
        self.name_entry = tk.Entry(
            self.center_frame, font=("Arial", 14), width=32,
            fg=WHITE, bg=GREY,
            relief="solid", bd=2,
            highlightbackground=BORDER,
            highlightcolor=BORDER,
            highlightthickness=2,
            insertbackground=WHITE
        )
        self.name_entry.insert(0, "Input name:")
        self.name_entry.pack(ipady=10, pady=(0, 22))

        def _clear_placeholder(e):
            if self.name_entry.get() == "Input name:":
                self.name_entry.delete(0, tk.END)
        self.name_entry.bind("&lt;FocusIn&gt;", _clear_placeholder)

        # DESCRIPTION
        desc_outer = tk.Frame(self.center_frame, bg=BORDER)
        desc_outer.pack(pady=(0, 22))
        desc_inner = tk.Frame(desc_outer, bg=GREY, bd=0)
        desc_inner.pack(padx=2, pady=2)
        self.description_label = tk.Label(
            desc_inner,
            text=(
                "Description: What the quiz is about\n"
                "This quiz covers Databricks concepts and the Medallion Architecture.\n"
                "It is designed for data analysts and Power BI practitioners."
            ),
            font=("Arial", 12),
            fg=WHITE,
            bg=GREY,
            justify="left",
            anchor="nw",
            padx=12, pady=12,
            wraplength=560
        )
        desc_inner.configure(width=584)
        self.description_label.pack(fill="both")

        # START BUTTON
        self.start_btn_border = tk.Frame(self.center_frame, bg=BLUE)
        self.start_btn_border.pack(pady=(0, 6))
        self.start_button = tk.Button(
            self.start_btn_border,
            text="Click to start quiz",
            font=("Arial", 14, "bold"),
            fg=WHITE,
            bg=GREY,
            activebackground=GREY,
            activeforeground=WHITE,
            relief="flat",
            bd=0,
            padx=24, pady=12,
            command=self._handle_start
        )
        self.start_button.pack(padx=2, pady=2)

        def _hover_in(e):  self.start_button.configure(bg="#6A6464")
        def _hover_out(e): self.start_button.configure(bg=GREY)
        self.start_button.bind("&lt;Enter&gt;", _hover_in)
        self.start_button.bind("&lt;Leave&gt;", _hover_out)

        # Pressing Enter starts the quiz
        self.name_entry.bind("&lt;Return&gt;", lambda e: self._handle_start())

    # HANDLER WITH VALIDATION
    def _handle_start(self):
        raw = (self.name_entry.get() or "").strip()

        # Treat placeholder as empty
        if raw == "" or raw == "Input name:":
            messagebox.showwarning(
                "Name required",
                "Please enter your name (3–25 letters, hyphens allowed)."
            )
            self.name_entry.focus_set()
            self.name_entry.select_range(0, tk.END)
            return

        # Validate with regex: letters + hyphens, 3–15 chars, must start/end with a letter
        if not NAME_REGEX.match(raw):
            messagebox.showwarning(
                "Invalid name",
                "Your name must be 3–15 characters, contain only letters and hyphens (-), "
                "and begin and end with a letter.\n\nExamples:\n• Elliot\n• Pacey-Carrier"
            )
            self.name_entry.focus_set()
            self.name_entry.select_range(0, tk.END)
            return

        # If valid, proceed
        name = raw
        self.hide()
        self.on_start(name)

    # CONTROL
    def show(self):
        self.frame.pack(fill="both", expand=True)

    def hide(self):
        self.frame.pack_forget()