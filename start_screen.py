# start_screen.py
import tkinter as tk
from tkinter import messagebox      # NEW: for popups
import re                            # NEW: for name validation

# Compile once at module load (fast & clean):
# Letters and hyphens only, 3–15 chars, must start/end with a letter
NAME_REGEX = re.compile(r"^[A-Za-z](?:[A-Za-z\- ]{1,20})[A-Za-z]$")


class StartScreen:
    """
    Styled start screen using your palette:
      Orange/Red:  #F86153  (for the 'Databricks' word)
      Dark Blue:   #1F2630  (page background)
      Grey:        #5E5757  (input and button background)
      White:       #E2E2E2  (text)
      Black:       #000000  (input borders)
      Blue:        #4D91EA  (button border)
    """
    def __init__(self, root, on_start):
        self.root = root
        self.on_start = on_start  # callback(name: str)

        # ---------- MAIN BACKGROUND ----------
        self.frame = tk.Frame(root, bg="#1F2630")
        self.frame.pack(fill="both", expand=True)

        # Center container
        self.center_frame = tk.Frame(self.frame, bg="#1F2630")
        self.center_frame.place(relx=0.5, rely=0.5, anchor="center")

        # ---------- TITLE ----------
        title_frame = tk.Frame(self.center_frame, bg="#1F2630")
        title_frame.pack(pady=(0, 20))

        tk.Label(title_frame, text="Welcome to the ",
                 font=("Arial", 20, "bold"),
                 fg="#E2E2E2", bg="#1F2630").pack(side="left")

        tk.Label(title_frame, text="Databricks",
                 font=("Arial", 20, "bold"),
                 fg="#F86153", bg="#1F2630").pack(side="left")

        tk.Label(title_frame, text=" Quiz",
                 font=("Arial", 20, "bold"),
                 fg="#E2E2E2", bg="#1F2630").pack(side="left")

        # ---------- SUBTITLE ----------
        tk.Label(self.center_frame, text="What’s your name?",
                 font=("Arial", 16, "bold"),
                 fg="#E2E2E2", bg="#1F2630").pack(pady=(10, 8))

        # ---------- NAME ENTRY ----------
        self.name_entry = tk.Entry(
            self.center_frame, font=("Arial", 14), width=32,
            fg="#E2E2E2", bg="#5E5757",
            relief="solid", bd=2,
            highlightbackground="#000000",
            highlightcolor="#000000",
            highlightthickness=2,
            insertbackground="#E2E2E2"
        )
        self.name_entry.insert(0, "Input name:")
        self.name_entry.pack(ipady=10, pady=(0, 22))

        def _clear_placeholder(e):
            if self.name_entry.get() == "Input name:":
                self.name_entry.delete(0, tk.END)
        self.name_entry.bind("<FocusIn>", _clear_placeholder)

        # ---------- DESCRIPTION (as you already have) ----------
        desc_outer = tk.Frame(self.center_frame, bg="#000000")
        desc_outer.pack(pady=(0, 22))
        desc_inner = tk.Frame(desc_outer, bg="#5E5757", bd=0)
        desc_inner.pack(padx=2, pady=2)
        self.description_label = tk.Label(
            desc_inner,
            text=(
                "Description: What the quiz is about\n"
                "This quiz covers Databricks concepts and the Medallion Architecture.\n"
                "It is designed for data analysts and Power BI practitioners."
            ),
            font=("Arial", 12),
            fg="#E2E2E2",
            bg="#5E5757",
            justify="left",
            anchor="nw",
            padx=12, pady=12,
            wraplength=560
        )
        desc_inner.configure(width=584)
        self.description_label.pack(fill="both")

        # ---------- START BUTTON (grey with blue border frame) ----------
        self.start_btn_border = tk.Frame(self.center_frame, bg="#4D91EA")
        self.start_btn_border.pack(pady=(0, 6))
        self.start_button = tk.Button(
            self.start_btn_border,
            text="Click to start quiz",
            font=("Arial", 14, "bold"),
            fg="#E2E2E2",
            bg="#5E5757",
            activebackground="#5E5757",
            activeforeground="#E2E2E2",
            relief="flat",
            bd=0,
            padx=24, pady=12,
            command=self._handle_start
        )
        self.start_button.pack(padx=2, pady=2)

        def _hover_in(e):  self.start_button.configure(bg="#6A6464")
        def _hover_out(e): self.start_button.configure(bg="#5E5757")
        self.start_button.bind("<Enter>", _hover_in)
        self.start_button.bind("<Leave>", _hover_out)

        # Pressing Enter starts the quiz
        self.name_entry.bind("<Return>", lambda e: self._handle_start())

    # ---------- HANDLER WITH VALIDATION ----------
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

    # ---------- CONTROL ----------
    def show(self):
        self.frame.pack(fill="both", expand=True)

    def hide(self):
        self.frame.pack_forget()