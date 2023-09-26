import tkinter as tk
import sqlite3
import style
from widget_generators import *
from tkinter import ttk
from password import WindowNewPassword, WindowDeletePassword
from helper_functions import toggle_password

class App(tk.Tk):

    def __init__(self):

        #running the app
        super().__init__()


        self.__initialize_main_window()


        self.__initialize_password_list_frame()


        self.__fetch()


        self.__initialize_password_handling_frame()


        self.password_value_index = 0        


        self.mainloop()


    def __initialize_main_window(self):

        self.title("Passman")

        self.geometry(f"{style.x}x{style.y}")

        self.minsize(style.x, style.y)

        self.eval("tk::PlaceWindow . center")


    def __initialize_password_list_frame(self):

        self.frame_password_list = tk.Frame(
            master=self,
            bd=3,
        )
        
        self.frame_password_list.place(
            x=style.x_margin,
            y=style.y_margin,
            width=style.width_password_list,
            height=style.height_password_list
        )


        self.password_list = tk.Listbox(
            master=self.frame_password_list,
            selectmode=tk.SINGLE,
            font=("Times New Roman", 12),
            bg="gray96",
            selectbackground="gray",
            activestyle="none",
            height=4,
            x=style.x_margin,
            y=style.y_margin,
        )
        
        self.password_list.place(x=style.x_margin, y=style.y_margin, width=style.width_password_list, height=style.height_password_list)

        self.password_list.bind("<<ListboxSelect>>", self.__get_password)


    def __fetch(self):

        connection = sqlite3.connect("passman.db")

        cursor = connection.cursor()

        # cursor.execute("CREATE TABLE passman (id INTEGER PRIMARY KEY AUTOINCREMENT, password_address TEXT, password_name TEXT, password TEXT, password_description TEXT DEFAULT NULL, password_update DATETIME DEFAULT CURRENT_TIMESTAMP)") # How to add timestamp?

        # passwords = [
        #     ("hh.ee", "haha", "12345678"),
        #     ("asdfg.com", "asdfg", "123412")
        # ]

        # cursor.executemany("INSERT INTO passman (password_address, password_name, password) VALUES (?,?,?)", passwords)

        # connection.commit()

        # for row in cursor.execute("SELECT * FROM passman"):

        #     print(row)
        for row in cursor.execute("SELECT password_name, password_address FROM passman"):

            self.password_list.insert(tk.END, f"{row[0]} {row[1]}")


        connection.close()


    def __initialize_password_handling_frame(self):

        self.frame_password_handling = ttk.Frame(
            master=self,
        )

        self.frame_password_handling.place(
            x=style.x_frame_password_handling,
            y=style.y_margin,
            width=style.width_frame_password_handling,
            height=style.height_frame
        )


        self.button_add_new_password = ButtonGenerator(
            master=self.frame_password_handling,
            text="Add new password",
            command=self.__create_new_password_window,
            x=style.x_margin,
            y=style.y_margin,
            width=200,
            height=style.height_button
        )


        self.password_field_label = LabelGenerator(
            master=self.frame_password_handling,
            text="Edit password:",
            x=style.x_margin, 
            y=style.y_label_password_field,
        )


        self.password_value = tk.StringVar()

        self.password_field = EntryGenerator(
            master=self.frame_password_handling, 
            width=style.width_password_field, 
            show="*",
            state=tk.DISABLED,
            textvariable=self.password_value,
            x=style.x_margin,
            y=style.y_password_field
        )

        
        self.button_delete_password = ButtonGenerator(
            master=self.frame_password_handling,
            text="Delete",
            command=self.__create_delete_password_window,
            x=style.x_button_delete_password,
            y=style.y_password_field,
            width=style.width_button,
            height=style.height_button
        )


        self.button_show_password = ButtonGenerator(
            master=self.frame_password_handling,
            text="Show",
            command=lambda: toggle_password(self.password_field),
            x=style.x_margin,
            y=style.y_button_show_password,
            width=style.width_button,
            height=style.height_button
        )


        self.button_update_password = ButtonGenerator(
            master=self.frame_password_handling,
            text="Edit",
            state="disabled", 
            command=self.__update_password,
            x=style.x_button_update_password,
            y=style.y_button_show_password,
            width=style.width_button,
            height=style.height_button
        )


        self.password_description = TextGenerator(
            master=self.frame_password_handling,
            width=30,
            x=style.x_margin,
            y=style.y_password_description
        )


        self.button_close_window = ButtonGenerator(
            master=self.frame_password_handling,
            text="Close",
            command=self.destroy,
            x=style.x_button_close, 
            y=style.y_button_close, 
            width=style.width_window_button_close,
            height=style.height_window_button_close
        )


    def __create_delete_password_window(self):

        print(self.password_list.curselection())

        password_index = self.password_list.curselection()[0] + 1

        WindowDeletePassword(password_index)

    
    def __create_new_password_window(self):

        return WindowNewPassword(self)


    def __get_password(self, *args):

        password_list_value = self.password_list.get(self.password_list.curselection()).split(" ")

        db_connection = sqlite3.connect("passman.db")
        
        cursor = db_connection.cursor()
        
        data = cursor.execute(f"SELECT password FROM passman WHERE password_name = '{password_list_value[0]}' AND password_address = '{password_list_value[1]}';")

        self.password_value.set(data.fetchall()[0][0])

        db_connection.close()

        self.button_update_password.config(state="normal")


    def __update_password(self):

        if self.password_field["state"] == "disabled":

            self.button_delete_password.config(state="disabled")

            self.password_field.config(state="normal")

            self.button_update_password.config(text="Update")

        else:

            password_list_value = self.password_list.get(self.password_list.curselection()).split(" ")

            db_connection = sqlite3.connect("passman.db")
            
            cursor = db_connection.cursor()
            
            cursor.execute(f"UPDATE passman SET password = '{self.password_value.get()}' WHERE password_name = '{password_list_value[0]}' AND password_address = '{password_list_value[1]}';")

            db_connection.commit()

            db_connection.close()

            self.password_field.config(state="disabled")

            self.button_delete_password.config(state="normal")

            self.button_update_password.config(text="Edit")


App()
