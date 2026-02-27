import tkinter as tk
from quiz_engine import QuizEngine
from quiz_ui import QuizUI
from messages import MessageService

root = tk.Tk()
engine = QuizEngine()
messages = MessageService()
ui = QuizUI(root, engine, messages)
root.mainloop()