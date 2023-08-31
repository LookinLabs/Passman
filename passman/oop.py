from tkinter import *
from style import *

saved_passwords_names = []

saved_passwords = []


class Main():

    window = Tk()

    def __init__(self):

        self.window = Tk()

        self.window.title("Pass keeper")
        
        self.window.geometry(f"{x}x{y}")

        self.window.resizable(False, False)


        self.window.frame_password_list = Frame(master=self.window, bd=frame_border, relief=GROOVE)

        self.window.frame_password_list.place(
            x=x_margin, y=y_margin, width=width_frame_password_list, height=height_frame)
        

        self.window.frame_password_add = Frame(master=self.window, bd=frame_border, relief=GROOVE)

        self.window.frame_password_add.place(
            x=x_frame_password_add, y=y_margin, width=width_frame_password_add, height=height_frame)
        

        self.window.password_list = Listbox(master=self.window.frame_password_list, listvariable=saved_passwords_names, selectmode=SINGLE)

        self.window.password_list.configure(bg="gray96", selectbackground="gray")

        self.window.password_list.configure(activestyle="none", height=4)

        self.window.password_list.place(
            x=x_margin, y=y_margin, width=width_password_list, height=height_password_list)
        
        self.window.password_list.bind("<<ListboxSelect>>", self.get_password)

        
        self.fill_data()


        self.window.button_add_new_password = Button(
            master=self.window.frame_password_add, text="Add new password")
        
        self.window.button_add_new_password.config(command=self.window.destroy) #WindowNewPassword

        self.window.button_add_new_password.place(x=x_margin, y=y_margin, width=200, height=height_button)

        
        self.window.password_field_label = Label(master=self.window.frame_password_add, text="Edit password:")
        
        self.window.password_field_label.configure(font=("Times New Roman", 12))

        self.window.password_field_label.place(x=x_margin, y=y_label_password_field)


        self.password_value = StringVar()


        self.window.password_field = Entry(
            master=self.window.frame_password_add, width=width_password_field, show="*", textvariable=self.password_value, state=DISABLED)
        
        self.window.password_field.place(x=x_margin, y=y_password_field)

        
        self.window.button_delete_password = Button(
        master=self.window.frame_password_add, text="Delete", command=self.delete_password)

        self.window.button_delete_password.place(x=x_button_delete_password, y=y_password_field, width=width_button, height=height_button)


        self.window.button_show_password = Button(
        self.window.frame_password_add, text="Show", command=self.window.destroy) #self.show_and_hide_password

        self.window.button_show_password.place(
        x=x_margin, y=y_button_show_password, width=width_button, height=height_button)


        self.window.button_update_password = Button(
        self.window.frame_password_add, text="Edit", state="disabled", command=self.update_password)

        self.window.button_update_password.place(
        x=x_button_update_password, y=y_button_show_password, width=width_button, height=height_button)


        self.window.close_self_button = Button(
            self.window.frame_password_add, text="Close", font=("Lora", 13), command=self.window.destroy)
        
        self.window.close_self_button.place(
            x=x_button_close, y=y_button_close, width=width_window_button_close, height=height_window_button_close)
        
        
        self.window.current_password_index = 0

        
        self.window.mainloop()


    def fill_data(self):
    
        with open("passman.txt") as data:

            row = data.readline()

            while row != "":

                password_parts = row.split(":")

                name = password_parts[0]

                value = password_parts[1]

                self.window.password_list.insert(END, name)

                saved_passwords_names.append(name)

                saved_passwords.append(value)

                row = data.readline()


    def get_password(self):

        password_name_value = self.window.password_list.get(self.password_list.curselection())

        password_value_index = saved_passwords_names.index(password_name_value)

        password_string_value = self.window.saved_passwords[password_value_index].rstrip("\n")

        self.window.password_value.set(password_string_value)

        self.window.button_update_password.config(state="normal")


    def delete_password(self):

        def confirm_delete_password():

            self.window.password_list.delete(password_value_index)

            saved_passwords_names.pop(password_value_index)

            saved_passwords.pop(password_value_index)

            old_file_lines = []

            with open("passman.txt", "r") as file:

                old_file_lines = file.readlines()

            with open("passman.txt", "w") as file:

                for index, line in enumerate(old_file_lines):

                    if index != password_value_index:

                        file.write(line)

            window_delete_password.destroy()

            self.window.password_value.set("")


        password_field_value = self.window.password_value.get()

        password_value_index = self.window.saved_passwords.index(password_field_value)


        window_delete_password = Tk()

        window_delete_password.title("Password deletion")

        window_delete_password.geometry(
            f"{x_window_password_delete}x{y_window_password_delete}")

        window_delete_password.resizable(False, False)


        label_delete_password = Label(
            master=window_delete_password, text=f"Are you sure you want to delete password '{saved_passwords_names[password_value_index]}'?", relief=GROOVE)

        label_delete_password.place(
            x=x_window_password_delete / 2 - width_label_password_delete / 2, y=10, width=width_label_password_delete, height=40)
        

        button_save_password = Button(master=window_delete_password, text="Yes!")

        button_save_password.config(command=confirm_delete_password)

        button_save_password.place(x=x_margin, y=95, width=50, height=25)


        button_cancel_save_password = Button(master=window_delete_password, text="Cancel")

        button_cancel_save_password.config(command=window_delete_password.destroy)

        button_cancel_save_password.place(x=70, y=95, width=50, height=25)


    def update_password(self):

        if self.window.password_field["state"] == "disabled":

            self.window.button_delete_password.config(state="disabled")

            self.window.password_field.config(state="normal")

            self.window.button_update_password.config(text="Update")

        else:

            password_name_value = self.window.password_list.get(self.password_list.curselection())

            password_value_index = saved_passwords_names.index(password_name_value)

            updated_password_value = self.window.password_field.get()

            new_password_full_string = f"{updated_password_value}\n"

            self.window.saved_passwords[password_value_index] = new_password_full_string
                    
            with open('passman.txt', 'w', encoding='utf-8') as file:

                for index in range(len(self.window.saved_passwords)):

                    line = f"{saved_passwords_names[index]}:{self.saved_passwords[index]}"

                    file.write(line)


            self.window.password_field.config(state="disabled")

            self.window.button_delete_password.config(state="normal")

            self.window.button_update_password.config(text="Edit")
        

