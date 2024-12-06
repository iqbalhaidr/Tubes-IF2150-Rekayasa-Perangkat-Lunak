import sqlite3

class ReportManager:
    def __init__(self, db_name="SIMADA.db"):
        self.db_name = db_name

    def connect(self):
        return sqlite3.connect(self.db_name)

    def add_report(self, report_id: int, report_details: str):
        conn = self.connect()
        cur = conn.cursor()
        try:
            cur.execute(
                "INSERT INTO reports (report_id, details) VALUES (?, ?)",
                (report_id, report_details)
            )
            conn.commit()
            return f"Laporan dengan ID '{report_id}' berhasil ditambahkan."
        finally:
            conn.close()

    def get_report_by_id(self, report_id: int):
        conn = self.connect()
        cur = conn.cursor()
        try:
            cur.execute("SELECT details FROM reports WHERE report_id = ?", (report_id,))
            report = cur.fetchone()
            return f"Detail laporan: {report[0]}" if report else "Laporan tidak ditemukan."
        finally:
            conn.close()
