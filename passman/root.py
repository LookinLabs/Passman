import tkinter as tk
import style
from database import *
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


    def __fill_listbox(self):

        self.password_list.delete(0, tk.END)
        
        db = DatabaseConnection()

        listbox_data = db.fetch_data()

        for row in listbox_data:
        
            self.password_list.insert(tk.END, f"{row[0]} {row[1]}")


    def __initialize_password_handling_frame(self):

        self.frame_password_handling = tk.ttk.Frame(
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
            state="disabled",
            command=self.__delete_password,
            x=style.x_button_delete_password,
            y=style.y_password_field,
            width=style.width_button,
            height=style.height_button
        )


        self.button_show_password = ButtonGenerator(
            master=self.frame_password_handling,
            text="Show",
            state="disabled",
            command=lambda: toggle_password(self.password_field, self.button_show_password),
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


        self.password_description = tk.StringVar()

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


    def __delete_password(self):

        return WindowDeletePassword(self)

    
    def __create_new_password_window(self):

        return WindowNewPassword(self)


    def __get_password(self, *args):

        self.password_list_value = self.password_list.get(self.password_list.curselection())

        current_password = self.password_list_value.split()

        SQL_query_password_data = f"SELECT password, password_description FROM passman WHERE password_name = '{current_password[0]}' AND password_address = '{current_password[1]}';"

        db = DatabaseConnection()

        db.fetch_password_data(SQL_query_password_data, self.password_value, self.password_description)

        self.button_update_password.config(state="normal")

        self.button_show_password.config(state="normal")

        self.button_delete_password.config(state="normal")


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

            del db_connection

            self.password_field.config(state="disabled")

            self.button_delete_password.config(state="normal")

            self.button_update_password.config(text="Edit")


if __name__ == "__main__":
    
    App()
