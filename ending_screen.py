# end_screen.py
import tkinter as tk

# Palette (same as start/quiz UI)
BG_DARK   = "#1F2630"
FG_TEXT   = "#E2E2E2"
ACCENT    = "#F86153" 
GREY      = "#5E5757"
BORDER    = "#000000"
BLUE      = "#4D91EA"

CHECK = "✅"
CROSS = "❌"


class EndScreen:
    """
    End screen summary:
      - "Your score was X/15" (with 'score' highlighted)
      - 3 grey columns with black border containing Q1..Q15 + tick/cross
      - Grey thank-you strip
      - 'Restart Quiz' button with blue border at the bottom
    """
    def __init__(self, root, results, score, total, on_restart):
        self.root = root
        self.results = results              # list[tuple[str, bool]] -> (question_text, is_correct)
        self.score = score
        self.total = total
        self.on_restart = on_restart

        # ---------- MAIN ----------
        self.frame = tk.Frame(root, bg=BG_DARK)
        self.frame.pack(fill="both", expand=True)

        # ---------- HEADER: "Your score was X/15" ----------
        header = tk.Frame(self.frame, bg=BG_DARK)
        header.pack(pady=(20, 12))

        tk.Label(
            header, text="Your ", font=("Arial", 18), fg=FG_TEXT, bg=BG_DARK
        ).pack(side="left")

        tk.Label(
            header, text="score", font=("Arial", 18, "bold"), fg=ACCENT, bg=BG_DARK
        ).pack(side="left")

        tk.Label(
            header, text=f" was {self.score}/{self.total}", font=("Arial", 18), fg=FG_TEXT, bg=BG_DARK
        ).pack(side="left")

        # ---------- RESULTS GRID (3 columns x 5 rows) ----------
        # Prepare data as boolean list by question index
        # If results length < total (edge cases), pad with False
        flags = [is_correct for (_q, is_correct) in self.results]
        if len(flags) < self.total:
            flags += [False] * (self.total - len(flags))
        flags = flags[:self.total]

        grid = tk.Frame(self.frame, bg=BG_DARK)
        grid.pack(pady=(8, 16))

        # Helper to build one grey column with black border
        def make_column(parent):
            outer = tk.Frame(parent, bg=BORDER)
            outer.pack(side="left", padx=10)
            inner = tk.Frame(outer, bg=GREY)
            inner.pack(padx=2, pady=2)
            return inner

        col1 = make_column(grid)
        col2 = make_column(grid)
        col3 = make_column(grid)

        # Place Q1..Q15 across the three columns
        # Column 1: 1..5, Column 2: 6..10, Column 3: 11..15
        def add_rows(col_frame, start_q_idx, end_q_idx):
            for i in range(start_q_idx, end_q_idx + 1):
                # i is 1-based question number; flags index is i-1
                ok = flags[i - 1] if (0 <= i - 1 < len(flags)) else False
                symbol = CHECK if ok else CROSS
                fg_symbol = "#3EE46B" if ok else "#FF5C5C"  # nice green/red for icons

                row = tk.Frame(col_frame, bg=GREY)
                row.pack(anchor="w", padx=10, pady=6)

                tk.Label(
                    row, text=f"Q{i}", font=("Arial", 14, "bold"),
                    fg=FG_TEXT, bg=GREY, width=3, anchor="w"
                ).pack(side="left")

                tk.Label(
                    row, text=symbol, font=("Arial", 16, "bold"),
                    fg=fg_symbol, bg=GREY, width=2, anchor="w"
                ).pack(side="left")

        add_rows(col1, 1, 5)
        add_rows(col2, 6, 10)
        add_rows(col3, 11, 15)

        # ---------- THANK YOU STRIP ----------
        thanks_border = tk.Frame(self.frame, bg=BORDER)
        thanks_border.pack(pady=(8, 12))

        thanks = tk.Label(
            thanks_border,
            text="Thank you for taking the quiz!",
            font=("Arial", 14, "bold"),
            fg=FG_TEXT,
            bg=GREY,
            padx=18,
            pady=10
        )
        thanks.pack(padx=2, pady=2)

        # ---------- RESTART BUTTON (GREY with BLUE BORDER) ----------
        btn_border = tk.Frame(self.frame, bg=BLUE)
        btn_border.pack(pady=(0, 20))

        restart_btn = tk.Button(
            btn_border,
            text="Restart Quiz",
            font=("Arial", 14, "bold"),
            fg=FG_TEXT,
            bg=GREY,
            activebackground=GREY,
            activeforeground=FG_TEXT,
            relief="flat",
            bd=0,
            padx=24,
            pady=12,
            command=self._handle_restart
        )
        restart_btn.pack(padx=2, pady=2)

        # Optional hover effect (lighten grey slightly)
        def _hover_in(e):  restart_btn.configure(bg="#6A6464")
        def _hover_out(e): restart_btn.configure(bg=GREY)
        restart_btn.bind("<Enter>", _hover_in)
        restart_btn.bind("<Leave>", _hover_out)

    # ---------- Action ----------
    def _handle_restart(self):
        self.hide()
        if callable(self.on_restart):
            self.on_restart()

    # ---------- Control ----------
    def show(self):
        self.frame.pack(fill="both", expand=True)

    def hide(self):
        self.frame.pack_forget()