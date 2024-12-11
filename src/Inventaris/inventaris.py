import sqlite3

class Inventaris:
    def __init__(self, db_name="SIMADA.db"):
        self.db_name = db_name

    def connect(self):
        """Membuat koneksi ke database."""
        return sqlite3.connect(self.db_name)

    def allocate(self, resource_id: int, quantity: int, location: str):
        """Mengalokasikan sumber daya ke lokasi tertentu."""
        conn = self.connect()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO Inventaris (resource_id, location, quantity)
            VALUES (?, ?, ?)
        """, (resource_id, location.upper(), quantity))
        print(location.upper())
        print(quantity)
        print(resource_id)
        conn.commit()
        conn.close()
        return True
        

    def deallocate(self, inventaris_id:int, quantity:int):
        print(f"quantity; {quantity}")
        """Menghapus alokasi sumber daya dari lokasi tertentu."""        
        conn = self.connect()
        cur = conn.cursor()
        cur.execute('''
            SELECT resource_id, quantity FROM Inventaris
            WHERE inventaris_id = ?
        ''', (inventaris_id, ))
        resource_id, location_quantity = cur.fetchone()

        cur.execute('''
            SELECT quantity FROM Resources
            WHERE id = ? 
        ''', (resource_id,))
        resource_qty = cur.fetchone()
        print(resource_qty[0])

        #state 0 gagal
        #state 1 Berhasil dan tidak nol
        #state 2 Berhasil dan 0

        state =0 
        # Kurangi jumlah di lokasi
        new_quantity_loc = location_quantity - quantity
        if new_quantity_loc>=0:
            new_quantity_resource = resource_qty[0] + quantity
            cur.execute('''
                UPDATE inventaris
                SET quantity = ?
                WHERE inventaris_id = ?
            ''', (new_quantity_loc, inventaris_id))
            conn.commit()  

            cur.execute('''
                UPDATE Resources
                SET quantity = ?
                WHERE id = ?
            ''', (new_quantity_resource, resource_id))
            conn.commit()  
            conn.close()
            state = 1 if new_quantity_loc > 0 else 2
            print("gett")
            return state
        else:
            conn.close()
            return 0


    def delete_location_zero_loc_qty (self, inventaris_id: int):
        conn = self.connect()
        cur = conn.cursor()
        cur.execute('''
            DELETE FROM Inventaris
            WHERE inventaris_id = ?
        ''', (inventaris_id,))
        conn.commit()
        conn.close()
        return True

              

    def distribute_to(self, inventaris_id: int, location: str, quantity:int):
        """Mendistribusikan sumber daya dari satu lokasi ke lokasi lain."""
        conn = self.connect()
        cur = conn.cursor()
        cur.execute('''
            SELECT resource_id, quantity FROM Inventaris
            WHERE inventaris_id = ?
        ''', (inventaris_id, ))
        resource_id, location_quantity = cur.fetchone()

        cur.execute('''
            SELECT quantity, inventaris_id FROM Inventaris
            WHERE resource_id = ? AND location = ? 
        ''', (resource_id, location.upper() ))
        id_distributed_loc ,quantity_of_distributed_loc = cur.fetchone()
        new_qty_in_distributed_loc = quantity_of_distributed_loc + quantity
        new_loc_qty = location_quantity - quantity
        if new_loc_qty >= 0:
            cur.execute('''
                UPDATE inventaris
                SET quantity = ?
                WHERE inventaris_id = ?
            ''', (new_loc_qty, inventaris_id))
            conn.commit()

            cur.execute('''
                UPDATE inventaris
                SET quantity = ?
                WHERE inventaris_id = ?
            ''', (new_qty_in_distributed_loc, id_distributed_loc))
            conn.commit()
            conn.close()
            state = 1 if new_loc_qty > 0 else 2
            return state
          




    def get_all_allocation_by_id(self, resource_id: int):
        """Mengambil semua alokasi untuk sumber daya tertentu."""
        conn = self.connect()
        cur = conn.cursor()
        cur.execute('''
            SELECT * FROM Inventaris
            WHERE resource_id = ?
        ''', (resource_id,  ))
        all_location = cur.fetchall()

        conn.close()
        return all_location ## formatnya inventaris_id, loc, qty
        
        
