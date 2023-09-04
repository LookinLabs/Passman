import tkinter as tk
import style
from widget_generators import *
from tkinter import ttk
from password import WindowNewPassword, WindowDeletePassword

class App(tk.Tk):

    def __init__(self, title, x, y):

        #running the app
        super().__init__()

        self.title(title)

        self.geometry(f"{x}x{y}")

        self.minsize(x, y)

        self.saved_passwords_names = []

        self.saved_passwords = []

        #widgets
        self.frame_password_list = ttk.Frame(
            master=self,
            relief=tk.GROOVE
        )
        
        self.frame_password_list.place(
            x=style.x_margin,
            y=style.y_margin,
            width=style.width_password_list,
            height=style.height_password_list
        )


        self.password_list = tk.Listbox(
            master=self.frame_password_list,
            listvariable=self.saved_passwords_names,
            selectmode=tk.SINGLE,
            bg="gray96",
            selectbackground="gray",
            activestyle="none",
            height=4,
            x=style.x_margin,
            y=style.y_margin,
            width=int(style.width_password_list),
        )

        
        self.password_list.place(x=style.x, y=style.y, width=style.width_password_list, height=style.height_password_list)

        self.password_list.bind("<<ListboxSelect>>", self.get_password)


        self.fill_data_arrays()


        self.frame_password_add = ttk.Frame(
            master=self,
            relief=tk.GROOVE
        )

        self.frame_password_add.place(
            x=style.x_frame_password_add,
            y=style.y_margin,
            width=style.width_frame_password_add,
            height=style.height_frame
        )


        self.button_add_new_password = ButtonGenerator(
            master=self.frame_password_add,
            text="Add new password",
            command=self.create_new_password_window, #WindowNewPassword
            x=style.x_margin,
            y=style.y_margin,
            width=200,
            height=style.height_button
        )


        self.password_field_label = LabelGenerator(
            master=self.frame_password_add,
            text="Edit password:",
            font=("Times New Roman", 12),
            x=style.x_margin, 
            y=style.y_label_password_field
        )


        self.password_value = tk.StringVar()

        self.password_field = EntryGenerator(
            master=self.frame_password_add, 
            width=style.width_password_field, 
            show="*", 
            textvariable=self.password_value,
            x=style.x_margin,
            y=style.y_password_field
        )

        
        self.button_delete_password = ButtonGenerator(
            master=self.frame_password_add,
            text="Delete",
            command=self.create_delete_password_window,
            x=style.x_button_delete_password,
            y=style.y_password_field,
            width=style.width_button,
            height=style.height_button
        )


        self.button_show_password = ButtonGenerator(
            master=self.frame_password_add,
            text="Show",
            command=self.destroy, #self.show_and_hide_password
            x=style.x_margin,
            y=style.y_button_show_password,
            width=style.width_button,
            height=style.height_button
        )


        self.button_update_password = ButtonGenerator(
            master=self.frame_password_add,
            text="Edit",
            state="disabled", 
            command=self.update_password,
            x=style.x_button_update_password,
            y=style.y_button_show_password,
            width=style.width_button,
            height=style.height_button
        )


        self.button_close_window = ButtonGenerator(
            master=self.frame_password_add,
            text="Close",
            command=self.destroy,
            x=style.x_button_close, 
            y=style.y_button_close, 
            width=style.width_window_button_close,
            height=style.height_window_button_close
        )


        self.password_value_index = 0        


        self.mainloop()


    def fill_data_arrays(self):
    
        with open("passman.txt") as data:

            row = data.readline()

            while row != "":

                password_parts = row.split(":")

                name = password_parts[0]

                value = password_parts[1]

                self.saved_passwords_names.append(name)

                self.password_list.insert(tk.END, name)

                self.saved_passwords.append(value)

                row = data.readline()


    def create_delete_password_window(self):

        return WindowDeletePassword()

    
    def create_new_password_window(self):

        return WindowNewPassword(self)


    def get_password(self):

        password_name_value = self.password_list.get(self.password_list.curselection())

        password_value_index = self.saved_passwords_names.index(password_name_value)

        password_string_value = self.saved_passwords[password_value_index].rstrip("\n")

        self.password_value.set(password_string_value)

        self.button_update_password.config(state="normal")


    def update_password(self):

        if self.password_field["state"] == "disabled":

            self.button_delete_password.config(state="disabled")

            self.password_field.config(state="normal")

            self.button_update_password.config(text="Update")

        else:

            password_name_value = self.password_list.get(self.password_list.curselection())

            password_value_index = self.saved_passwords_names.index(password_name_value)

            updated_password_value = self.password_field.get()

            new_password_full_string = f"{updated_password_value}\n"

            self.saved_passwords[password_value_index] = new_password_full_string
                    
            with open('passman.txt', 'w', encoding='utf-8') as file:

                for index in range(len(self.saved_passwords)):

                    line = f"{self.saved_passwords_names[index]}:{self.saved_passwords[index]}"

                    file.write(line)


            self.password_field.config(state="disabled")

            self.button_delete_password.config(state="normal")

            self.button_update_password.config(text="Edit")


    def delete_password(self):

        def confirm_delete_password():

            self.password_list.delete(self.password_value_index)

            self.saved_passwords_names.pop(self.password_value_index)

            self.saved_passwords.pop(self.password_value_index)

            old_file_lines = []

            with open("passman.txt", "r") as file:

                old_file_lines = file.readlines()

            with open("passman.txt", "w") as file:

                for index, line in enumerate(old_file_lines):

                    if index != self.password_value_index:

                        file.write(line)

            self.destroy() #window_delete_password

            self.password_value.set("")

        
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


App("Pass keeper", style.x, style.y)
