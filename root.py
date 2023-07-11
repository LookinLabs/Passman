from tkinter import *


window = Tk()

window.title("Pass Keeper")


def add_password():

    global saved_password

    saved_password = password_field.get()

    window.destroy()


x_coordinate = 600

y_coordinate = 400

window.geometry(f"{x_coordinate}x{y_coordinate}")

window.resizable(False, False)


saved_password = ""


password_field_label = Label(master=window, text="Enter your password:")

password_field_label.configure(font=("Times New Roman", 12))

password_field_label.place(x=x_coordinate - 200, y=30)


password_field = Entry(master=window, width=20)

password_field.place(x=x_coordinate - 200, y=50)


button_add_password = Button(master=window, text="Add")

button_add_password.config(command=add_password)

button_add_password.place(x=x_coordinate - 150, y=70, width=50, height=30)


button_clear_field = Button(master=window, text="Clear")

button_clear_field.place(x=x_coordinate - 80, y=70, width=50, height=30)


close_button = Button(window, text="Close", font=("Lora", 13), command=window.destroy)

close_button_width = 170

close_button_height = 30

close_button_x = x_coordinate / 2 - close_button_width / 2

close_button.place(x=close_button_width, y=y_coordinate - 50, width=close_button_width, height=close_button_height)

window.mainloop()

if saved_password != "":

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

    message_button.mainloop()