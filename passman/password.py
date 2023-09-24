import tkinter as tk
import sqlite3
import style
from widget_generators import *
import helper_functions


class WindowNewPassword(tk.Toplevel):

    def __init__(self, parent):

        super().__init__(parent)

        self.title("New password")

        self.geometry(
            f"{style.x_window_password_new}x{style.y_window_password_new}")
        
        self.resizable(False, False)


        self.parent = parent

        self.new_password_address = tk.StringVar()
        
        self.new_password_name = tk.StringVar()

        self.new_password_field = tk.StringVar()


        self.new_password_address_label = LabelGenerator(
            master=self,
            text="Enter your password's address:",
            font=("Times New Roman", 12),
            x=style.x_margin,
            y=style.y_margin
        )


        self.new_password_address = EntryGenerator(
            master=self,
            show="",
            textvariable=self.new_password_address,
            width=style.width_password_field,
            x=style.x_margin,
            y=style.y_new_password_address
        )


        self.new_password_name_label = LabelGenerator(
            master=self,
            text="Enter your password's name:",
            font=("Times New Roman", 12),
            x=style.x_margin,
            y=style.y_label_new_password_name
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
            command=self.__save_new_password,
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
            command=lambda: helper_functions.toggle_password(self.new_password_field),
            x=style.x_button_show_new_password,
            y=style.y_new_password_field,
            width=style.width_button,
            height=style.height_button
        )


        self.mainloop()


    def __save_new_password(self):

        password_address_value = self.new_password_address.get()

        password_name_value = self.new_password_name.get()

        password_field_value = self.new_password_field.get()

        new_password_data = (password_address_value, password_name_value, password_field_value)

        connection = sqlite3.connect("passman.db")

        cursor = connection.cursor()

        cursor.executemany("INSERT INTO passman (password_address, password_name, password) VALUES (?,?,?)", new_password_data)

        connection.commit()

        connection.close()

        self.parent.password_list.insert(tk.END, password_name_value)


        with open("passman.txt", "at") as data:

            data.write(f"{password_name_value}:{password_field_value}")

        self.destroy()


        self.window_message = NotificationGenerator(
            title = "Notification",
            text="Password successfully added",
        )


        self.window_message.mainloop()


class WindowDeletePassword:

    def __init__(self, parent):

        self.parent = parent

        password_field_value = self.parent.password_value.get()

        password_value_index = self.parent.saved_passwords.index(password_field_value)


        self.window_delete_password = ConfirmationGenerator(
            "password deletion",
        )


        self.label_delete_password = LabelGenerator(
            master=self.window_delete_password,
            font=("Times New Roman", 12),
            text=f"Are you sure you want to delete password '{self.parent.saved_passwords_names[password_value_index]}'?",
            x=style.x_window_password_delete / 2 - style.width_label_password_delete / 2,
            y=10,
        )
        

        self.button_save_password = ButtonGenerator(
            master=self.window_delete_password,
            text="Yes!",
            command=self.confirm_password_deletion,
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

    def confirm_password_deletion(self):

        self.notification_window = NotificationGenerator(text="Password successfully deleted!")

        self.window_delete_password.destroy()
    