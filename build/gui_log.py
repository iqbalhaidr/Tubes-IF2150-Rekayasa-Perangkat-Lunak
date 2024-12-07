
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer

from tkinter import Toplevel, messagebox
from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\IMPLEMENTASI RPL\Tkinter-Designer-master\Tkinter-Designer-master\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("758x539")
window.configure(bg = "#2F0160")


canvas = Canvas(
    window,
    bg = "#2F0160",
    height = 539,
    width = 758,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)


def make_element(list_of_item : tuple):
    image_image_2 = PhotoImage(
                    file=relative_to_assets("image_2.png"))
    
    button_image_report = PhotoImage(
        file=relative_to_assets("button_1.png"))
    
    button_image_see_report = PhotoImage(
        file=relative_to_assets("button_2.png"))
    
    
    for i in range (len(list_of_item)):
        canvas.create_image(
            378.48193359375,
            218.81390380859375 + i*121.327819824,
            image=image_image_2
        )

        button_1 = Button(
            image=button_image_report,
            borderwidth=0,
            highlightthickness=0,
            command=lambda id=list_of_item[i][0]: open_popup(id),
            relief="flat"
        )
        button_1.place(
            x=629.56103515625,
            y=198.9749755859375 + i*121.595825195,
            width=40.531944274902344,
            height=40.531944274902344
        )

        button_2 = Button(
            image=button_image_see_report,
            borderwidth=0,
            highlightthickness=0,
            command=lambda id=list_of_item[i][0]: print("button_2 clicked"),
            relief="flat"
        )
        button_2.place(
            x=565.341796875,
            y=198.9749755859375 + i*121.595825195,
            width=40.531944274902344,
            height=40.531944274902344
        )

        canvas.create_text(
            82.64306640625,
            202.65966796875 + i*121.595825195,
            anchor="nw",
            text=list_of_item[i][2],
            fill="#3C0505",
            font=("Inter Bold", 23 * -1)
        )


def open_popup(id):
    popup = Toplevel(window)
    popup.geometry("300x200")
    popup.title("Action for ID: " + str(id))
    
    def create_action():
        print(f"Create action for ID {id}")
        popup.destroy()  

    def update_action():
        print(f"Update action for ID {id}")
        popup.destroy()

    def delete_action():
        print(f"Delete action for ID {id}")
        popup.destroy()

    def cancel_action():
        print("Cancel action")
        popup.destroy()

    Button(popup, text="Create", command=create_action, bg="#2F0160", fg="white").pack(pady=10)
    Button(popup, text="Update", command=update_action, bg="#FFD700", fg="white").pack(pady=10)
    Button(popup, text="Delete", command=delete_action, bg="red", fg="white").pack(pady=10)
    Button(popup, text="Cancel", command=cancel_action, bg="black", fg="white").pack(pady=10)





        
