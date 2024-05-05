import tkinter as tk


class ButtonGenerator(tk.Button):

    def __init__(self, master, text, command, x, y, width, height, state="normal"):

        super().__init__(master)

        self.configure(
            text=text,
            state=state,
            font=( "Arial",
                   12 ),
            command=command  #WindowNewPassword
        )

        self.place(x=x, y=y, width=width, height=height)


class LabelGenerator(tk.Label):

    def __init__(self, master, x, y, text, font=( "Lora", 12 ), foreground="black"):

        super().__init__(master)

        self.configure(text=text, font=font, foreground=foreground)

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


class NotificationGenerator(tk.Toplevel):

    def __init__(self, text, title="Notification"):

        super().__init__()

        self.title(title)

        self.resizable(False, False)

        self.geometry(f"300x200+400+400")

        self.grab_set()

        self.message_label = LabelGenerator(
            master=self,
            text=text,
            x=320 / 2 - 300 / 2,
            y=10,
        )

        self.message_button = ButtonGenerator(
            master=self,
            text="Ok",
            command=self.destroy,
            x=320 / 2 - 50 / 2,
            y=100,
            width=50,
            height=24
        )

    def __del__(self):

        self.grab_release()


class ConfirmationGenerator(tk.Toplevel):

    def __init__(self, title):

        super().__init__()

        self.title(title)

        self.minsize(width=380, height=200)

        self.geometry(f"300x200+400+400")

        self.grab_set()

    def __del__(self):

        self.grab_release()
