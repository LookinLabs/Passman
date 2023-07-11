from tkinter import *


window = Tk()

window.title("Pass Keeper")

x_coordinate = 500

y_coordinate = 400

window.geometry(f"{x_coordinate}x{y_coordinate}")

close_button = Button(window, text="Close", font=("Lora", 13), command=window.destroy)

close_button_width = 170

close_button_height = 30

close_button_x = x_coordinate / 2 - close_button_width / 2

close_button.place(x=close_button_width, y=y_coordinate - 50, width=close_button_width, height=close_button_height)

window.mainloop()