import sqlite3

class LogActivity:
    def __init__(self, db_name="SIMADA.db"):
        self.db_name = db_name

    def connect(self):
        """Membuat koneksi ke database."""
        return sqlite3.connect(self.db_name)

    def log_new_activity(self, resource_id: int, activity: str, jumlah: int, locate: bool, lokasi: str = "", tujuan:str = ""):
        """Menambahkan log aktivitas ke database (tambah, kurangi, alokasi, distribusi, dealokasi)."""
        conn = self.connect()
        cur = conn.cursor()
        action_detail = ""

        if activity == "allocate":
            action_detail = f"Alokasi {jumlah} unit ke {lokasi.upper()}" if lokasi else f"Alokasi {jumlah} unit"
        elif activity == "deallocate":
            action_detail = f"Dealokasi {jumlah} unit dari {lokasi.upper()}" if lokasi else f"Dealokasi {jumlah} unit"
        elif activity == "increase":
            action_detail = f"Penambahan {jumlah} unit"
        elif activity == "decrease":
            action_detail = f"Pengurangan {jumlah} unit"
        elif activity == "distribute":
            action_detail = f"Distribusi {jumlah} unit dari {lokasi.upper()} ke {tujuan.upper()}" if lokasi else f"Distribusi {jumlah} unit"
        else:
            action_detail = f"Aktivitas tidak dikenali"

        cur.execute("""
            INSERT INTO LogActivity (resource_id, activity, timestamp)
            VALUES (?, ?, CURRENT_TIMESTAMP)
        """, (resource_id, action_detail))
        
        # Commit perubahan
        conn.commit()
        


    def get_log_activity(self, resource_id: int):
        """Mengambil log aktivitas dari database berdasarkan resource_id."""
        conn = self.connect()
        cur = conn.cursor()
        try:
            cur.execute('''
                SELECT *
                FROM LogActivity
                WHERE resource_id = ?
            ''', (resource_id,))
            logs = cur.fetchall()
            return logs  # Mengembalikan list of tuples [(action_type, timestamp, jumlah, lokasi), ...]
        except sqlite3.Error as e:
            raise RuntimeError(f"Kesalahan saat mengambil log aktivitas: {str(e)}")
        finally:
            conn.close()

    def delete_logs(self, resource_id: int):
        """Menghapus semua log aktivitas untuk resource_id tertentu."""
        conn = self.connect()
        cur = conn.cursor()
        try:
            cur.execute('''
                DELETE FROM log_activity
                WHERE resource_id = ?
            ''', (resource_id,))
            conn.commit()
        except sqlite3.Error as e:
            raise RuntimeError(f"Kesalahan saat menghapus log aktivitas: {str(e)}")
        finally:
            conn.close()
