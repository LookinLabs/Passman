from tkinter import *


window = Tk()

window.title("Pass Keeper")


def add_password():

    def show_and_hide_new_password():

        if new_password_field["show"] == "*":

            new_password_field["show"] = ""

        else:

            new_password_field["show"] = "*"


    def save_new_password():

        saved_passwords_names.append(new_password_name.get())

        password_list.insert(END, new_password_name.get())

        saved_passwords.append(new_password_field.get())

        window_new_password.destroy()


        window_message = Tk()

        window_message.title("Notification")

        window_message_x = 320

        window_message_y = 200

        window_message.geometry(f"{window_message_x}x{window_message_y}")

        window_message.resizable(False, False)


        message_label = Label(
            master=window_message, text="Password successfully added!", relief=GROOVE)

        message_label_width = 300

        message_label.place(x=window_message_x / 2 - message_label_width / 2, y=10, width=message_label_width, height=40)


        message_button = Button(master=window_message, text="Ok")

        message_button.config(command=window_message.destroy)

        message_button_width = 70

        message_button.place(x=window_message_x / 2 - message_button_width / 2, y=100, width=message_button_width, height=45)


        window_message.mainloop()


    window_new_password = Tk()

    window_new_password.title("New password")

    window_new_password_x = 320

    window_new_password_y = 200

    window_new_password.geometry(
        f"{window_new_password_x}x{window_new_password_y}")

    window_new_password.resizable(False, False)


    new_password_name_label = Label(
        master=window_new_password, text="Enter your password's name(usually it's a domain address):")

    new_password_name_label.configure(font=("Times New Roman", 12))

    new_password_name_label.place(x=5, y=5)


    new_password_name = Entry(master=window_new_password, width=20)

    new_password_name.place(x=5, y=25)


    new_password_field_label = Label(
        master=window_new_password, text="Enter your password:")

    new_password_field_label.configure(font=("Times New Roman", 12))

    new_password_field_label.place(x=5, y=50)


    new_password_field = Entry(master=window_new_password, width=20, show="*")

    new_password_field.place(x=5, y=70)


    button_save_new_password = Button(master=window_new_password, text="Save")

    button_save_new_password.config(command=save_new_password)

    button_save_new_password.place(x=5, y=95, width=50, height=25)


    button_cancel_new_password = Button(
        master=window_new_password, text="Cancel", command=window_new_password.destroy)

    button_cancel_new_password.place(x=60, y=95, width=50, height=25)


    button_show_new_password = Button(
        window_new_password, text="Show", command=show_and_hide_new_password)

    button_show_new_password.place(
        x=window_new_password_x / 3 * 2, y=70, width=50, height=25)


def get_password(*args):

    global password_value_index

    password_name_value = password_list.get(password_list.curselection())

    password_value_index = saved_passwords_names.index(password_name_value)

    password_value.set(saved_passwords[password_value_index])


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

    window_delete_password_x = 380

    window_delete_password_y = 200

    window_delete_password.geometry(
        f"{window_delete_password_x}x{window_delete_password_y}")

    window_delete_password.resizable(False, False)


    label_delete_password = Label(
        master=window_delete_password, text=f"Are you sure you want to delete password '{saved_passwords_names[password_value_index]}'?", relief=GROOVE)

    label_delete_password_width = 370

    label_delete_password.place(
        x=window_delete_password_x / 2 - label_delete_password_width / 2, y=10, width=label_delete_password_width, height=40)
    

    button_save_password = Button(master=window_delete_password, text="Yes!")

    button_save_password.config(command=confirm_delete_password)

    button_save_password.place(x=5, y=95, width=50, height=25)


    button_cancel_save_password = Button(master=window_delete_password, text="Cancel")

    button_cancel_save_password.config(command=window_delete_password.destroy)

    button_cancel_save_password.place(x=70, y=95, width=50, height=25)


x_coordinate = 600

y_coordinate = 400

window.geometry(f"{x_coordinate}x{y_coordinate}")

window.resizable(False, False)


frame_password_list = Frame(master=window, bd=3, relief=GROOVE)

frame_password_list.place(
    x=5, y=5, width=x_coordinate / 2 - 20, height=y_coordinate - 10)


frame_password_add = Frame(master=window, bd=3, relief=GROOVE)

frame_password_add.place(
    x=x_coordinate / 2, y=5, width=x_coordinate / 2, height=y_coordinate - 10)


saved_passwords_names = []

saved_passwords = []


password_list = Listbox(master=frame_password_list, listvariable=saved_passwords_names, selectmode=SINGLE)

password_list.configure(bg="gray96", selectbackground="gray")

password_list.configure(activestyle="none", height=4)

for password_name in saved_passwords_names:

    password_list.insert(END, password_name)

password_list.bind("<<ListboxSelect>>", get_password)

password_list.place(
    x=5, y=5, width=x_coordinate / 2 - 40, height=y_coordinate - 30)


button_add_new_password = Button(
    master=frame_password_add, text="Add new password")

button_add_new_password.config(command=add_password)

button_add_new_password.place(x=5, y=5, width=250, height=25)


password_field_label = Label(master=frame_password_add, text="Edit password:")

password_field_label.configure(font=("Times New Roman", 12))

password_field_label.place(x=5, y=40)


password_value = StringVar()

password_field = Entry(
    master=frame_password_add, width=20, show="*", textvariable=password_value, state=DISABLED)

password_field.place(x=5, y=60)


button_delete_password = Button(master=frame_password_add, text="Delete")

button_delete_password.config(command=delete_password)

button_delete_password.place(x=200, y=60)


button_show_password = Button(
        frame_password_add, text="Show", command=show_and_hide_password)

button_show_password.place(
        x=5, y=100, width=50, height=25)


button_update_password = Button(
        frame_password_add, text="Edit", command=update_password)

button_update_password.place(
        x=100, y=100, width=60, height=25)


close_window_button = Button(
    frame_password_add, text="Close", font=("Lora", 13), command=window.destroy)

close_window_button_width = 150

close_window_button_height = 30

close_button_x = x_coordinate / 2 - 200

close_window_button.place(
    x=close_button_x, y=y_coordinate - 50, width=close_window_button_width, height=close_window_button_height)


current_password_index = 0


window.mainloop()
