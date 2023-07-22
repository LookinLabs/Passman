from tkinter import *


window = Tk()

window.title("Pass Keeper")


def add_password():


    def save_new_password():

        password_list.insert(END, password_field.get())
        

        window_new_password.destroy()

    
        window_message = Tk()

        window_message.title("Notification")

        window_message_x = 320

        window_message_y = 200

        window_message.geometry(f"{window_message_x}x{window_message_y}")

        window_message.resizable(False, False)


        message_label = Label(master=window_message, text="Password successfully added!", relief=GROOVE)

        message_label_width = 300

        message_label.place(x=window_message_x /  2 - message_label_width / 2, y=10, width=message_label_width, height=40)


        message_button = Button(master=window_message, text="Ok")

        message_button.config(command=window_message.destroy)

        message_button_width = 100

        message_button.place(x=window_message_x /  2 - message_button_width / 2, y=20, width=message_button_width, height=60)

        window_message.mainloop()


    window_new_password = Tk()

    window_new_password.title("New password")

    window_new_password_x = 320

    window_new_password_y = 200

    window_new_password.geometry(f"{window_new_password_x}x{window_new_password_y}")

    window_new_password.resizable(False, False)


    password_field_label = Label(master=window_new_password, text="Enter your password:")

    password_field_label.configure(font=("Times New Roman", 12))

    password_field_label.place(x=5, y=5)


    password_field = Entry(master=window_new_password, width=20)

    password_field.place(x=5, y=25)


    button_save_password = Button(master=window_new_password, text="Save")

    button_save_password.config(command=save_new_password)

    button_save_password.place(x=5, y=45, width=50, height=25)


    button_clear_field = Button(master=window_new_password, text="Cancel", command=window_new_password.destroy)

    button_clear_field.place(x=60, y=45, width=50, height=25)



def get_password(*args):

    password_value = password_list.get(password_list.curselection())

    password.set(password_value)



x_coordinate = 600

y_coordinate = 400

window.geometry(f"{x_coordinate}x{y_coordinate}")

window.resizable(False, False)


frame_password_list = Frame(master=window, bd=3, relief=GROOVE)

frame_password_list.place(x=5, y=5, width=x_coordinate / 2 - 20, height=y_coordinate - 10)

frame_password_add = Frame(master=window, bd=3, relief=GROOVE)

frame_password_add.place(x=x_coordinate / 2, y=5, width=x_coordinate / 2, height=y_coordinate - 10)


saved_passwords = []


password_list = Listbox(master=frame_password_list, listvariable=saved_passwords, selectmode=SINGLE)

password_list.configure(bg="gray96", selectbackground="gray")

password_list.configure(activestyle="none", height=4)

for password in saved_passwords:

    password_list.insert(END, password)

password_list.select_set(0)

password_list.bind("<<ListboxSelect>>", get_password)

password_list.place(x=5, y=5, width = x_coordinate / 2 - 40, height=y_coordinate - 30)


button_add_password = Button(master=frame_password_add, text="Add new password")

button_add_password.config(command=add_password)

button_add_password.place(x=5, y=5, width=250, height=25)


password_field_label = Label(master=frame_password_add, text="Edit password:")

password_field_label.configure(font=("Times New Roman", 12))

password_field_label.place(x=5, y=40)


password = StringVar()

password_field = Entry(master=frame_password_add, width=20, textvariable=password)

password_field.place(x=5, y=60)



close_button = Button(frame_password_add, text="Close", font=("Lora", 13), command=window.destroy)

close_button_width = 150

close_button_height = 30

close_button_x = x_coordinate / 2 - 200

close_button.place(x=close_button_x, y=y_coordinate - 50, width=close_button_width, height=close_button_height)

window.mainloop()