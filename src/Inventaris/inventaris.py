import sqlite3
from LogActivity.log_activity import LogActivity

class Inventaris:
    def __init__(self, db_name="SIMADA.db"):
        self.db_name = db_name

    def connect(self):
        """Membuat koneksi ke database."""
        return sqlite3.connect(self.db_name)

    def allocate(self, resource_id: int, quantity: int, location: str, isExist: bool):
        """Mengalokasikan sumber daya ke lokasi tertentu."""
        conn = self.connect()
        cur = conn.cursor()
        if (isExist):
            cur.execute('''
                UPDATE inventaris
                SET quantity = ?
                WHERE resource_id = ? AND location = ?
            ''', (quantity, resource_id, location))
            conn.commit()
        else:
            cur.execute("""
                INSERT INTO Inventaris (resource_id, location, quantity)
                VALUES (?, ?, ?)
            """, (resource_id, location.upper(), quantity))
            conn.commit()
        print(location.upper())
        print(quantity)
        print(resource_id)
        conn.close()
        return 2
        

    def deallocate(self, resource_id: int, inventaris_id:int, new_quantity_loc: int, new_quantity_resource: int):
        """Menghapus alokasi sumber daya dari lokasi tertentu."""        
        conn = self.connect()
        cur = conn.cursor()
        
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
    
            

    def delete_location_zero_loc_qty (self, inventaris_id: int):
        conn = self.connect()
        cur = conn.cursor()
        cur.execute('''
            DELETE FROM Inventaris
            WHERE inventaris_id = ?
        ''', (inventaris_id,))
        conn.commit()
        conn.close()
        return 999

              

    def distribute_to(self, inventaris_id: int, location: str, quantity:int):
        """Mendistribusikan sumber daya dari satu lokasi ke lokasi lain."""
        conn = self.connect()
        cur = conn.cursor()
        cur.execute('''
            SELECT resource_id, location ,quantity FROM Inventaris
            WHERE inventaris_id = ?
        ''', (inventaris_id, ))
        resource_id, source_location ,location_quantity = cur.fetchone()

        cur.execute('''
            SELECT quantity, inventaris_id FROM Inventaris
            WHERE resource_id = ? AND location = ? 
        ''', (resource_id, location.upper() ))
        quantity_of_distributed_loc , id_distributed_loc = cur.fetchone()
        if (id_distributed_loc == inventaris_id):
            return 0
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
            log = LogActivity()
            log.log_new_activity(resource_id, "distribute", quantity, True, source_location, location)
            state = 1 if new_loc_qty > 0 else 2

            return state
        else:
            return 0
        
    def distribute_to(self, inventaris_id: int, id_distributed_loc: int, new_loc_qty: str,  new_qty_in_distributed_loc:int):
        """Mendistribusikan sumber daya dari satu lokasi ke lokasi lain."""
        conn = self.connect()
        cur = conn.cursor()
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
          




    def get_all_allocation_by_id(self, resource_id: int):
        """Mengambil semua alokasi untuk sumber daya tertentu."""
        print(f"r = {resource_id}")
        conn = self.connect()
        cur = conn.cursor()
        cur.execute('''
            SELECT * FROM Inventaris
            WHERE resource_id = ?
        ''', (resource_id,  ))
        all_location = cur.fetchall()

        conn.close()
        return all_location ## formatnya inventaris_id, loc, qty
        
        
