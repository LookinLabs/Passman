from tkinter import *
from style import *


window = Tk()

window.title("Pass Keeper")


def add_password():

    def show_and_hide_new_password():

        if new_password_field["show"] == "*":

            new_password_field["show"] = ""

        else:

            new_password_field["show"] = "*"


    def save_new_password():

        password_name_value = new_password_name.get()

        password_field_value = new_password_field.get()

        saved_passwords_names.append(password_name_value)

        password_list.insert(END, password_name_value)

        saved_passwords.append(password_field_value)


        with open("passman.txt", "at") as data:

            data.write(f"{password_name_value}:{password_field_value}\n")

        window_new_password.destroy()


        window_message = Tk()

        window_message.title("Notification")

        window_message.geometry(f"{x_window_message}x{y_window_message}")

        window_message.resizable(False, False)


        message_label = Label(
            master=window_message, text="Password successfully added!", relief=GROOVE)

        message_label.place(x=x_window_message / 2 - width_label_message / 2, y=10, width=width_label_message, height=40)


        message_button = Button(master=window_message, text="Ok")

        message_button.config(command=window_message.destroy)

        message_button_width = 70

        message_button.place(x=x_window_message / 2 - message_button_width / 2, y=100, width=message_button_width, height=45)


        window_message.mainloop()


    window_new_password = Tk()

    window_new_password.title("New password")

    window_new_password.geometry(
        f"{x_window_password_new}x{y_window_password_new}")

    window_new_password.resizable(False, False)


    new_password_name_label = Label(
        master=window_new_password, text="Enter your password's name(usually it's a domain address):")

    new_password_name_label.configure(font=("Times New Roman", 12))

    new_password_name_label.place(x=x_margin, y=y_margin)


    new_password_name = Entry(master=window_new_password, width=20)

    new_password_name.place(x=x_margin, y=y_margin + 20)


    new_password_field_label = Label(
        master=window_new_password, text="Enter your password:")

    new_password_field_label.configure(font=("Times New Roman", 12))

    new_password_field_label.place(x=x_margin, y=50)


    new_password_field = Entry(master=window_new_password, width=20, show="*")

    new_password_field.place(x=x_margin, y=70)


    button_save_new_password = Button(master=window_new_password, text="Save")

    button_save_new_password.config(command=save_new_password)

    button_save_new_password.place(x=x_margin, y=95, width=50, height=25)


    button_cancel_new_password = Button(
        master=window_new_password, text="Cancel", command=window_new_password.destroy)

    button_cancel_new_password.place(x=60, y=95, width=50, height=25)


    button_show_new_password = Button(
        window_new_password, text="Show", command=show_and_hide_new_password)

    button_show_new_password.place(
        x=x_window_password_new / 3 * 2, y=70, width=50, height=25)


def get_password(*args):

    global password_value_index

    password_name_value = password_list.get(password_list.curselection())

    password_value_index = saved_passwords_names.index(password_name_value)

    password_value.set(saved_passwords[password_value_index])

    button_update_password.config(state="normal")


def show_and_hide_password():

    if password_field["show"] == "*":

        password_field["show"] = ""

    else:

        password_field["show"] = "*"


def update_password():

    global current_password_index

    if password_field["state"] == "disabled":

        button_delete_password.config(state="disabled")

        password_field.config(state="normal")

        button_update_password.config(text="Update")

    else:

        updated_password_value = password_field.get()

        saved_passwords[current_password_index] = updated_password_value

        password_field.config(state="disabled")

        button_delete_password.config(state="normal")

        button_update_password.config(text="Edit")


def delete_password(*args):

    def confirm_delete_password():

        password_list.delete(password_value_index)

        saved_passwords_names.pop(password_value_index)

        saved_passwords.pop(password_value_index)

        window_delete_password.destroy()

        password_value.set("")


    password_field_value = password_value.get()

    password_value_index = saved_passwords.index(password_field_value)


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


window.geometry(f"{x}x{y}")

window.resizable(False, False)


frame_password_list = Frame(master=window, bd=frame_border, relief=GROOVE)

frame_password_list.place(
    x=x_margin, y=y_margin, width=width_frame_password_list, height=height_frame)


frame_password_add = Frame(master=window, bd=frame_border, relief=GROOVE)

frame_password_add.place(
    x=x_frame_password_add, y=y_margin, width=width_frame_password_add, height=height_frame)


saved_passwords_names = []

saved_passwords = []


password_list = Listbox(master=frame_password_list, listvariable=saved_passwords_names, selectmode=SINGLE)

password_list.configure(bg="gray96", selectbackground="gray")

password_list.configure(activestyle="none", height=4)

with open("passman.txt") as data:

    row = data.readline()

    while row != "":

        password_parts = row.split(":")

        name = password_parts[0]

        value = password_parts[1]

        password_list.insert(END, name)

        saved_passwords_names.append(name)

        saved_passwords.append(value)

        row = data.readline()

password_list.bind("<<ListboxSelect>>", get_password)

password_list.place(
    x=x_margin, y=y_margin, width=width_password_list, height=height_password_list)


button_add_new_password = Button(
    master=frame_password_add, text="Add new password")

button_add_new_password.config(command=add_password)

button_add_new_password.place(x=x_margin, y=y_margin, width=200, height=height_button)


password_field_label = Label(master=frame_password_add, text="Edit password:")

password_field_label.configure(font=("Times New Roman", 12))

password_field_label.place(x=x_margin, y=y_label_password_field)


password_value = StringVar()

password_field = Entry(
    master=frame_password_add, width=width_password_field, show="*", textvariable=password_value, state=DISABLED)

password_field.place(x=x_margin, y=y_password_field)


button_delete_password = Button(
        master=frame_password_add, text="Delete", command=delete_password)

button_delete_password.place(x=x_button_delete_password, y=y_password_field, width=width_button, height=height_button)


button_show_password = Button(
        frame_password_add, text="Show", command=show_and_hide_password)

button_show_password.place(
        x=x_margin, y=y_button_show_password, width=width_button, height=height_button)


button_update_password = Button(
        frame_password_add, text="Edit", state="disabled", command=update_password)

button_update_password.place(
        x=x_button_update_password, y=y_button_show_password, width=width_button, height=height_button)


close_window_button = Button(
    frame_password_add, text="Close", font=("Lora", 13), command=window.destroy)

close_window_button.place(
    x=x_button_close, y=y_button_close, width=width_window_button_close, height=height_window_button_close)


current_password_index = 0


window.mainloop()
