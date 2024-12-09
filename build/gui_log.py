# build/gui_log.py

import sys
from pathlib import Path

# Menambahkan direktori root proyek ke sys.path
current_dir = Path(__file__).parent.parent
sys.path.append(str(current_dir))

from src.ResourceControl.resource_control import ResourceControl
from src.ReportManager.report_manager import ReportManager

import tkinter as tk
from tkinter import Toplevel, Button, Entry, Label, messagebox
from tkinter import Tk, Canvas, PhotoImage, Frame, Text

# Mendefinisikan path assets
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("assets/frame0")  # Gunakan tanda "/" untuk kompatibilitas lintas platform

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()
window.geometry("758x539")
window.configure(bg="#2F0160")

canvas = Canvas(
    window,
    bg="#2F0160",
    height=539,
    width=758,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)

# List referensi untuk menyimpan PhotoImage agar tidak dihapus oleh garbage collector
image_refs = []

def middle(popup_height, popup_width):
    screen_width = window.winfo_width()
    screen_height = window.winfo_height()
    position_top = window.winfo_rooty() + (screen_height // 2 - popup_height // 2)
    position_left = window.winfo_rootx() + (screen_width // 2 - popup_width // 2)

    return position_top,position_left

def make_element(list_of_item: list):
    button_image_7 = PhotoImage(file=relative_to_assets("button_7.png"))
    image_refs.append(button_image_7)
    button_7 = Button(
        image=button_image_7,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_7 clicked"),
        relief="flat"
    )
    button_7.place(
        x=646.0,
        y=51.0,
        width=58.0,
        height=49.0
    )

    image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
    image_refs.append(image_image_1)
    canvas.create_image(
        410.77978515625,
        73.2166748046875,
        image=image_image_1
    )

    canvas.create_text(
        318.99169921875,
        58.95556640625,
        anchor="nw",
        text="Log Activity",
        fill="#2F0160",
        font=("Inter Bold", 31 * -1)
    )

    canvas.create_text(
        67.904296875,
        58.95556640625,
        anchor="nw",
        text="Inventaris",
        fill="#FFFFFF",
        font=("Inter Bold", 31 * -1)
    )

    canvas.create_rectangle(
        -2.631944417953491,
        100.95566517550947,
        758.0000191605759,
        106.33056640625,
        fill="#FFFFFF",
        outline="")


    image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
    button_image_report = PhotoImage(file=relative_to_assets("button_1.png"))
    button_image_see_report = PhotoImage(file=relative_to_assets("button_2.png"))

    # Simpan referensi gambar
    image_refs.extend([image_image_2, button_image_report, button_image_see_report])

    for i in range(len(list_of_item)):
        # Menampilkan gambar
        canvas.create_image(
            378.48,
            218.81 + i * 121.33,
            image=image_image_2
        )

        # Tombol Report untuk membuka pop-up
        button_1 = Button(
            image=button_image_report,
            borderwidth=0,
            highlightthickness=0,
            command=lambda id=list_of_item[i][0], resource_id=list_of_item[i][1]: open_popup(id, resource_id),
            relief="flat"
        )
        button_1.place(
            x=629.56,
            y=198.97 + i * 121.6,
            width=40.53,
            height=40.53
        )

        # Tombol See Report
        button_2 = Button(
            image=button_image_see_report,
            borderwidth=0,
            highlightthickness=0,
            command=lambda id=list_of_item[i][0]: see_report(id),
            relief="flat"
        )
        button_2.place(
            x=565.34,
            y=198.97 + i * 121.6,
            width=40.53,
            height=40.53
        )

        # Menampilkan teks untuk item
        canvas.create_text(
            82.64,
            202.66 + i * 121.6,
            anchor="nw",
            text=list_of_item[i][2],
            fill="#3C0505",
            font=("Inter Bold", 23 * -1)
        )

def open_popup(id, res_id):
    popup = Toplevel(window)
    popup.geometry("350x150")
    popup.config(bg="#2F0160")  
    popup.grab_set() 
    popup_width = 350
    popup_height = 120
    screen_width = window.winfo_width()
    screen_height = window.winfo_height()

    #Tengah-Tengah
    position_top = window.winfo_rooty() + (screen_height // 2 - popup_height // 2)
    position_left = window.winfo_rootx() + (screen_width // 2 - popup_width // 2)
    popup.geometry(f'{popup_width}x{popup_height}+{position_left}+{position_top}')

    title_label = Label(popup, text="Action for Report in Log", font=("Arial", 14, "bold"), bg="#2F0160", fg="white")
    title_label.pack(pady=10)  

    def create_action():
        popup.destroy()
        rc = ResourceControl()
        already_exist = rc.check_exist_report(id)
        if already_exist:
            messagebox.showinfo("Eror", "Laporan sudah pernah dibuat.")
        else:
            open_form(res_id, id, action="create")

    def update_action():
        popup.destroy()
        rc = ResourceControl()
        already_exist = rc.check_exist_report(id)
        if not already_exist:
            messagebox.showinfo("Eror", "Laporan belum pernah dibuat, tidak ada yang bisa diupdate.")
        else:
            open_form(res_id, id, action="update")

    def delete_action():
        rc = ResourceControl()
        berhasil = rc.delete_report(id)
        if berhasil:
            messagebox.showinfo("Success", f"Laporan dengan ID {id} berhasil dihapus.")
        else:
            messagebox.showerror("Failed", f"Gagal menghapus laporan dengan ID {id}.")
        popup.destroy()

    def cancel_action():
        print("Cancel action")
        popup.destroy()

    button_frame = Frame(popup, bg="#2F0160") 
    button_frame.pack(side="bottom", fill="x", pady=20)

    # Tombol Create, Update, Delete, dan Cancel
    Button(button_frame, text="Create", command=create_action, bg="#28a745", fg="white").pack(side="left", fill="x", expand=True, padx=5)
    Button(button_frame, text="Update", command=update_action, bg="#2196F3", fg="white").pack(side="left", fill="x", expand=True, padx=5)
    Button(button_frame, text="Delete", command=delete_action, bg="red", fg="white").pack(side="left", fill="x", expand=True, padx=5)
    Button(button_frame, text="Cancel", command=cancel_action, bg="black", fg="white").pack(side="left", fill="x", expand=True, padx=5)

def open_form(res_id, id, action):
    # Membuka pop-up baru untuk form input
    form_popup = Toplevel(window)
    popup_width = 400
    popup_height = 300
    
    position_top, position_left=middle(popup_height,popup_width)
    form_popup.geometry(f"{popup_width}x{popup_height}+{position_left}+{position_top}")
    form_popup.config(bg="#2F0160")
    form_popup.grab_set()
    form_popup.title(f"{action.capitalize()} Report for ID: {id}")

    # Label dan input field untuk form
    label_input = Label(form_popup, text=f"Enter detail to {action} Report:", bg="#2F0160", fg="white", font=("Arial", 12))
    label_input.pack(pady=10)

    # Membuat input teks paragraf
    input_field = Text(form_popup, width=50, height=10, font=("Arial", 12), bd=3, relief="solid")
    input_field.pack(pady=5, padx=10)  

    # Fungsi untuk menangani aksi Create
    def submit_create_action(id):
        user_input = input_field.get("1.0", "end-1c")
        if not user_input:
            messagebox.showwarning("Input Error", "Data tidak boleh kosong.")
            return
        rc = ResourceControl()
        berhasil = rc.create_report(res_id, id, user_input)
        if berhasil:
            messagebox.showinfo("Success", "Laporan berhasil dibuat.")
        else:
            messagebox.showerror("Failed", "Gagal membuat laporan.")
        form_popup.destroy()  

    def submit_update_action(id):
        user_input = input_field.get("1.0", "end-1c") 
        if not user_input:
            messagebox.showwarning("Input Error", "Data tidak boleh kosong.")
            return
        rc = ResourceControl()
        berhasil = rc.update_report(id, user_input)
        if berhasil:
            messagebox.showinfo("Success", "Laporan berhasil diperbarui.")
        else:
            messagebox.showerror("Failed", "Gagal memperbarui laporan.")
        form_popup.destroy()  

    # Tombol Submit 
    if action == "create":
        Button(form_popup, text="Submit Create", command=lambda: submit_create_action(id), bg="white", fg="#2F0160", font=("Arial", 12)).pack(pady=10)
    elif action == "update":
        Button(form_popup, text="Submit Update", command=lambda: submit_update_action(id), bg="white", fg="#2F0160", font=("Arial", 12)).pack(pady=10)


def see_report(id):
    control = ResourceControl()
    report = control.get_report_detail_id(id)

    if report:  # Menggunakan 'report' untuk mengecek apakah ada data
        popup = tk.Toplevel()
        popup.geometry("300x300")
        popup.title("Laporan")
        popup.config(bg="#2F0160")
        
        # Frame untuk konten dan scrollbar
        frame = tk.Frame(popup)
        frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        frame.pack_propagate(False)  # Menghentikan frame untuk menyesuaikan dengan konten

        # Membuat widget Text untuk menampilkan laporan
        text_box = tk.Text(frame, wrap="word", font=("Arial", 12), height=10, width=45, 
                           bg="#2F0160", fg="white", bd=0, relief="flat")  # Menggunakan ungu dan tanpa border
        text_box.insert(tk.END, report)  # Memasukkan laporan ke dalam Text box
        text_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Menambahkan scrollbar vertikal
        scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=text_box.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Menyambungkan scrollbar dengan Text box
        text_box.config(yscrollcommand=scrollbar.set)

    else:
        popup = tk.Toplevel()
        popup.geometry("375x100")
        popup.title("Laporan")
        position_top, position_left = middle(300, 100)
        popup.geometry(f"300x100+{position_left-90}+{position_top+100}") 
        popup.grab_set()
        popup.config(bg="#2F0160")
        
        label = tk.Label(popup, text="Maaf, belum ada Laporan untuk Log ini", wraplength=300, bg="#2F0160", fg="white", font=("Arial", 12))
        label.pack(pady=10)

    # Tombol Close yang selalu berada di bawah popup
    close_button = tk.Button(popup, text="Close", command=popup.destroy, bg="#2F0160", fg="white")
    close_button.pack(side=tk.BOTTOM, pady=10)  # Menempatkan tombol di bagian bawah



# Contoh list_of_item dengan format (ID, resource_id, deskripsi)
list_of_item = [
    (1, 1, "Allocate 100 Vibranium to Jakarta"),
    (2, 2, "Distribute 100 Vibranium to Bandung"),
    (3, 3, "Deallocate 50 Vibranium from Jakarta")
]

# Panggil fungsi untuk menampilkan elemen

make_element(list_of_item)

window.resizable(False, False)
window.mainloop()
