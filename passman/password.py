import tkinter as tk
import sqlite3
from widget_generators import *
from database import DatabaseConnection
import helper_functions


class WindowNewPassword(tk.Toplevel):

    def __init__(self, parent):

        super().__init__(parent)

        self.title("New password")

        self.geometry(
            f"{320}x{400}")
        
        self.resizable(False, False)

        self.parent = parent

        self.geometry("+%d+%d" %(self.parent.winfo_x() // 4 + 320, self.parent.winfo_y() // 4 + 400))

        self.new_password_address = tk.StringVar()
        
        self.new_password_name = tk.StringVar()

        self.new_password = tk.StringVar()

        self.new_password.trace_add(mode="write", callback=self.__check_new_password)
        
        self.new_password_description = tk.StringVar()

        self.new_password_description.set("")

        self.grab_set()


        self.new_password_address_label = LabelGenerator(
            master=self,
            text="Enter your password's address:",
            font=("Times New Roman", 12),
            x=5,
            y=5
        )


        self.new_password_address = EntryGenerator(
            master=self,
            show="",
            textvariable=self.new_password_address,
            width=24,
            x=5,
            y=5 + 20
        )


        self.new_password_name_label = LabelGenerator(
            master=self,
            text="Enter your password's name:",
            font=("Times New Roman", 12),
            x=5,
            y=5 + 20 * 2
        )


        self.new_password_name = EntryGenerator(
            master=self,
            show="",
            textvariable=self.new_password_name,
            width=24,
            x=5,
            y=5 + 20 * 2 + 20
        )


        self.new_password_field_label = LabelGenerator(
            master=self, 
            text="Enter your password:",
            font=("Times New Roman", 12),
            x=5,
            y=5 + 20 * 2 + 20 * 2
        )


        self.new_password_field = EntryGenerator(
            master=self,
            textvariable=self.new_password,
            width=24,
            show="*",
            x=5,
            y=5 + 20 * 2 + 20 * 2 + 20
        )


        self.new_password_security_label = LabelGenerator(
            master=self,
            text="",
            font=("Times New Roman", 12),
            x=5, 
            y=5 + 20 * 2 + 20 * 2 + 20 + 25
        )


        self.new_password_description_label = LabelGenerator(
            master=self,
            text="Description:",
            font=("Times New Roman", 12),
            x=5, 
            y=5 + 20 * 2 + 20 * 2 + 20 + 25 + 25 + 10
        )


        self.new_password_description = TextGenerator(
            master=self,
            width=24,
            x=5,
            y=5 + 20 * 2 + 20 * 2 + 20 + 25 + 25 + 30
        )


        self.button_save_new_password = ButtonGenerator(
            master=self,
            text="Save",
            command=self.__save_new_password,
            state=tk.DISABLED,
            x=5,
            y=5 + 20 * 2 + 20 * 2 + 20 + 120,
            width=50,
            height=24
        )


        self.button_cancel_new_password = ButtonGenerator(
            master=self,
            text="Cancel",
            command=self.__cancel_new_password,
            x=5 + 55,
            y=5 + 20 * 2 + 20 * 2 + 20 + 120,
            width=50,
            height=24
        )


        self.button_show_new_password = ButtonGenerator(
            master=self,
            text="Show",
            command=lambda: helper_functions.toggle_password(self.new_password_field, self.button_show_new_password),
            x=5 + 24 * 9,
            y=5 + 20 * 2 + 20 * 2 + 20,
            width=50,
            height=24
        )


        self.mainloop()


    def __check_new_password(self, *args):

        password_validation = helper_functions.PasswordValidation()
        
        strong_password = password_validation.is_password_valid(self.new_password.get())

        if not strong_password:

            self.new_password_security_label.config(text="Password is weak!!!", foreground="red")

            self.button_save_new_password.config(state=tk.DISABLED)

        else:

            self.new_password_security_label.config(text="Password is good.", foreground="green")

            self.button_save_new_password.config(state=tk.ACTIVE)


    def __save_new_password(self):

        password_address_value = self.new_password_address.get()

        password_name_value = self.new_password_name.get()

        password_field_value = self.new_password.get()

        password_description_value = self.new_password_field.get()

        new_password_data = [(password_address_value, password_name_value, password_field_value, password_description_value)]

        connection = sqlite3.connect("passman.db")

        cursor = connection.cursor()

        cursor.executemany("INSERT INTO passman (password_address, password_name, password, password_description) VALUES (?,?,?,?)", new_password_data)

        connection.commit()

        connection.close()

        self.parent.password_list.insert(tk.END, password_name_value + " " + password_address_value)

        self.window_message = NotificationGenerator(
            title = "Notification",
            text="Password successfully added",
        )

        self.window_message.mainloop()
        
        self.destroy()


    def __cancel_new_password(self):

        self.grab_release()

        self.destroy()


class WindowDeletePassword():

    def __init__(self, parent):

        self.parent = parent

        self.window_delete_password = ConfirmationGenerator(
            "password deletion",
        )


        self.label_delete_password = LabelGenerator(
            master=self.window_delete_password,
            font=("Times New Roman", 12),
            text=f"Are you sure you want to delete password ''?", # add password description!
            x=380 / 2 - 370 / 2,
            y=10,
        )

        self.button_save_password = ButtonGenerator(
            master=self.window_delete_password,
            text="Yes!",
            command=self.confirm_password_deletion,
            x=5,
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

        self.parent.password_list.delete(0, tk.END)

        password_values_list = self.parent.password_list_value.split()
        
        connection = sqlite3.connect("passman.db")

        cursor = connection.cursor()
        
        cursor.execute(f"DELETE FROM passman WHERE password_name = '{password_values_list[0]}' AND password_address = '{password_values_list[1]}';")

        connection.commit()
        
        listbox_data = cursor.execute("SELECT password_name, password_address FROM passman;")

        for row in listbox_data:
        
            self.parent.password_list.insert(tk.END, f"{row[0]} {row[1]}")
        
        connection.close()

        self.notification_window = NotificationGenerator(text="Password successfully deleted!")

        self.window_delete_password.destroy()
    