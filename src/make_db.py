import sqlite3


def create_tables():
    con = sqlite3.connect("SIMADA.db")
    cur = con.cursor()

    # Tabel Resources
    cur.execute("""
    CREATE TABLE IF NOT EXISTS Resources (
        id INTEGER PRIMARY KEY AUTOINCREMENT,   
        name TEXT NOT NULL,
        quantity INTEGER NOT NULL,
        total_quantity INTEGER NOT NULL
    )
    """)

    #Tabel Inventaris
    cur.execute("""
    CREATE TABLE IF NOT EXISTS Inventaris (
        inventaris_id INTEGER PRIMARY KEY AUTOINCREMENT,
        resource_id INTEGER,
        location TEXT NOT NULL,
        quantity INTEGER NOT NULL,
        FOREIGN KEY (resource_id) REFERENCES Resources(id) ON DELETE CASCADE
    )
    """)

    #Tabel Report
    cur.execute("""
    CREATE TABLE IF NOT EXISTS Report (
        report_id INTEGER PRIMARY KEY,
        resource_id INTEGER,
        detail TEXT NOT NULL,
        FOREIGN KEY (resource_id) REFERENCES Resources(id) ON DELETE CASCADE,
        FOREIGN KEY (report_id) REFERENCES LogActivity(id) ON DELETE CASCADE
    )
    """)

    #Tabel LogActivity
    cur.execute("""
    CREATE TABLE IF NOT EXISTS LogActivity (
        log_id INTEGER PRIMARY KEY AUTOINCREMENT,
        resource_id INTEGER,
        activity TEXT NOT NULL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (resource_id) REFERENCES Resources(id) ON DELETE CASCADE
    )
    """)


    con.commit()
    con.close()

def delete_all_tables():
    # Koneksi ke database
    con = sqlite3.connect("SIMADA.db")
    cur = con.cursor()

    # Daftar nama tabel yang akan dihapus
    tables = ['Resources', 'Inventaris', 'Report', 'LogActivity']

    # Loop untuk menghapus tabel satu per satu
    for table in tables:
        cur.execute(f"DROP TABLE IF EXISTS {table}")
        print(f"Tabel {table} telah dihapus.")
    
    # Commit perubahan dan menutup koneksi
    con.commit()
    con.close()

delete_all_tables()
create_tables()

    