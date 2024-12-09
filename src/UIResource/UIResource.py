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
        self.firstPage = tk.Frame(self.root)
        self.firstPage.pack(fill=tk.BOTH, expand=True)

        # Membuat canvas dan scrollable area untuk halaman pertama
        self.firstPageCanvasFrame = tk.Frame(self.firstPage)
        self.firstPageCanvasFrame.pack(fill=tk.BOTH, expand=True)

        self.firstPageCanvas = tk.Canvas(self.firstPageCanvasFrame, bg='#2F0160', highlightthickness=0)
        self.firstPageCanvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.firstPageScrollbar = tk.Scrollbar(self.firstPageCanvasFrame, orient="vertical", command=self.firstPageCanvas.yview, width=20)
        self.firstPageScrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.firstPageCanvas.configure(yscrollcommand=self.firstPageScrollbar.set)

        self.firstPageScrollableFrame = tk.Frame(self.firstPageCanvas, bg='#2F0160')
        self.firstPageCanvas.create_window((0, 0), window=self.firstPageScrollableFrame, anchor="nw")

        self.firstPageScrollableFrame.bind("<Configure>", lambda e: self.firstPageCanvas.configure(scrollregion=self.firstPageCanvas.bbox("all")))

        self.setupFirstPageContent()

    
    def setupFirstPageContent(self):
        """Membuat halaman utama UI dengan menyesuaikan posisi elemen"""
        headerAwal = tk.Label(self.firstPageScrollableFrame, text="SIMADA", font=("Arial", 20, "bold"), bg='#2F0160', fg='yellow')
        headerAwal.pack(pady=(30, 0), anchor="w", padx=(50, 10))  

        namaPage = tk.Label(self.firstPageScrollableFrame, text="Daftar Resource", font=("Arial", 25, "bold"), bg='#2F0160', fg='white')
        namaPage.pack(pady=(0, 6), anchor="center", padx=10)  # 

        # Menambahkan tombol 'Tambah Resource' di sisi kiri
        self.loadImage = tk.PhotoImage(file="img/tambahButton.png")  

        self.tambahButton = tk.Button(self.firstPageScrollableFrame, image=self.loadImage, command=self.onButtonClick, bd=0, highlightthickness=0)
        self.tambahButton.pack(pady=20, anchor="w", padx=(50, 10))  

        self.bgImage = PhotoImage(file="img/bar.png")
        self.allocateButtonImage = PhotoImage(file="img/allocateButton.png")
        self.deleteButton1Image = PhotoImage(file="img/deleteButton1.png")
        self.editButtonImage = PhotoImage(file="img/editButton.png")
        self.InventarisButtonImage = PhotoImage(file="img/InventarisButton.png")
        
        # DUMMY MAS
        resources = [
            {"name": "Vibranium", "quantity": 100, "location": "Wakanda"},
            {"name": "Adamantium", "quantity": 50, "location": "Xandar"},
            {"name": "Besi tua madura", "quantity": 50, "location": "Xandar"},
            {"name": "kontol", "quantity": 50, "location": "Xandar"},
        ]

        for resource in resources:
            self.createResourceRow(resource)
        self.root.after(100, self.check1_size)

    def check1_size(self):
        print(f"Width: {self.firstPageScrollableFrame.winfo_width()}")
        print(f"Height: {self.firstPageScrollableFrame.winfo_height()}")
        print(f"Geometry: {self.firstPageScrollableFrame.winfo_geometry()}")

    def createResourceRow(self, resource):
        """Membuat baris dengan gambar sebagai background."""        
        resourceCanvas = tk.Canvas(self.firstPageScrollableFrame, width=678, height=91, bg='#2F0160', highlightthickness=0)
        resourceCanvas.pack(anchor="w", padx=50, pady=(10, 10), fill="x")  # Padding untuk jarak antar elemen

        # Menambahkan gambar sebagai background
        resourceCanvas.create_image(0, 0, anchor="nw", image=self.bgImage)
        resourceCanvas.image = self.bgImage  # Menyimpan referensi agar gambar tidak hilang

        nameLabel = tk.Label(self.firstPageScrollableFrame, text=resource["name"], font=("Arial", 20, "bold"), bg="#F7F7F7", fg="black")
        resourceCanvas.create_window(30, 45, anchor="w", window=nameLabel)  
        # Tambahkan tombol "Edit" dengan gambar
        allocateButton = tk.Button(
            self.firstPageScrollableFrame, image=self.allocateButtonImage,
            command=lambda: self.formAllocateResource(resource["name"]),
            bd=0,  
            highlightthickness=0,  
            bg="#2F0160",  
            activebackground="#2F0160"  
        )
        resourceCanvas.create_window(340, 45, anchor="w", window=allocateButton)
        
        # Tambahkan tombol "Edit" dengan gambar
        editButton = tk.Button(
            self.firstPageScrollableFrame,image=self.editButtonImage,
            command=lambda: self.formUpdateResource(resource["name"]),
            bd=0,  
            highlightthickness=0,  
            bg="#2F0160",  # Sesuaikan dengan warna latar belakang canvas
            activebackground="#2F0160"  # Warna latar belakang saat tombol diklik
        )
        resourceCanvas.create_window(425, 45, anchor="w", window=editButton)

        # Tambahkan tombol "Hapus" dengan gambar
        deleteButton1 = tk.Button(
            self.firstPageScrollableFrame,
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
            self.firstPageScrollableFrame,
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
        self.formCreateResource()

    def formCreateResource(self):
        """Menampilkan form untuk membuat resource baru.""" 
        createWindow = tk.Toplevel(self.root)
        createWindow.title("Tambah Resource")
        createWindow.config(bg='#2F0160')
        createWindow.geometry("510x310")  # Sesuaikan ukuran pop-up

        # Load gambar input field
        inputFieldBG = tk.PhotoImage(file="img/inputField.png")

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
        nameCanvas.create_image(0, 0, image=inputFieldBG, anchor="nw")
        
        nameEntry = tk.Entry(nameCanvas, font=("Arial", 12), bg="#ffffff", bd=0, justify="left")
        nameEntry.place(x=10, y=5, width=210, height=22)  # Sesuaikan ukuran dan posisi entry

        # quantity Resource
        quantityFrame = tk.Frame(createWindow, bg='#2F0160')
        quantityFrame.pack(anchor="w", padx=15, pady=(5, 5))

        quantityLabel = tk.Label(quantityFrame, text="Jumlah Resource:", bg='#2F0160', fg='white', font=("Arial", 12))
        quantityLabel.pack(side="left")

        quantityCanvas = tk.Canvas(quantityFrame, width=230, height=32, bg='#2F0160', highlightthickness=0)
        quantityCanvas.pack(side="left", padx=(10, 0))
        quantityCanvas.create_image(0, 0, image=inputFieldBG, anchor="nw")
        
        quantityEntry = tk.Entry(quantityCanvas, font=("Arial", 12), bg="#ffffff", bd=0, justify="left")
        quantityEntry.place(x=10, y=5, width=210, height=22)  

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
        createWindow.inputFieldBG = inputFieldBG

    def addNewResource(self, nameEntry, quantityEntry, window):
        """Menangani penambahan resource baru.""" 
        name = nameEntry.get()
        try:
            quantity = int(quantityEntry.get())
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
        inputFieldBG = tk.PhotoImage(file="img/inputField.png")
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
        newLocationCanvas.create_image(0, 0, image=inputFieldBG, anchor="nw")
        
        newLocationEntry = tk.Entry(newLocationCanvas, font=("Arial", 12), bg="#ffffff", bd=0, justify="left")
        newLocationEntry.place(x=10, y=5, width=210, height=22)  
        
        # Alokasi Quantity
        quantityFrame = tk.Frame(allocateWindow, bg='#2F0160')
        quantityFrame.pack(anchor="w", padx=15, pady=(5, 5))

        quantityLabel = tk.Label(quantityFrame, text="Jumlah Quantity alokasi:", bg='#2F0160', fg='white', font=("Arial", 12))
        quantityLabel.pack(side="left")

        quantityCanvas = tk.Canvas(quantityFrame, width=233, height=32, bg='#2F0160', highlightthickness=0)
        quantityCanvas.pack(side="left", padx=(10, 0))
        quantityCanvas.create_image(3, 0, image=inputFieldBG, anchor="nw")
        
        quantityEntry = tk.Entry(quantityCanvas, font=("Arial", 12), bg="#ffffff", bd=0, justify="left")
        quantityEntry.place(x=13, y=5, width=210, height=22)  

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
        
        allocateWindow.inputFieldBG = inputFieldBG
        
    def allocateResourceQuantity(self, nameEntry, newLocationEntry, quantityEntry, allocateWindow):
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
        inputFieldBG = tk.PhotoImage(file="img/inputField.png")
        nameEntry = resource_name

        # Header Form
        headerPage = tk.Label(updateWindow, 
                              text=f"Update Resource {resource_name}", 
                              font=("Arial", 16, "bold"), 
                              bg='#2F0160', fg='white')
        headerPage.pack(pady=(10, 2), anchor="w", padx=15)
        
        descPage = tk.Label(updateWindow, 
                            text="Silakan update quantity resource", 
                            font=("Arial", 10),
                            bg='#2F0160', fg='white')
        descPage.pack(pady=(2, 12), anchor="w", padx=15)

        newQuantityFrame = tk.Frame(updateWindow, bg='#2F0160')
        newQuantityFrame.pack(anchor="w", padx=15, pady=(5, 5))

        newQuantityLabel = tk.Label(newQuantityFrame, text="Jumlah quantity baru:", bg='#2F0160', fg='white', font=("Arial", 12))
        newQuantityLabel.pack(side="left")

        newQuantityCanvas = tk.Canvas(newQuantityFrame, width=230, height=32, bg='#2F0160', highlightthickness=0)
        newQuantityCanvas.pack(side="left", padx=(10, 0))
        newQuantityCanvas.create_image(0, 0, image=inputFieldBG, anchor="nw")
        
        newQuantityEntry = tk.Entry(newQuantityCanvas, font=("Arial", 12), bg="#ffffff", bd=0, justify="left")
        newQuantityEntry.place(x=10, y=5, width=210, height=22)  

        submitButton = tk.Button(
            updateWindow,text="Update",
            bg="blue",
            fg="white",
            activebackground="darkblue",
            activeforeground="yellow",
            relief="flat",
            font=("Arial", 12),
            command=lambda: self.updateResourceQuantity(nameEntry, newQuantityEntry, updateWindow)
        )
        submitButton.pack(anchor="w", padx=(340, 25), pady=(10, 10))
        updateWindow.inputFieldBG = inputFieldBG

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

        
    def setupSecondPage(self):
        """Menyiapkan halaman kedua dengan scrollable canvas dan tab"""
        self.secondPage = tk.Frame(self.root)
        self.secondPage.pack(fill=tk.BOTH, expand=True)  
        # Pastikan halaman kedua tidak terlihat pada awalnya

        # Membuat canvas dan scrollable area untuk halaman kedua
        self.canvasFrameSecond = tk.Frame(self.secondPage)
        self.canvasFrameSecond.pack(fill=tk.BOTH, expand=True)  # Memastikan canvas frame mengisi seluruh layar

        self.canvas_second = tk.Canvas(self.canvasFrameSecond, bg='#2F0160', highlightthickness=0)
        self.canvas_second.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)  # Memastikan canvas mengisi seluruh area

        self.scrollbar_second = tk.Scrollbar(self.canvasFrameSecond, orient="vertical", command=self.canvas_second.yview, width=20)
        self.scrollbar_second.pack(side=tk.RIGHT, fill=tk.Y)

        self.canvas_second.configure(yscrollcommand=self.scrollbar_second.set)

        self.secondPageScrollableFrame = tk.Frame(self.canvas_second, bg='#2F0160')
        self.canvas_second.create_window((0, 0), window=self.secondPageScrollableFrame, anchor="nw")

        self.secondPageScrollableFrame.bind("<Configure>", lambda e: self.canvas_second.configure(scrollregion=self.canvas_second.bbox("all")))
        self.setupSecondPageContent()

    def setupSecondPageContent(self):
        self.currentActiveTab = 'inventaris'  
        
        tabControlFrame = tk.Frame(self.secondPageScrollableFrame, bg="#2F0160")
        tabControlFrame.pack(fill=tk.X)

        self.tabContentFrame = tk.Frame(self.secondPageScrollableFrame, bg="#2F0160")
        self.tabContentFrame.pack(fill=tk.BOTH, expand=True, pady=(10, 0))

        tabCanvas = tk.Canvas(tabControlFrame, bg="#2F0160", height=100, width=778, highlightthickness=0, bd=0)
        tabCanvas.pack(anchor="w", pady=(20, 10), fill=tk.X)
        
        self.InventarisImage = tk.PhotoImage(file="img/InventarisTab.png")  
        self.LogActivityImage = tk.PhotoImage(file="img/InventarisTab.png") 
        self.backButtonImage = tk.PhotoImage(file="img/xButton.png")  
        
        self.inventarisButton = tk.Button(
            tabCanvas, image=self.InventarisImage, text="Inventaris",  
            font=("Arial", 22, "bold"), bg="#2F0160", fg="white", 
            command=lambda: self.togglesecondPageTab('inventaris'), borderwidth=0,
            highlightthickness=0, relief="flat",  
            compound="center"  
        )
        tabCanvas.create_window(145, 37, window=self.inventarisButton)

        self.logActivityButton = tk.Button(
            tabCanvas, image=self.LogActivityImage, text="Log Aktivitas", 
            font=("Arial", 22, "bold"), bg="#2F0160", fg="#2F0160", 
            command=lambda: self.togglesecondPageTab('logActivity'), borderwidth=0,
            highlightthickness=0, relief="flat",  
            compound="center"  
        )
        
        tabCanvas.create_window(400, 37, window=self.logActivityButton)
        
        self.backButtonImage = tk.PhotoImage(file="img/xButton.png")  
        backButton = tk.Button(
            tabCanvas, image=self.backButtonImage, command=self.goToMainPage,bg="#2F0160",
            borderwidth=0, highlightthickness=0  
        )
        tabCanvas.create_window(735, 15, anchor="ne", window=backButton)
        
        tabCanvas.create_line(0, 65, 778, 65, fill="white", width=2)

        self.showTab(self.showInventoryContent)
        self.updateTabState()

    def updateTabState(self):
        if self.currentActiveTab == 'inventaris':  
            self.inventarisButton.config(image=self.InventarisImage, fg="#2F0160") 
        else:  
            self.inventarisButton.config(image="", fg="white")  
        
        if self.currentActiveTab == 'logActivity':  
            self.logActivityButton.config(image=self.LogActivityImage, fg="#2F0160")  
        else:   
            self.logActivityButton.config(image="", fg="white")  

    def togglesecondPageTab(self, tabName):
        if tabName == 'inventaris':
            self.currentActiveTab = 'inventaris'  
            self.showTab(self.showInventoryContent)  
        elif tabName == 'logActivity':
            self.currentActiveTab = 'logActivity'  
            self.showTab(self.showLogActivityContent)  

        self.updateTabState()


    def showInventoryContent(self):
        """Menampilkan konten tab Inventaris"""
        # Bersihkan tab konten
        for widget in self.tabContentFrame.winfo_children():
            widget.destroy()

        # Tambahkan konten inventaris
        self.bgImage = PhotoImage(file="img/barInventory.png")
        self.quantityImage = PhotoImage(file="img/quantityInventory.png")
        self.distributeButtonImage = PhotoImage(file="img/distributeButton.png")
        self.deleteButton2Image = PhotoImage(file="img/deleteButton2.png")
        
        inventaris = [
            {"location": "JAKARTA", "quantity": 600},
            {"location": "BANDUNG", "quantity": 777},
            {"location": "WAKANDA", "quantity": 888},
            {"location": "IKN", "quantity": 999},
        ]
        
        for inventory in inventaris:
            self.createInventoryRow(inventory)
    
    def createInventoryRow(self, inventory):
        inventoryCanvas = tk.Canvas(self.tabContentFrame, width=678, height=91, bg='#2F0160', highlightthickness=0)
        inventoryCanvas.pack(anchor="w", padx=50, pady=(10, 10), fill="x")  #

        # Menambahkan gambar sebagai background
        inventoryCanvas.create_image(0, 0, anchor="nw", image=self.bgImage)
        inventoryCanvas.image = self.bgImage 
        
        # Menambahkan elemen di atas gambar (menggunakan koordinat)
        nameLabel = tk.Label(self.tabContentFrame, text=inventory["location"], font=("Arial", 20, "bold"), bg="#F7F7F7", fg="black")
        inventoryCanvas.create_window(30, 45, anchor="w", window=nameLabel)  # Label di kiri atas (disesuaikan dengan koordinat)
        
        inventoryCanvas.create_image(315, 22, anchor="nw", image=self.quantityImage)
        inventoryCanvas.image = self.quantityImage 
        
        QuantityLabel = tk.Label(self.tabContentFrame, text=f'{inventory["quantity"]}', font=("Arial", 20, "bold"), bg="#2F0160", fg="white")
        inventoryCanvas.create_window(405, 45, anchor="w", window=QuantityLabel)  # Label di kiri atas (disesuaikan dengan koordinat)
        
        deleteButton2 = tk.Button(
            self.tabContentFrame,
            image=self.deleteButton2Image,
            command=lambda: self.deleteInventory(inventory["location"]),
            bd=0,
            highlightthickness=0,
            bg="#2F0160",
            activebackground="#2F0160"
        )
        inventoryCanvas.create_window(515, 45, anchor="w", window=deleteButton2)
        
        distributeButton = tk.Button(
            self.tabContentFrame,
            image=self.distributeButtonImage,
            command=lambda: self.formDistributeInventory(inventory["location"]),
            bd=0,
            highlightthickness=0,
            bg="#2F0160",
            activebackground="#2F0160"
        )
        inventoryCanvas.create_window(605, 45, anchor="w", window=distributeButton)    
        
        
    def deleteInventory(self, InventoryLocation):
        """Menangani klik tombol Hapus."""        
        print(f"Delete resource {InventoryLocation}")
        # Tambahkan logika untuk menghapus resource di sini
        messagebox.showinfo("Informasi", f"Inventaris di {InventoryLocation} telah dihapus.")
        
    def formDistributeInventory(self, InventoryLocation):
        """Menangani form untuk mengupdate resource."""        
        DistributeWindow = tk.Toplevel(self.root)
        DistributeWindow.title("Distribute Resource To")
        DistributeWindow.config(bg='#2F0160')
        DistributeWindow.geometry("510x265")
        
        inputFieldBG = tk.PhotoImage(file="../img/inputField.png")
        LocationEntry = InventoryLocation

        headerPage = tk.Label(DistributeWindow, 
                          text=f"Distribute Resource from {LocationEntry}", 
                          font=("Arial", 16, "bold"),
                          bg='#2F0160', fg='white')
        headerPage.pack(pady=(10, 2), anchor="w", padx=15)
        
        descPage = tk.Label(DistributeWindow, text="Silakan Distribusi Resource pada lokasi yang ingin dituju beserta quantity nya", font=("Arial", 10), bg='#2F0160', fg='white')
        descPage.pack(pady=(2, 12), anchor="w", padx=15)

        ToLocationFrame = tk.Frame(DistributeWindow, bg='#2F0160')
        ToLocationFrame.pack(anchor="w", padx=15, pady=(5, 5))

        ToLocationLabel = tk.Label(ToLocationFrame, text="Lokasi Tujuan Resource:", bg='#2F0160', fg='white', font=("Arial", 12))
        ToLocationLabel.pack(side="left")

        ToLocationCanvas = tk.Canvas(ToLocationFrame, width=230, height=32, bg='#2F0160', highlightthickness=0)
        ToLocationCanvas.pack(side="left", padx=(10, 0))
        ToLocationCanvas.create_image(0, 0, image=inputFieldBG, anchor="nw")
        
        ToLocationEntry = tk.Entry(ToLocationCanvas, font=("Arial", 12), bg="#ffffff", bd=0, justify="left")
        ToLocationEntry.place(x=10, y=5, width=210, height=22)  
        
        # Alokasi Quantity
        quantityFrame = tk.Frame(DistributeWindow, bg='#2F0160')
        quantityFrame.pack(anchor="w", padx=15, pady=(5, 5))

        quantityLabel = tk.Label(quantityFrame, text="Quantity untuk distribusi:", bg='#2F0160', fg='white', font=("Arial", 12))
        quantityLabel.pack(side="left")

        quantityCanvas = tk.Canvas(quantityFrame, width=233, height=32, bg='#2F0160', highlightthickness=0)
        quantityCanvas.pack(side="left", padx=(10, 0))
        quantityCanvas.create_image(3, 0, image=inputFieldBG, anchor="nw")
        
        quantityEntry = tk.Entry(quantityCanvas, font=("Arial", 12), bg="#ffffff", bd=0, justify="left")
        quantityEntry.place(x=13, y=5, width=210, height=22)  

        submitButton = tk.Button(
            DistributeWindow,
            text="Distribute",
            bg="blue",
            fg="white",
            activebackground="darkblue",
            activeforeground="yellow",
            relief="flat",
            font=("Arial", 12),
            command=lambda: self.distributeInventory(LocationEntry, ToLocationEntry, quantityEntry, DistributeWindow)
        )
        submitButton.pack(anchor="w", padx=(360, 25), pady=(10, 10))
        
        DistributeWindow.inputFieldBG = inputFieldBG
        
    def distributeInventory(self, LocationEntry, ToLocationEntry, quantityEntry, allocateWindow):
        """Mengupdate jumlah resource."""        
        location = LocationEntry.get()
        try:
            Tolocation = ToLocationEntry.get()
            quantity = int(quantityEntry.get())
            message = self.resource_control.allocate_resource(location, Tolocation, quantity)
            messagebox.showinfo("Informasi", message)
        except ValueError:
            messagebox.showerror("Error", "Jumlah harus berupa angka yang valid!")
        allocateWindow.destroy()
        
        
            

    def showLogActivityContent(self):
        """Menampilkan konten tab I"""
        # Bersihkan tab konten
        for widget in self.tabContentFrame.winfo_children():
            widget.destroy()

        # Tambahkan konten inventaris
        self.bgImage = PhotoImage(file="../img/barInventory.png")
        self.InventarisButton2Image = PhotoImage(file="../img/InventarisButton2.png")
        self.reportButtonImage = PhotoImage(file="../img/reportButton.png")
        
        LogActivities = [
            {"report":"Allocate 100 Vibranium to Jakarta"},
            {"report":"Distribute 100 Vibranium to Bandung"},
            {"report": "Deallocate 50 Vibranium from Jakarta"},
        ]
        
        for activity in LogActivities:
            self.createActivityRow(activity)
            
    def createActivityRow(self, activity):
        activityCanvas = tk.Canvas(self.tabContentFrame, width=678, height=91, bg='#2F0160', highlightthickness=0)
        activityCanvas.pack(anchor="w", padx=50, pady=(10, 10), fill="x") 
         
        activityCanvas.create_image(0, 0, anchor="nw", image=self.bgImage)
        activityCanvas.image = self.bgImage
        
        reportLabel = tk.Label(self.tabContentFrame, text=activity["report"], font=("Arial", 18, "bold"), bg="#F7F7F7", fg="black")
        activityCanvas.create_window(30, 45, anchor="w", window=reportLabel) 
        
        inventarisButton = tk.Button(
            self.tabContentFrame,
            image=self.InventarisButton2Image,
            command=lambda: self.delete(activity["report"]),
            bd=0,
            highlightthickness=0,
            bg="#2F0160",
            activebackground="#2F0160"
        )
        activityCanvas.create_window(530, 45, anchor="w", window=inventarisButton)
        
        reportButton = tk.Button(
            self.tabContentFrame,
            image=self.reportButtonImage,
            command=lambda: self.distributeResource(activity["report"]),
            bd=0,
            highlightthickness=0,
            bg="#2F0160",
            activebackground="#2F0160"
        )
        activityCanvas.create_window(600, 45, anchor="w", window=reportButton)
        
        
        
            
    

    def showTab(self, content_function):
        """Membersihkan konten tab sebelumnya dan menampilkan konten baru"""
        # Bersihkan semua konten tab sebelumnya
        for widget in self.tabContentFrame.winfo_children():
            widget.destroy()

        # Tampilkan konten tab baru
        content_function()


    def check_size(self):
        print(f"Width: {self.secondPageScrollableFrame.winfo_width()}")
        print(f"Height: {self.secondPageScrollableFrame.winfo_height()}")
        print(f"Geometry: {self.secondPageScrollableFrame.winfo_geometry()}")


    def goToSecondPage(self):
        self.firstPage.pack_forget()  
        self.setupSecondPage() 
        
    def goToMainPage(self):
        """Kembali ke halaman pertama"""
        self.secondPage.pack_forget()  
        self.firstPage.pack(fill="both", expand=True)  

  
        
