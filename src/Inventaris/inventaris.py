import sqlite3

class Inventaris:
    def __init__(self, db_name="SIMADA.db"):
        self.db_name = db_name

    def connect(self):
        """Membuat koneksi ke database."""
        return sqlite3.connect(self.db_name)

    def allocate(self, location: str, quantity: int, resource_id: int):
        """Mengalokasikan sumber daya ke lokasi tertentu."""
        conn = self.connect()
        cur = conn.cursor()
        try:
            # Cek apakah alokasi untuk resource_id dan lokasi sudah ada
            cur.execute('''
                SELECT inventaris_id, quantity FROM inventaris
                WHERE resource_id = ? AND location = ?
            ''', (resource_id, location))
            result = cur.fetchone()

            if result:
                # Jika data sudah ada, perbarui quantity
                inventaris_id, existing_quantity = result
                new_quantity = existing_quantity + quantity
                cur.execute('''
                    UPDATE inventaris
                    SET quantity = ?
                    WHERE inventaris_id = ?
                ''', (new_quantity, inventaris_id))
            else:
                # Jika data belum ada, insert data baru
                cur.execute('''
                    INSERT INTO inventaris (resource_id, location, quantity)
                    VALUES (?, ?, ?)
                ''', (resource_id, location, quantity))
            conn.commit()
        except sqlite3.Error as e:
            raise RuntimeError(f"Kesalahan saat mengalokasikan sumber daya: {str(e)}")
        finally:
            conn.close()

    def deallocate(self, location: str, quantity: int, resource_id: int):
        """Menghapus alokasi sumber daya dari lokasi tertentu."""
        if quantity <= 0:
            raise ValueError("Jumlah harus lebih besar dari nol.")
        
        conn = self.connect()
        cur = conn.cursor()
        try:
            # Cek jumlah yang ada di lokasi
            cur.execute('''
                SELECT inventaris_id, quantity FROM inventaris
                WHERE resource_id = ? AND location = ?
            ''', (resource_id, location))
            result = cur.fetchone()

            if result:
                inventaris_id, existing_quantity = result
                if existing_quantity >= quantity:
                    # Kurangi jumlah di lokasi
                    new_quantity = existing_quantity - quantity
                    cur.execute('''
                        UPDATE inventaris
                        SET quantity = ?
                        WHERE inventaris_id = ?
                    ''', (new_quantity, inventaris_id))
                else:
                    raise ValueError(f"Jumlah di lokasi {location} tidak mencukupi untuk deallocation.")
            else:
                raise ValueError(f"Tidak ada alokasi untuk resource_id {resource_id} di lokasi {location}.")
            conn.commit()
        except sqlite3.Error as e:
            raise RuntimeError(f"Kesalahan saat menghapus alokasi sumber daya: {str(e)}")
        finally:
            conn.close()

    def distribute_to(self, source_location: str, target_location: str, quantity: int, resource_id: int):
        """Mendistribusikan sumber daya dari satu lokasi ke lokasi lain."""
        if quantity <= 0:
            raise ValueError("Jumlah harus lebih besar dari nol.")
        
        conn = self.connect()
        try:
            # Deallocate dari lokasi asal
            self.deallocate(source_location, quantity, resource_id)

            # Allocate ke lokasi tujuan
            self.allocate(target_location, quantity, resource_id)
        except (ValueError, RuntimeError) as e:
            raise RuntimeError(f"Kesalahan saat mendistribusikan sumber daya: {str(e)}")
        finally:
            conn.close()

    def get_allocation(self, resource_id: int):
        """Mengambil semua alokasi untuk sumber daya tertentu."""
        conn = self.connect()
        cur = conn.cursor()
        try:
            cur.execute('''
                SELECT location, quantity FROM inventaris
                WHERE resource_id = ?
            ''', (resource_id,))
            results = cur.fetchall()
            return results  # Mengembalikan list Python tanpa formatting
        except sqlite3.Error as e:
            raise RuntimeError(f"Kesalahan saat mengambil data alokasi: {str(e)}")
        finally:
            conn.close()
