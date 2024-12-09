import sqlite3
from src.Report.Report import Report
class ReportManager:
    def __init__(self, db_name="SIMADA.db"):
        self.db_name = db_name

    def connect(self):
        """Membuat koneksi ke database."""
        return sqlite3.connect(self.db_name)

    def add_report(self, log_id,resource_id: int, detail: str):
        """Menambahkan laporan baru ke database."""
        if not detail:
            raise ValueError("Detail laporan tidak boleh kosong.")
        
        conn = self.connect()
        cur = conn.cursor()
        if not (self.check_existing_report(log_id)):
            try:
                cur.execute('''
                    INSERT INTO Report (report_id ,resource_id, detail)
                    VALUES (?, ?, ?)
                ''', (log_id, resource_id, detail))
                conn.commit()
                return True #berhasil 
            finally:
                conn.close()
        else:
            return False

    def get_report_by_id(self, report_id: int):
        """Mengambil laporan berdasarkan ID."""
        conn = self.connect()
        cur = conn.cursor()

        cur.execute('''
            SELECT report_id, resource_id, detail
            FROM Report
            WHERE report_id = ?
        ''', (report_id,))
        report = cur.fetchone()
        print(report)
        conn.close()
        if report:
            return Report(report[0],report[1],report[2])  # Mengembalikan instance Report
        else:
            return None
        

    def update_report_by_id(self, report_id: int, new_detail: str):
        """Memperbarui detail laporan tertentu berdasarkan ID."""
        conn = self.connect()
        cur = conn.cursor()
        if (self.check_existing_report(report_id)):
            cur.execute('''
                UPDATE Report
                SET detail = ?
                WHERE report_id = ?
            ''', (new_detail, report_id))
            conn.commit()
            conn.close()
            return True
        else:
            conn.close()
            return False

    def delete_report_by_id(self, report_id: int):
        """Menghapus laporan berdasarkan ID."""
        conn = self.connect()
        cur = conn.cursor()
        cur.execute('''
            DELETE FROM Report
            WHERE report_id = ?
        ''', (report_id,))
        conn.commit()
        return True
        

    def get_all_reports(self):
        """Mengambil semua laporan dari database."""
        conn = self.connect()
        cur = conn.cursor()
        try:
            cur.execute('''
                SELECT report_id, resource_id, detail, created_at
                FROM Report
            ''')
            reports = cur.fetchall()
            return [Report(*report) for report in reports]  # Mengembalikan list instance Report
        except sqlite3.Error as e:
            raise RuntimeError(f"Kesalahan saat mengambil semua laporan: {str(e)}")
        finally:
            conn.close()

    def check_existing_report(self, report_id: int):
        """Memeriksa apakah ada sumber daya dengan nama yang sama"""
        conn = self.connect()
        cur = conn.cursor()
        
        cur.execute("SELECT * FROM Report WHERE report_id = ?", (report_id,))
        existing_resource = cur.fetchall()  
        
        conn.close()
        
        return (len(existing_resource)>0)
