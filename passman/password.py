import tkinter as tk
import style
from widget_generators import *


class WindowNewPassword(tk.Toplevel):

    def __init__(self, parent):

        super().__init__(parent)

        self.title("New password")

        self.geometry(
            f"{style.x_window_password_new}x{style.y_window_password_new}")

        self.resizable(False, False)


        self.parent = parent
        
        self.new_password_name = tk.StringVar()

        self.new_password_field = tk.StringVar()


        self.new_password_name_label = LabelGenerator(
            master=self,
            text="Enter your password's name(usually it's a domain address):",
            font=("Times New Roman", 12),
            x=style.x_margin,
            y=style.y_margin
        )


        self.new_password_name = EntryGenerator(
            master=self,
            show="",
            textvariable=self.new_password_name,
            width=style.width_password_field,
            x=style.x_margin,
            y=style.y_new_password_name
        )


        self.new_password_field_label = LabelGenerator(
            master=self, 
            text="Enter your password:",
            font=("Times New Roman", 12),
            x=style.x_margin,
            y=style.y_label_new_password
        )


        self.new_password_field = EntryGenerator(
            master=self,
            textvariable=self.new_password_field,
            width=style.width_password_field,
            show="*",
            x=style.x_margin,
            y=style.y_new_password_field
        )


        self.new_password_description_label = LabelGenerator(
            master=self,
            text="Description:",
            font=("Times New Roman", 12),
            x=style.x_margin, 
            y=style.y_new_password_description_label
        )


        self.new_password_description = TextGenerator(
            master=self,
            width=style.width_password_field,
            x=style.x_margin,
            y=style.y_new_password_description
        )


        self.button_save_new_password = ButtonGenerator(
            master=self,
            text="Save",
            command=self.save_new_password,
            x=style.x_margin,
            y=style.y_button_save_new_password,
            width=style.width_button,
            height=style.height_button
        )


        self.button_cancel_new_password = ButtonGenerator(
            master=self,
            text="Cancel",
            command=self.destroy,
            x=style.x_button_cancel_new_password,
            y=style.y_button_save_new_password,
            width=style.width_button,
            height=style.height_button
        )


        self.button_show_new_password = ButtonGenerator(
            master=self,
            text="Show",
            command=self.show_and_hide_new_password,
            x=style.x_button_show_new_password,
            y=style.y_new_password_field,
            width=style.width_button,
            height=style.height_button
        )


    # def show_and_hide_new_password():

    #     if new_password_field["show"] == "*":

    #         new_password_field["show"] = ""

    #     else:

    #         new_password_field["show"] = "*"

        self.mainloop()


    def save_new_password(self):

        password_name_value = self.new_password_name.get()

        password_field_value = self.new_password_field.get()

        self.parent.saved_passwords_names.append(password_name_value)

        self.parent.password_list.insert(tk.END, password_name_value)

        self.parent.saved_passwords.append(password_field_value)


        with open("passman.txt", "at") as data:

            data.write(f"{password_name_value}:{password_field_value}\n")

        self.destroy()


        self.window_message = NotificationGenerator(
            title = "Notification",
            # x=style.x_window_message,
            # y=style.y_window_message
        )


        self.message_label = LabelGenerator(
            master=self.window_message,
            text="Password successfully added!",
            x=style.x_label_message,
            y=style.y_label_message,
            width=style.width_label_message,
            height=style.height_label_message
        )


        self.message_button = ButtonGenerator(
            master=self.window_message,
            text="Ok",
            command=self.destroy,
            x=style.x_button_message,
            y=style.y_button_message,
            width=style.width_button, 
            height=style.height_button)


        self.window_message.mainloop()


class WindowDeletePassword:

    def __init__(self):

    
        password_field_value = self.password_value.get()

        password_value_index = self.saved_passwords.index(password_field_value)


        self.window_delete_password = ConfirmationGenerator(
            "password deletion",
            style.x_window_password_delete,
            style.y_window_password_delete,
        )


        self.label_delete_password = LabelGenerator(
            master=self.window_delete_password,
            text=f"Are you sure you want to delete password '{self.saved_passwords_names[password_value_index]}'?",
            x=style.x_window_password_delete / 2 - style.width_label_password_delete / 2,
            y=10,
            width=style.width_label_password_delete,
            height=40
        )
        

        self.button_save_password = ButtonGenerator(
            master=self.window_delete_password,
            text="Yes!",
            command=confirm_delete_password,
            x=style.x_margin,
            y=95, 
            width=50,
            height=25
        )


        self.button_cancel_save_password = ButtonGenerator(
            master=self.window_delete_password,
            text="Cancel",
            command=self.window_delete_password.destroy,
            x=70,
            y=95,
            width=50,
            height=25
        )