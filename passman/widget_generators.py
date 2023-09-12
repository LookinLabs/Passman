import style
import tkinter as tk
from tkinter import ttk


class ButtonGenerator(tk.Button):

    def __init__(self, master, text, command, x, y, width, height, state="normal"):

        super().__init__(master)

        self.configure(
            text=text,
            state=state,
            font=("Arial", 12),
            command=command #WindowNewPassword
        )

        self.place(x=x, y=y, width=width, height=height)


class LabelGenerator(tk.Label):

    def __init__(self, master, text, font, x, y):

        super().__init__(master)

        self.configure(text=text, font=font)

        self.place(x=x, y=y)


class EntryGenerator(tk.Entry):
        

    def __init__(self, master, width, show, textvariable, x, y, state="normal"):

        super().__init__(master)

        self.configure(
            width=width,
            show=show,
            textvariable=textvariable,
            state=state,
        )

        self.place(x=x, y=y)


class TextGenerator(tk.Text):

    def __init__(self, master, width, x, y, height=3):

        super().__init__(master)

        self.configure(width=width, height=height)

        self.place(x=x, y=y)


class ConfirmationGenerator(tk.Toplevel):

    def __init__(self, title):
        
        super().__init__()

        self.title(title)

        self.minsize(x=style.x_window_password_delete, y=style.y_window_password_delete)


class NotificationGenerator(tk.Toplevel):

    def __init__(self, title="notification"):

        super().__init__()

        self.title(title)