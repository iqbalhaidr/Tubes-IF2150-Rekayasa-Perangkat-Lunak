# main.py
from make_db import create_tables
from UIResource import UIResource
from ResourceManager import ResourceManager
import tkinter as tk

# Membuat tabel terlebih dahulu jika belum ada
create_tables()

# Membuat aplikasi GUI
root = tk.Tk()
resource_manager = ResourceManager("SIMADA.db")
app = UIResource(root, resource_manager)

root.mainloop()
