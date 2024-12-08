import sqlite3
from Report import Report
class ReportManager:
    def __init__(self, db_name="SIMADA.db"):
        self.db_name = db_name

    def connect(self):
        """Membuat koneksi ke database."""
        return sqlite3.connect(self.db_name)

    def add_report(self, resource_id: int, detail: str):
        """Menambahkan laporan baru ke database."""
        if not detail:
            raise ValueError("Detail laporan tidak boleh kosong.")
        
        conn = self.connect()
        cur = conn.cursor()
        try:
            cur.execute('''
                INSERT INTO reports (resource_id, detail)
                VALUES (?, ?)
            ''', (resource_id, detail))
            conn.commit()
            return f"Laporan untuk resource_id '{resource_id}' berhasil ditambahkan."
        except sqlite3.Error as e:
            raise RuntimeError(f"Kesalahan saat menambahkan laporan: {str(e)}")
        finally:
            conn.close()

    def get_report_by_id(self, report_id: int):
        """Mengambil laporan berdasarkan ID."""
        conn = self.connect()
        cur = conn.cursor()
        try:
            cur.execute('''
                SELECT report_id, resource_id, detail, created_at
                FROM reports
                WHERE report_id = ?
            ''', (report_id,))
            report = cur.fetchone()
            if report:
                return Report(*report)  # Mengembalikan instance Report
            else:
                return f"Tidak ada laporan dengan ID '{report_id}'."
        except sqlite3.Error as e:
            raise RuntimeError(f"Kesalahan saat mengambil laporan: {str(e)}")
        finally:
            conn.close()

    def update_report_by_id(self, report_id: int, new_detail: str):
        """Memperbarui detail laporan tertentu berdasarkan ID."""
        if not new_detail:
            raise ValueError("Detail laporan tidak boleh kosong.")
        
        conn = self.connect()
        cur = conn.cursor()
        try:
            cur.execute('''
                UPDATE reports
                SET detail = ?
                WHERE report_id = ?
            ''', (new_detail, report_id))
            conn.commit()
            if cur.rowcount > 0:
                return f"Laporan dengan ID '{report_id}' berhasil diperbarui."
            else:
                return f"Tidak ada laporan dengan ID '{report_id}' untuk diperbarui."
        except sqlite3.Error as e:
            raise RuntimeError(f"Kesalahan saat memperbarui laporan: {str(e)}")
        finally:
            conn.close()

    def delete_report_by_id(self, report_id: int):
        """Menghapus laporan berdasarkan ID."""
        conn = self.connect()
        cur = conn.cursor()
        try:
            cur.execute('''
                DELETE FROM reports
                WHERE report_id = ?
            ''', (report_id,))
            conn.commit()
            if cur.rowcount > 0:
                return f"Laporan dengan ID '{report_id}' berhasil dihapus."
            else:
                return f"Tidak ada laporan dengan ID '{report_id}' untuk dihapus."
        except sqlite3.Error as e:
            raise RuntimeError(f"Kesalahan saat menghapus laporan: {str(e)}")
        finally:
            conn.close()

    def get_all_reports(self):
        """Mengambil semua laporan dari database."""
        conn = self.connect()
        cur = conn.cursor()
        try:
            cur.execute('''
                SELECT report_id, resource_id, detail, created_at
                FROM reports
            ''')
            reports = cur.fetchall()
            return [Report(*report) for report in reports]  # Mengembalikan list instance Report
        except sqlite3.Error as e:
            raise RuntimeError(f"Kesalahan saat mengambil semua laporan: {str(e)}")
        finally:
            conn.close()

    def check_existing_report(self, resource_id: int):
        """ Mengecek apakah Resource sudah memiliki Report."""
        conn = self.connect()
        cur = conn.cursor()
        cur.execute('''
            SELECT report_id, resource_id, detail, created_at
            FROM reports
            WHERE resource_id = ?
        ''', (resource_id,))
        report = cur.fetchall()
        conn.close()

        return len(report) > 0
