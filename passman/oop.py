from tkinter import *
from style import *

saved_passwords_names = []

saved_passwords = []


class WindowGenerator:

    def __init__(self, title, x, y, resizable_x, resizable_y):

        self.window = Tk()

        self.window.title(title)
        
        self.window.geometry(f"{x}x{y}")

        self.window.resizable(resizable_x, resizable_y)


class FrameGenerator:

    def __init__(self, master, bd, x, y, width, height):

        self.frame = Frame(master=master, bd=bd, relief=GROOVE)

        self.frame.place(
            x=x, y=y, width=width, height=height)
        

class ListBoxGenerator:

    def __init__(self, master, listvariable, bg, selectbackground, activestyle, height_list, x, y, width, height):

        self.listbox = Listbox(master=master, listvariable=listvariable, selectmode=SINGLE)

        self.listbox.configure(bg=bg, selectbackground=selectbackground)

        self.listbox.configure(activestyle=activestyle, height=height_list)

        self.listbox.place(
            x=x, y=y, width=width, height=height)


class ButtonGenerator:

    def __init__(self, master, text, command, x, y, width, height, state="normal", font=("Lora", 13)):

        self.button = Button(
            master=master, text=text, state=state, font=font)
        
        self.button.config(command=command) #WindowNewPassword

        self.button.place(x=x, y=y, width=width, height=height)


class LabelGenerator:

    def __init__(self, master, text, font, x, y):

        self.label = Label(master=master, text=text)
        
        self.label.configure(font=font)

        self.label.place(x=x, y=y)


class EntryGenerator:

        def __init__(self, master, width, show, textvariable, x, y):

            self.entry = Entry(
                master=master,
                width=width,
                show=show,
                textvariable=textvariable,
                state=DISABLED,
            )

            self.entry.place(x=x, y=y)

        
class Main():

    def __init__(self):

        self.main_window = WindowGenerator("Pass keeper", x, y, False, False)


        self.frame_password_list = FrameGenerator(
            master=self.main_window.window, 
            bd=frame_border, 
            x=x_margin, 
            y=y_margin, 
            width=width_frame_password_list, 
            height=height_frame
        )


        self.frame_password_add = FrameGenerator(
            master=self.main_window.window, 
            bd=frame_border, 
            x=x_frame_password_add, 
            y=y_margin, 
            width=width_frame_password_add, 
            height=height_frame
        )
        

        self.password_list = ListBoxGenerator(
            master=self.frame_password_list.frame,
            listvariable=saved_passwords_names,
            bg="gray96",
            selectbackground="gray",
            activestyle="none",
            height_list=4,
            x=x_margin,
            y=y_margin,
            width=width_password_list,
            height=height_password_list
        )
        
        self.password_list.listbox.bind("<<ListboxSelect>>", self.get_password)

        
        self.fill_data()


        self.button_add_new_password = ButtonGenerator(
            master=self.frame_password_add.frame,
            text="Add new password",
            command=self.main_window.window.destroy, #WindowNewPassword
            x=x_margin,
            y=y_margin,
            width=200,
            height=height_button
        )

        
        self.password_field_label = LabelGenerator(
            master=self.frame_password_add.frame,
            text="Edit password:",
            font=("Times New Roman", 12),
            x=x_margin, y=y_label_password_field
        )


        self.password_value = StringVar()


        self.password_field = EntryGenerator(
            master=self.frame_password_add.frame, 
            width=width_password_field, 
            show="*", 
            textvariable=self.password_value,
            x=x_margin,
            y=y_password_field
        )

        
        self.button_delete_password = ButtonGenerator(
            master=self.frame_password_add.frame,
            text="Delete",
            command=self.delete_password,
            x=x_button_delete_password,
            y=y_password_field,
            width=width_button,
            height=height_button
        )


        self.button_show_password = ButtonGenerator(
            master=self.frame_password_add.frame,
            text="Show",
            command=self.main_window.window.destroy, #self.show_and_hide_password
            x=x_margin,
            y=y_button_show_password,
            width=width_button,
            height=height_button
        )


        self.button_update_password = ButtonGenerator(
            master=self.frame_password_add.frame,
            text="Edit",
            state="disabled", 
            command=self.update_password,
            x=x_button_update_password,
            y=y_button_show_password,
            width=width_button,
            height=height_button
        )


        self.button_close_window = ButtonGenerator(
            master=self.frame_password_add.frame,
            text="Close",
            command=self.main_window.window.destroy,
            x=x_button_close, 
            y=y_button_close, 
            width=width_window_button_close,
            height=height_window_button_close
        )
        
        
        self.current_password_index = 0

        
        self.main_window.window.mainloop()


    def fill_data(self):
    
        with open("passman.txt") as data:

            row = data.readline()

            while row != "":

                password_parts = row.split(":")

                name = password_parts[0]

                value = password_parts[1]

                self.password_list.listbox.insert(END, name)

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


        self.window_delete_password = WindowGenerator(
            "password deletion",
            x_window_password_delete,
            y_window_password_delete,
            False,
            False
        )


        self.label_delete_password = LabelGenerator(
            master=self.window_delete_password.window,
            text=f"Are you sure you want to delete password '{saved_passwords_names[password_value_index]}'?",
            x=x_window_password_delete / 2 - width_label_password_delete / 2,
            y=10,
            width=width_label_password_delete,
            height=40
        )
        

        self.button_save_password = ButtonGenerator(
            master=self.window_delete_password.window,
            text="Yes!",
            command=confirm_delete_password,
            x=x_margin,
            y=95, 
            width=50,
            height=25
        )


        self.button_cancel_save_password = ButtonGenerator(
            master=self.window_delete_password.window,
            text="Cancel",
            command=self.window_delete_password.window.destroy,
            x=70,
            y=95,
            width=50,
            height=25
        )


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
