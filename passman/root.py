import tkinter as tk
import sqlite3
from database import DatabaseConnection
from widget_generators import *
from password import WindowNewPassword, WindowDeletePassword
from helper_functions import toggle_password


class App(tk.Tk):

    def __init__(self):

        #running the app
        super().__init__()

        self.__initialize_main_window()

        self.__initialize_password_list_frame()

        self.__fill_listbox()

        self.password_value_index = 0

        self.__initialize_password_handling_frame()

        self.mainloop()

    def __initialize_main_window(self):

        self.title("Passman")

        self.geometry(f"600x400")

        self.minsize(600, 400)

        self.eval("tk::PlaceWindow . center")

    def __initialize_password_list_frame(self):

        self.frame_password_list = tk.Frame(
            master=self,
            bd=3,
        )

        self.frame_password_list.place(x=5, y=5, width=600 / 2 - 30, height=400 - 10)

        self.password_list = tk.Listbox(
            master=self.frame_password_list,
            selectmode=tk.SINGLE,
            font=( "Times New Roman",
                   12 ),
            bg="gray96",
            selectbackground="gray",
            activestyle="none",
            height=4,
            x=5,
            y=5,
        )

        self.password_filter_value = tk.StringVar()

        self.password_filter_value.trace_add(
            mode="write",
            callback=self.__filter_passwords
        )

        self.get_filter_focus = (self.register(self.__start_filtering))

        self.password_search = EntryGenerator(
            master=self.frame_password_list,
            width=40,
            foreground="gray",
            validate="focus",
            validatecommand=self.get_filter_focus,
            textvariable=self.password_filter_value,
            x=5,
            y=5
        )

        self.password_search.insert(0, "Search password...")

        self.password_list.place(
            x=5,
            y=35,
            width=600 / 2 - 30,
            height=400 - 40
        )  # add to the arguments list above

        self.password_list.bind("<<ListboxSelect>>", self.__get_password)

    def __fill_listbox(self):

        self.password_list.delete(0, tk.END)

        db = DatabaseConnection()

        listbox_data = db.fetch_data()

        for row in listbox_data:

            self.password_list.insert(tk.END, f"{row[0]} {row[1]}")

    def __start_filtering(self):

        self.password_search.delete(0, tk.END)

        self.password_search.configure(foreground="black")

        # write functionality to get passwords data from the list (the function below)

    def __filter_passwords(self, *args):

        filter_value = self.password_filter_value.get()

        print(self.password_list.get(0, tk.END))

    def __initialize_password_handling_frame(self):

        self.frame_password_handling = tk.Frame(master=self, )

        self.frame_password_handling.place(
            x=600 / 2 - 10,
            y=5,
            width=600 / 2 + 10,
            height=400 - 5 * 2
        )

        self.button_add_new_password = ButtonGenerator(
            master=self.frame_password_handling,
            text="Add new password",
            command=self.__create_new_password_window,
            x=5,
            y=5,
            width=200,
            height=24
        )

        self.password_field_label = LabelGenerator(
            master=self.frame_password_handling,
            text="Edit password:",
            x=5,
            y=24 + 20,
        )

        self.password_value = tk.StringVar()

        self.password_field = EntryGenerator(
            master=self.frame_password_handling,
            width=24,
            show="*",
            state=tk.DISABLED,
            textvariable=self.password_value,
            x=5,
            y=24 + 20 + 20
        )

        self.button_delete_password = ButtonGenerator(
            master=self.frame_password_handling,
            text="Delete",
            state="disabled",
            command=self.__delete_password,
            x=24 + 200,
            y=24 + 20 + 20,
            width=50,
            height=24
        )

        self.button_show_password = ButtonGenerator(
            master=self.frame_password_handling,
            text="Show",
            state="disabled",
            command=lambda:
            toggle_password(self.password_field,
                            self.button_show_password),
            x=5,
            y=24 + 20 + 20 + 40,
            width=50,
            height=24
        )

        self.button_update_password = ButtonGenerator(
            master=self.frame_password_handling,
            text="Edit",
            state="disabled",
            command=self.__update_password,
            x=5 + 50 + 20,
            y=24 + 20 + 20 + 40,
            width=50,
            height=24
        )

        self.password_description = tk.StringVar()

        self.password_description = TextGenerator(
            master=self.frame_password_handling,
            width=30,
            x=5,
            y=24 + 20 + 20 + 40 + 40
        )

        self.button_close_window = ButtonGenerator(
            master=self.frame_password_handling,
            text="Close",
            command=self.destroy,
            x=600 / 2 - 200,
            y=600 / 2,
            width=150,
            height=30
        )

    def __delete_password(self):

        return WindowDeletePassword(self)

    def __create_new_password_window(self):

        return WindowNewPassword(self)

    def __get_password(self, *args):

        self.password_list_value = self.password_list.get(
            self.password_list.curselection()
        )

        current_password = self.password_list_value.split()

        SQL_query_password_data = f"SELECT password, password_description FROM passman WHERE password_name = '{current_password[0]}' AND password_address = '{current_password[1]}';"

        db = DatabaseConnection()

        db.fetch_password_data(
            SQL_query_password_data,
            self.password_value,
            self.password_description
        )

        self.button_update_password.config(state="normal")

        self.button_show_password.config(state="normal")

        self.button_delete_password.config(state="normal")

    def __update_password(self):

        if self.password_field["state"] == "disabled":

            self.button_delete_password.config(state="disabled")

            self.password_field.config(state="normal")

            self.button_update_password.config(text="Update")

        else:

            password_list_value = self.password_list.get(
                self.password_list.curselection()
            ).split(" ")

            db_connection = sqlite3.connect("passman.db")

            cursor = db_connection.cursor()

            cursor.execute(
                f"UPDATE passman SET password = '{self.password_value.get()}' WHERE password_name = '{password_list_value[0]}' AND password_address = '{password_list_value[1]}';"
            )

            db_connection.commit()

            del db_connection

            self.password_field.config(state="disabled")

            self.button_delete_password.config(state="normal")

            self.button_update_password.config(text="Edit")


if __name__ == "__main__":

    App()
