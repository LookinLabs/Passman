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

button_clear_field = Button(master=window, text="Clear")


close_button = Button(window, text="Close", font=("Lora", 13), command=window.destroy)

close_button_width = 170

close_button_height = 30

close_button_x = x_coordinate / 2 - close_button_width / 2

close_button.place(x=close_button_width, y=y_coordinate - 50, width=close_button_width, height=close_button_height)

window.mainloop()