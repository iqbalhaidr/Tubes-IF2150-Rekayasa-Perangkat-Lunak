import sqlite3

class LogActivity:
    def __init__(self, db_name="SIMADA.db"):
        self.db_name = db_name

    def connect(self):
        """Membuat koneksi ke database."""
        return sqlite3.connect(self.db_name)

    def log_new_activity(self, resource_id: int, action_type: str, timestamp: str, jumlah: int, lokasi: str, locate:bool):
        """Menambahkan log aktivitas ke database."""
        if jumlah <= 0:
            raise ValueError("Jumlah harus lebih besar dari nol.")
        
        conn = self.connect()
        cur = conn.cursor()
        action_detail=""
        if locate:
            action_detail= action_type + " " + f"{jumlah}" + " to " + lokasi
        else:
            action_detail= action_type + " " + "Jumlah" + " Sumber Daya"

        try:
            cur.execute('''
                INSERT INTO log_activity (resource_id, activity, timestamp)
                VALUES (?, ?, ?, ?, ?)
            ''', (resource_id, action_detail, timestamp))
            conn.commit()
        except sqlite3.Error as e:
            raise RuntimeError(f"Kesalahan saat menambahkan log aktivitas: {str(e)}")
        finally:
            conn.close()

    def get_log_activity(self, resource_id: int):
        """Mengambil log aktivitas dari database berdasarkan resource_id."""
        conn = self.connect()
        cur = conn.cursor()
        try:
            cur.execute('''
                SELECT action_type, timestamp, jumlah, lokasi
                FROM log_activity
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
