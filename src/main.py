# main.py
from make_db import create_tables
from UIResource.UIResource import UIResource
from ResourceManager.resource_manager import ResourceManager
import tkinter as tk


if __name__ == "__main__":
# Membuat tabel terlebih dahulu jika belum ada
    create_tables()

    # Membuat aplikasi GUI
    root = tk.Tk()
    resource_manager = ResourceManager("SIMADA.db")
    app = UIResource(root, resource_manager)

    root.mainloop()
