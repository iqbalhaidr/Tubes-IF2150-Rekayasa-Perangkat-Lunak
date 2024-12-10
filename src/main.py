# main.py

from UIResource.UIResource import UIResource

from ResourceManager.resource_manager import ResourceManager
import tkinter as tk


if __name__ == "__main__":
# Membuat tabel terlebih dahulu jika belum ada

    # Membuat aplikasi GUI
    root = tk.Tk()
    app = UIResource(root)

    root.mainloop()
