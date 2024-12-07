import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import PhotoImage

class UIResource:
    def __init__(self, root, resource_control):
        self.root = root
        self.root.title("SIMADA")
        self.resource_control = resource_control

        # Ukuran window
        self.root.geometry("778x539")

        # Background color
        self.root.config(bg='#2F0160')

        # Setup halaman pertama
        self.setupFirstPage()

    def setupFirstPage(self):
        """Membuat halaman pertama dengan scrollable canvas"""
        self.first_page = tk.Frame(self.root)
        self.first_page.pack(fill=tk.BOTH, expand=True)

        # Membuat canvas dan scrollable area untuk halaman pertama
        self.canvas_frame_first = tk.Frame(self.first_page)
        self.canvas_frame_first.pack(fill=tk.BOTH, expand=True)

        self.canvas_first = tk.Canvas(self.canvas_frame_first, bg='#2F0160', highlightthickness=0)
        self.canvas_first.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar_first = tk.Scrollbar(self.canvas_frame_first, orient="vertical", command=self.canvas_first.yview, width=20)
        self.scrollbar_first.pack(side=tk.RIGHT, fill=tk.Y)

        self.canvas_first.configure(yscrollcommand=self.scrollbar_first.set)

        self.scrollable_frame_first = tk.Frame(self.canvas_first, bg='#2F0160')
        self.canvas_first.create_window((0, 0), window=self.scrollable_frame_first, anchor="nw")

        self.scrollable_frame_first.bind("<Configure>", lambda e: self.canvas_first.configure(scrollregion=self.canvas_first.bbox("all")))

        # Menampilkan tampilan utama
        self.setupFirstPageContent()

    
    def setupFirstPageContent(self):
        """Membuat halaman utama UI dengan menyesuaikan posisi elemen"""
        # Membuat label dengan teks 'SIMADA' yang diposisikan di kiri atas
        headerAwal = tk.Label(self.scrollable_frame_first, text="SIMADA", font=("Arial", 20, "bold"), bg='#2F0160', fg='yellow')
        headerAwal.pack(pady=(30, 0), anchor="w", padx=(50, 10))  # anchor="w" agar di kiri, padx memberi ruang di kiri

        namaPage = tk.Label(self.scrollable_frame_first, text="Daftar Resource", font=("Arial", 25, "bold"), bg='#2F0160', fg='white')
        namaPage.pack(pady=(0, 6), anchor="center", padx=10)  # Mengatur anchor ke tengah

        # Menambahkan tombol 'Tambah Resource' di sisi kiri
        self.loadImage = tk.PhotoImage(file="../img/tambahButton.png")  # Pastikan path relatif benar

        # Membuat tombol dengan gambar
        self.tambahButton = tk.Button(self.scrollable_frame_first, image=self.loadImage, command=self.onButtonClick, bd=0, highlightthickness=0)
        self.tambahButton.pack(pady=20, anchor="w", padx=(50, 10))  # Menambahkan padding untuk memberi ruang antar elemen

        self.bgImage = PhotoImage(file="../img/bar.png")
        self.allocateButtonImage = PhotoImage(file="../img/allocateButton.png")
        self.deleteButton1Image = PhotoImage(file="../img/deleteButton1.png")
        self.editButtonImage = PhotoImage(file="../img/editButton.png")
        self.InventarisButtonImage = PhotoImage(file="../img/InventarisButton.png")
        
        # Menampilkan daftar Resource (contoh: vibranium dan adamantium)
        resources = [
            {"name": "Vibranium", "quantity": 100, "location": "Wakanda"},
            {"name": "Adamantium", "quantity": 50, "location": "Xandar"},
            {"name": "Besi tua madura", "quantity": 50, "location": "Xandar"},
            {"name": "kontol", "quantity": 50, "location": "Xandar"},
        ]

        # Membuat frame untuk setiap resource dan menambahkan tombol edit, hapus, dan request stock
        for resource in resources:
            self.createResourceRow(resource)
        self.root.after(100, self.check1_size)

    def check1_size(self):
        print(f"Width: {self.scrollable_frame_first.winfo_width()}")
        print(f"Height: {self.scrollable_frame_first.winfo_height()}")
        print(f"Geometry: {self.scrollable_frame_first.winfo_geometry()}")

    def createResourceRow(self, resource):
        """Membuat baris dengan gambar sebagai background."""        
        # Canvas untuk menampilkan gambar sebagai background
        resourceCanvas = tk.Canvas(self.scrollable_frame_first, width=678, height=91, bg='#2F0160', highlightthickness=0)
        resourceCanvas.pack(anchor="w", padx=50, pady=(10, 10), fill="x")  # Padding untuk jarak antar elemen

        # Menambahkan gambar sebagai background
        resourceCanvas.create_image(0, 0, anchor="nw", image=self.bgImage)
        resourceCanvas.image = self.bgImage  # Menyimpan referensi agar gambar tidak hilang

        # Menambahkan elemen di atas gambar (menggunakan koordinat)
        nameLabel = tk.Label(self.scrollable_frame_first, text=resource["name"], font=("Arial", 20, "bold"), bg="#F7F7F7", fg="black")
        resourceCanvas.create_window(30, 45, anchor="w", window=nameLabel)  # Label di kiri atas (disesuaikan dengan koordinat)

        # Tambahkan tombol "Edit" dengan gambar
        allocateButton = tk.Button(
            self.scrollable_frame_first,
            image=self.allocateButtonImage,
            command=lambda: self.formAllocateResource(resource["name"]),
            bd=0,  # Tanpa border
            highlightthickness=0,  # Tanpa highlight border
            bg="#2F0160",  # Sesuaikan dengan warna latar belakang canvas
            activebackground="#2F0160"  # Warna latar belakang saat tombol diklik
        )
        resourceCanvas.create_window(340, 45, anchor="w", window=allocateButton)
        
        # Tambahkan tombol "Edit" dengan gambar
        editButton = tk.Button(
            self.scrollable_frame_first,
            image=self.editButtonImage,
            command=lambda: self.formUpdateResource(resource["name"]),
            bd=0,  # Tanpa border
            highlightthickness=0,  # Tanpa highlight border
            bg="#2F0160",  # Sesuaikan dengan warna latar belakang canvas
            activebackground="#2F0160"  # Warna latar belakang saat tombol diklik
        )
        resourceCanvas.create_window(425, 45, anchor="w", window=editButton)

        # Tambahkan tombol "Hapus" dengan gambar
        deleteButton1 = tk.Button(
            self.scrollable_frame_first,
            image=self.deleteButton1Image,
            command=lambda: self.deleteResource(resource["name"]),
            bd=0,
            highlightthickness=0,
            bg="#2F0160",
            activebackground="#2F0160"
        )
        resourceCanvas.create_window(505, 45, anchor="w", window=deleteButton1)

        # Tambahkan tombol "Request Stock" dengan gambar
        InventarisButton = tk.Button(
            self.scrollable_frame_first,
            image=self.InventarisButtonImage,
            command=lambda: self.goToSecondPage(),
            bd=0,
            highlightthickness=0,
            bg="#2F0160",
            activebackground="#2F0160"
        )
        resourceCanvas.create_window(590, 45, anchor="w", window=InventarisButton)

    def onButtonClick(self):
        """Menangani klik pada tombol 'Tambah Resource' dengan gambar"""
        print("Tombol 'Tambah Resource' dengan gambar diklik!")
        # Menampilkan form untuk menambahkan Resource
        self.formCreateResource()

    def formCreateResource(self):
        """Menampilkan form untuk membuat resource baru.""" 
        createWindow = tk.Toplevel(self.root)
        createWindow.title("Tambah Resource")
        createWindow.config(bg='#2F0160')
        createWindow.geometry("510x310")  # Sesuaikan ukuran pop-up

        # Load gambar input field
        input_bg = tk.PhotoImage(file="../img/inputField.png")

        # Header Form
        headerPage = tk.Label(createWindow, text="Create Resource", font=("Arial", 16, "bold"), bg='#2F0160', fg='white')
        headerPage.pack(pady=(10, 2), anchor="w", padx=15)

        descPage = tk.Label(createWindow, text="Silakan lengkapi isian berikut untuk menambah resource baru", font=("Arial", 10), bg='#2F0160', fg='white')
        descPage.pack(pady=(2, 12), anchor="w", padx=15)

        # Nama Resource
        nameFrame = tk.Frame(createWindow, bg='#2F0160')
        nameFrame.pack(anchor="w", padx=15, pady=(5, 5))

        nameLabel = tk.Label(nameFrame, text="Nama Resource:", bg='#2F0160', fg='white', font=("Arial", 12))
        nameLabel.pack(side="left")

        nameCanvas = tk.Canvas(nameFrame, width=230, height=32, bg='#2F0160', highlightthickness=0)
        nameCanvas.pack(side="left", padx=(10, 0))
        nameCanvas.create_image(0, 0, image=input_bg, anchor="nw")
        
        nameEntry = tk.Entry(nameCanvas, font=("Arial", 12), bg="#ffffff", bd=0, justify="left")
        nameEntry.place(x=10, y=5, width=210, height=22)  # Sesuaikan ukuran dan posisi entry

        # quantity Resource
        quantityFrame = tk.Frame(createWindow, bg='#2F0160')
        quantityFrame.pack(anchor="w", padx=15, pady=(5, 5))

        quantityLabel = tk.Label(quantityFrame, text="Jumlah Resource:", bg='#2F0160', fg='white', font=("Arial", 12))
        quantityLabel.pack(side="left")

        quantityCanvas = tk.Canvas(quantityFrame, width=230, height=32, bg='#2F0160', highlightthickness=0)
        quantityCanvas.pack(side="left", padx=(10, 0))
        quantityCanvas.create_image(0, 0, image=input_bg, anchor="nw")
        
        quantityEntry = tk.Entry(quantityCanvas, font=("Arial", 12), bg="#ffffff", bd=0, justify="left")
        quantityEntry.place(x=10, y=5, width=210, height=22)  # Sesuaikan ukuran dan posisi entry

        
        # tesLabel = tk.Label(createWindow, text="Nama Resource:", bg='#2F0160', fg='white', font=("Arial", 12))
        # tesLabel.pack(padx=(5,0), pady=(5,10))

        submitButton = tk.Button(
        createWindow,
        text="Tambah",
        bg="darkorange",
        fg="white",
        activebackground="orange",
        activeforeground="black",
        relief="flat",
        font=("Arial", 12),
        command=lambda: self.addNewResource(nameEntry, quantityEntry, createWindow)
        )
        submitButton.pack(anchor="w", padx=(310, 25), pady=(10, 10))  # Mengurangi jarak vertikal dengan mengatur pady


        # Menyimpan referensi ke gambar agar tidak hilang
        createWindow.input_bg = input_bg




    def addNewResource(self, nameEntry, quantityEntry, window):
        """Menangani penambahan resource baru.""" 
        name = nameEntry.get()
        try:
            quantity = int(quantityEntry.get())

            # Panggil metode ResourceControl untuk menambah resource
            message = self.resource_control.add_resource(name, quantity)
            messagebox.showinfo("Informasi", message)
        except ValueError:
            messagebox.showerror("Error", "Jumlah harus berupa angka yang valid!")
        window.destroy()
    
    def formAllocateResource(self, resource_name):
        """Menangani form untuk mengupdate resource."""        
        allocateWindow = tk.Toplevel(self.root)
        allocateWindow.title("Update Resource")
        allocateWindow.config(bg='#2F0160')
        allocateWindow.geometry("510x265")
        
        # Load gambar input field
        input_bg = tk.PhotoImage(file="../img/inputField.png")
        nameEntry = resource_name

        # Header Form
        headerPage = tk.Label(allocateWindow, 
                          text=f"Allocate Resource {resource_name}",  # Nama resource disisipkan ke dalam teks
                          font=("Arial", 16, "bold"),
                          bg='#2F0160', fg='white')
        headerPage.pack(pady=(10, 2), anchor="w", padx=15)
        
        descPage = tk.Label(allocateWindow, text="Silakan alokasi Resource pada lokasi yang ingin dituju beserta quantity nya", font=("Arial", 10), bg='#2F0160', fg='white')
        descPage.pack(pady=(2, 12), anchor="w", padx=15)

        # Lokasi Resource yang ingin dialokasi
        newLocationFrame = tk.Frame(allocateWindow, bg='#2F0160')
        newLocationFrame.pack(anchor="w", padx=15, pady=(5, 5))

        newLocationLabel = tk.Label(newLocationFrame, text="Lokasi Tujuan Resource:", bg='#2F0160', fg='white', font=("Arial", 12))
        newLocationLabel.pack(side="left")

        newLocationCanvas = tk.Canvas(newLocationFrame, width=230, height=32, bg='#2F0160', highlightthickness=0)
        newLocationCanvas.pack(side="left", padx=(10, 0))
        newLocationCanvas.create_image(0, 0, image=input_bg, anchor="nw")
        
        newLocationEntry = tk.Entry(newLocationCanvas, font=("Arial", 12), bg="#ffffff", bd=0, justify="left")
        newLocationEntry.place(x=10, y=5, width=210, height=22)  
        
        # Alokasi Quantity
        quantityFrame = tk.Frame(allocateWindow, bg='#2F0160')
        quantityFrame.pack(anchor="w", padx=15, pady=(5, 5))

        quantityLabel = tk.Label(quantityFrame, text="Jumlah Quantity alokasi:", bg='#2F0160', fg='white', font=("Arial", 12))
        quantityLabel.pack(side="left")

        quantityCanvas = tk.Canvas(quantityFrame, width=230, height=32, bg='#2F0160', highlightthickness=0)
        quantityCanvas.pack(side="left", padx=(10, 0))
        quantityCanvas.create_image(0, 0, image=input_bg, anchor="nw")
        
        quantityEntry = tk.Entry(quantityCanvas, font=("Arial", 12), bg="#ffffff", bd=0, justify="left")
        quantityEntry.place(x=10, y=5, width=210, height=22)  

        submitButton = tk.Button(
            allocateWindow,
            text="Allocate",
            bg="blue",
            fg="white",
            activebackground="darkblue",
            activeforeground="yellow",
            relief="flat",
            font=("Arial", 12),
            command=lambda: self.allocateResourceQuantity(nameEntry, newLocationEntry, quantityEntry, allocateWindow)
        )
        submitButton.pack(anchor="w", padx=(360, 25), pady=(10, 10))
        
        allocateWindow.input_bg = input_bg
        
    def allocateResource(self, nameEntry, newLocationEntry, quantityEntry, allocateWindow):
        """Mengupdate jumlah resource."""        
        name = nameEntry.get()
        try:
            location = newLocationEntry.get()
            quantity = int(quantityEntry.get())
            message = self.resource_control.allocate_resource(name, location, quantity)
            messagebox.showinfo("Informasi", message)
        except ValueError:
            messagebox.showerror("Error", "Jumlah harus berupa angka yang valid!")
        allocateWindow.destroy()

    def formUpdateResource(self, resource_name):
        """Menangani form untuk mengupdate resource."""        
        updateWindow = tk.Toplevel(self.root)
        updateWindow.title("Update Resource")
        updateWindow.config(bg='#2F0160')
        updateWindow.geometry("510x200")
        
        # Load gambar input field
        input_bg = tk.PhotoImage(file="../img/inputField.png")
        nameEntry = resource_name

        # Header Form
        headerPage = tk.Label(updateWindow, 
                              text=f"Update Resource {resource_name}", 
                              font=("Arial", 16, "bold"), 
                              bg='#2F0160', fg='white')
        headerPage.pack(pady=(10, 2), anchor="w", padx=15)
        
        descPage = tk.Label(updateWindow, text="Silakan update quantity resource", font=("Arial", 10), bg='#2F0160', fg='white')
        descPage.pack(pady=(2, 12), anchor="w", padx=15)

        # quantity Resource
        newQuantityFrame = tk.Frame(updateWindow, bg='#2F0160')
        newQuantityFrame.pack(anchor="w", padx=15, pady=(5, 5))

        newQuantityLabel = tk.Label(newQuantityFrame, text="Jumlah quantity baru:", bg='#2F0160', fg='white', font=("Arial", 12))
        newQuantityLabel.pack(side="left")

        newQuantityCanvas = tk.Canvas(newQuantityFrame, width=230, height=32, bg='#2F0160', highlightthickness=0)
        newQuantityCanvas.pack(side="left", padx=(10, 0))
        newQuantityCanvas.create_image(0, 0, image=input_bg, anchor="nw")
        
        newQuantityEntry = tk.Entry(newQuantityCanvas, font=("Arial", 12), bg="#ffffff", bd=0, justify="left")
        newQuantityEntry.place(x=10, y=5, width=210, height=22)  

        submitButton = tk.Button(
            updateWindow,
            text="Update",
            bg="blue",
            fg="white",
            activebackground="darkblue",
            activeforeground="yellow",
            relief="flat",
            font=("Arial", 12),
            command=lambda: self.updateResourceQuantity(nameEntry, newQuantityEntry, updateWindow)
        )
        submitButton.pack(anchor="w", padx=(340, 25), pady=(10, 10))
        updateWindow.input_bg = input_bg

    def updateResourceQuantity(self, nameEntry, newQuantityEntry, updateWindow):
        """Mengupdate jumlah resource."""        
        name = nameEntry.get()
        try:
            newQuantity = int(newQuantityEntry.get())
            message = self.resource_control.update_resource_quantity(name, newQuantity)
            messagebox.showinfo("Informasi", message)
        except ValueError:
            messagebox.showerror("Error", "Jumlah harus berupa angka yang valid!")
        updateWindow.destroy()

    def deleteResource(self, resource_name):
        """Menangani klik tombol Hapus."""        
        print(f"Delete resource {resource_name}")
        # Tambahkan logika untuk menghapus resource di sini
        messagebox.showinfo("Informasi", f"Resource {resource_name} telah dihapus.")

    def requestStockDetails(self, resource_name):
        """Menangani klik tombol Request Stock Detail.""" 
        print(f"Request stock details for {resource_name}")
        # Tambahkan logika untuk meminta detail quantity di sini
        messagebox.showinfo("Informasi", f"Detail quantity untuk {resource_name} telah diminta.")
        
    def setupSecondPage(self):
        """Menyiapkan halaman kedua dengan scrollable canvas dan tab"""
        self.second_page = tk.Frame(self.root)
        self.second_page.pack(fill=tk.BOTH, expand=True)  
        # Pastikan halaman kedua tidak terlihat pada awalnya

        # Membuat canvas dan scrollable area untuk halaman kedua
        self.canvas_frame_second = tk.Frame(self.second_page)
        self.canvas_frame_second.pack(fill=tk.BOTH, expand=True)  # Memastikan canvas frame mengisi seluruh layar

        self.canvas_second = tk.Canvas(self.canvas_frame_second, bg='#2F0160', highlightthickness=0)
        self.canvas_second.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)  # Memastikan canvas mengisi seluruh area

        self.scrollbar_second = tk.Scrollbar(self.canvas_frame_second, orient="vertical", command=self.canvas_second.yview, width=20)
        self.scrollbar_second.pack(side=tk.RIGHT, fill=tk.Y)

        self.canvas_second.configure(yscrollcommand=self.scrollbar_second.set)

        self.scrollable_frame_second = tk.Frame(self.canvas_second, bg='#2F0160')
        self.canvas_second.create_window((0, 0), window=self.scrollable_frame_second, anchor="nw")

        self.scrollable_frame_second.bind("<Configure>", lambda e: self.canvas_second.configure(scrollregion=self.canvas_second.bbox("all")))

        # Menampilkan halaman kedua
        self.setupSecondPageContent()

        # Pastikan halaman kedua mengisi seluruh layar
        # Ini memastikan halaman kedua mengisi layar

    def setupSecondPageContent(self):
        """Menyiapkan pusat konten halaman kedua dengan mekanisme tab tanpa Notebook"""
        # Membuat area untuk kontrol tab
        tab_control_frame = tk.Frame(self.scrollable_frame_second, bg="#2F0160")
        tab_control_frame.pack(fill=tk.X, pady=(10, 0))

        # Membuat area untuk konten tab
        self.tab_content_frame = tk.Frame(self.scrollable_frame_second, bg="#2F0160")
        self.tab_content_frame.pack(fill=tk.BOTH, expand=True, pady=(10, 0))

        # Tombol untuk berpindah antar-tab
        inventory_button = tk.Button(
            tab_control_frame, 
            text="Inventaris", 
            font=("Arial", 12), 
            bg="darkorange", 
            fg="white", 
            command=lambda: self.showTab(self.showInventoryContent)
        )
        inventory_button.pack(anchor="center", padx=5)

        log_activity_button = tk.Button(
            tab_control_frame, 
            text="Log Aktivitas", 
            font=("Arial", 12), 
            bg="darkorange", 
            fg="white", 
            command=lambda: self.showTab(self.showLogActivityContent)
        )
        log_activity_button.pack(anchor="center", padx=5)

        # Tombol kembali ke halaman utama
        backButton = tk.Button(
            self.scrollable_frame_second, 
            text="Kembali ke Halaman Utama", 
            command=self.goToMainPage, 
            bg="darkorange", 
            fg="white", 
            font=("Arial", 12)
        )
        backButton.pack(pady=10)

        # Tampilkan tab inventaris secara default
        self.showTab(self.showInventoryContent)

    def showInventoryContent(self):
        """Menampilkan konten tab Inventaris"""
        # Bersihkan tab konten
        for widget in self.tab_content_frame.winfo_children():
            widget.destroy()

        # Tambahkan konten inventaris
        self.bgImage = PhotoImage(file="../img/barInventory.png")
        self.quantityImage = PhotoImage(file="../img/quantityInventory.png")
        self.distributeButtonImage = PhotoImage(file="../img/distributeButton.png")
        self.deleteButton2Image = PhotoImage(file="../img/deleteButton2.png")
        
        inventaris = [
            {"location": "JAKARTA", "quantity": 600},
            {"location": "BANDUNG", "quantity": 777},
            {"location": "WAKANDA", "quantity": 888},
        ]
        
        for inventory in inventaris:
            self.createInventoryRow(inventory)
    
    def createInventoryRow(self, inventory):
        inventoryCanvas = tk.Canvas(self.tab_content_frame, width=678, height=91, bg='#2F0160', highlightthickness=0)
        inventoryCanvas.pack(anchor="w", padx=50, pady=(10, 10), fill="x")  # Padding untuk jarak antar elemen

        # Menambahkan gambar sebagai background
        inventoryCanvas.create_image(0, 0, anchor="nw", image=self.bgImage)
        inventoryCanvas.image = self.bgImage 
        
        # Menambahkan elemen di atas gambar (menggunakan koordinat)
        nameLabel = tk.Label(self.tab_content_frame, text=inventory["location"], font=("Arial", 20, "bold"), bg="#F7F7F7", fg="black")
        inventoryCanvas.create_window(30, 45, anchor="w", window=nameLabel)  # Label di kiri atas (disesuaikan dengan koordinat)
        
        inventoryCanvas.create_image(315, 22, anchor="nw", image=self.quantityImage)
        inventoryCanvas.image = self.quantityImage 
        
        QuantityLabel = tk.Label(self.tab_content_frame, text=f'{inventory["quantity"]}', font=("Arial", 20, "bold"), bg="#2F0160", fg="white")
        inventoryCanvas.create_window(405, 45, anchor="w", window=QuantityLabel)  # Label di kiri atas (disesuaikan dengan koordinat)
        
        # Tambahkan tombol "Hapus" dengan gambar
        deleteButton2 = tk.Button(
            self.tab_content_frame,
            image=self.deleteButton2Image,
            command=lambda: self.delete(inventory["location"]),
            bd=0,
            highlightthickness=0,
            bg="#2F0160",
            activebackground="#2F0160"
        )
        inventoryCanvas.create_window(515, 45, anchor="w", window=deleteButton2)
        
        distributeButton = tk.Button(
            self.tab_content_frame,
            image=self.distributeButtonImage,
            command=lambda: self.distributeResource(inventory["location"]),
            bd=0,
            highlightthickness=0,
            bg="#2F0160",
            activebackground="#2F0160"
        )
        inventoryCanvas.create_window(605, 45, anchor="w", window=distributeButton)
        
        # Tampilkan jumlah kuantitas
        
        
            

    def showLogActivityContent(self):
        """Menampilkan konten tab Log Aktivitas"""
        # Bersihkan tab konten
        for widget in self.tab_content_frame.winfo_children():
            widget.destroy()

        # Tambahkan konten log aktivitas
        log_label = tk.Label(self.tab_content_frame, text="Log Aktivitas", font=("Arial", 16, "bold"), bg="#2F0160", fg="white")
        log_label.pack(pady=20)

        tk.Label(self.tab_content_frame, text="(Isi log aktivitas di sini)", bg="#2F0160", fg="white").pack()

        # Contoh log aktivitas
        log_entries = ["User1 menambahkan inventaris.", "User2 memperbarui data logistik."]
        for log in log_entries:
            tk.Label(self.tab_content_frame, text=f"- {log}", bg="#2F0160", fg="white").pack(anchor="w", padx=20)

    def showTab(self, content_function):
        """Membersihkan konten tab sebelumnya dan menampilkan konten baru"""
        # Bersihkan semua konten tab sebelumnya
        for widget in self.tab_content_frame.winfo_children():
            widget.destroy()

        # Tampilkan konten tab baru
        content_function()


    def check_size(self):
        print(f"Width: {self.scrollable_frame_second.winfo_width()}")
        print(f"Height: {self.scrollable_frame_second.winfo_height()}")
        print(f"Geometry: {self.scrollable_frame_second.winfo_geometry()}")


    def goToSecondPage(self):
        """Berpindah ke halaman kedua"""
        self.first_page.pack_forget()  # Sembunyikan halaman pertama
        self.setupSecondPage()  # Tampilkan halaman kedua

    def goToMainPage(self):
        """Kembali ke halaman pertama"""
        self.second_page.pack_forget()  # Sembunyikan halaman kedua
        self.first_page.pack(fill="both", expand=True)  # Tampilkan halaman pertama lagi

  
        
