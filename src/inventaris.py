import sqlite3

class Inventaris:
    def __init__(self, db_name="SIMADA.db"):
        self.db_name = db_name

    def connect(self):
        return sqlite3.connect(self.db_name)

    def add_resource_to_location(self, resource_name: str, location: str, quantity: int):
        if quantity <= 0:
            raise ValueError("Jumlah harus lebih besar dari nol.")
        
        conn = self.connect()
        cur = conn.cursor()
        try:
            cur.execute("""
                INSERT INTO inventaris (resource_id, location, quantity)
                VALUES ((SELECT resource_id FROM resources WHERE name = ?), ?, ?)
            """, (resource_name, location, quantity))
            conn.commit()
            return f"Sumber daya '{resource_name}' berhasil ditambahkan ke lokasi '{location}' dengan jumlah {quantity}."
        finally:
            conn.close()