class WindowNewPassword():

    def __init__(self):

        self.window_new_password = Toplevel()

        self.window_new_password.title("New password")

        self.window_new_password.geometry(
            f"{x_window_password_new}x{y_window_password_new}")

        self.window_new_password.resizable(False, False)


        new_password_name_label = Label(
            master=self.window_new_password, text="Enter your password's name(usually it's a domain address):")

        new_password_name_label.configure(font=("Times New Roman", 12))

        new_password_name_label.place(x=x_margin, y=y_margin)


        new_password_name = Entry(master=self.window_new_password, width=width_password_field)

        new_password_name.place(x=x_margin, y=y_new_password_name)


        new_password_field_label = Label(
            master=self.window_new_password, text="Enter your password:")

        new_password_field_label.configure(font=("Times New Roman", 12))

        new_password_field_label.place(x=x_margin, y=y_label_new_password)


        new_password_field = Entry(master=self.window_new_password, width=width_password_field, show="*")

        new_password_field.place(x=x_margin, y=y_new_password_field)


        new_password_description_label = Label(
        master=self.window_new_password, text="Description:")

        new_password_description_label.configure(font=("Times New Roman", 12))

        new_password_description_label.place(x=x_margin, y=y_new_password_description_label)


        new_password_description = Text(master=self.window_new_password, width=width_password_field, height=3)

        new_password_description.place(x=x_margin, y=y_new_password_description)


        button_save_new_password = Button(master=self.window_new_password, text="Save")

        button_save_new_password.config(command=self.save_new_password)

        button_save_new_password.place(
            x=x_margin, y=y_button_save_new_password, width=width_button, height=height_button)


        button_cancel_new_password = Button(
            master=self.window_new_password, text="Cancel", command=self.destroy)

        button_cancel_new_password.place(
            x=x_button_cancel_new_password, y=y_button_save_new_password, width=width_button, height=height_button)


        button_show_new_password = Button(
            self.window_new_password, text="Show", command=self.show_and_hide_new_password)

        button_show_new_password.place(
            x=x_button_show_new_password, y=y_new_password_field, width=width_button, height=height_button)


    # def show_and_hide_new_password():

    #     if new_password_field["show"] == "*":

    #         new_password_field["show"] = ""

    #     else:

    #         new_password_field["show"] = "*"


    def save_new_password(self):

        password_name_value = self.window_new_password.new_password_name.get()

        password_field_value = self.window_new_password.new_password_field.get()

        saved_passwords_names.append(password_name_value)

        self.window_new_password.password_list.insert(END, password_name_value)

        saved_passwords.append(password_field_value)


        with open("passman.txt", "at") as data:

            data.write(f"{password_name_value}:{password_field_value}\n")

        self.window_new_password.destroy()


        window_message = Tk()

        window_message.title("Notification")

        window_message.geometry(f"{x_window_message}x{y_window_message}")

        window_message.resizable(False, False)


        message_label = Label(
            master=window_message, text="Password successfully added!", relief=GROOVE)

        message_label.place(x=x_label_message, y=y_label_message, width=width_label_message, height=height_label_message)


        message_button = Button(master=window_message, text="Ok")

        message_button.config(command=window_message.destroy)

        message_button.place(x=x_button_message, y=y_button_message, width=width_button, height=height_button)


        window_message.mainloop()
