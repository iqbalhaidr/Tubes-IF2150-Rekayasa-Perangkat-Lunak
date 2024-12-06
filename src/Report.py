class Report:
    def __init__(self, report_id: int, report_details: str):
        self.report_id = report_id
        self.report_details = report_details

    def get_report_detail(self):
        return self.report_details

    def set_report_detail(self, new_details: str):
        if not new_details:
            raise ValueError("Detail laporan tidak boleh kosong.")
        self.report_details = new_details
        return f"Detail laporan berhasil diperbarui."

    def confirm_deletion(self):
        return f"Laporan dengan ID '{self.report_id}' akan dihapus. Konfirmasi diperlukan."

    def __str__(self):
        return f"ID Laporan: {self.report_id}\nDetail: {self.report_details}"
