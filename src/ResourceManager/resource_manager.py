import sqlite3

class ResourceManager:
    def __init__(self, db_name):
        self.db_name = "SIMADA.db"

    def connect(self):
        return sqlite3.connect(self.db_name)

    def check_existing_resource(self, resource_id: int):
        """Memeriksa apakah ada sumber daya dengan nama yang sama"""
        conn = self.connect()
        cur = conn.cursor()
        
        cur.execute("SELECT * FROM Resources WHERE id = ?", (resource_id,))
        existing_resource = cur.fetchall()  
        
        conn.close()
        
        return (len(existing_resource)>0)
    
    def create_resource(self, name:str, quantity:int):
        '''Menambahkan jenis resource baru yang di inginkan oleh user'''
        conn = self.connect()
        cur = conn.cursor()

        if not (self.check_existing_resource(name)):
            cur.execute("""
            INSERT INTO Resources (name, quantity)
            VALUES (?, ?)
            """, (name, quantity))
            conn.commit()  # simpan ke database
            conn.close()
            return True #berhasil ditambahkan
        else :
            conn.close()
            return False  # Jika nama sudah ada (duplicate entry)
        
    def delete_resource(self, name:str):
        '''Menghapus resource yang diinginkan'''
        conn = self.connect()
        cur = conn.cursor()
        cur.execute("DELETE FROM Resources WHERE name = ?", (name,))
        conn.commit()

        conn.close()

    def add_or_subtract_resource_quantity(self, name, quantity, add: bool):
        '''Menambahkan jumah quantity yang diinginkan pada resource'''
        conn = self.connect()
        cur = conn.cursor()

        cur.execute("SELECT * FROM Resources WHERE name = ?", (name,))
        existing_resource = cur.fetchone()

        current_quantity = existing_resource[2]  
        new_quantity=0
        if (add):
            new_quantity = current_quantity + quantity
        else:
            new_quantity = current_quantity - quantity

        cur.execute("UPDATE Resources SET quantity = ? WHERE name = ?", (new_quantity, name))
        conn.commit() 

        conn.close()

    def get_resource_quantity(self, id):
        '''Mendapatkan quantity dari resource yang dipilih user'''
        conn = self.connect()
        cur = conn.cursor()

        cur.execute("SELECT quantity FROM Resources WHERE id = ?", (id,))
        resource_quantity = cur.fetchone()

        conn.close()

        return resource_quantity
    
    def get_all_resource(self):
        '''Mendapatkan seluruh informasi yang ada dalam table resource'''
        cur.execute("SELECT * FROM Resources")
        list_of_resource = cur.fetchall()
        conn = self.connect()
        cur = conn.cursor()
        conn.close()  
        
        return list_of_resource
