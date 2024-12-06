class Report:
    def __init__(self, report_id: int, resource_id: int, detail: str, created_at: str = None):
        """
        Inisialisasi laporan baru.
        :param report_id: ID laporan (unik).
        :param resource_id: ID sumber daya terkait.
        :param detail: Detail laporan.
        :param created_at: Waktu pembuatan laporan (default: None, akan diambil dari database).
        """
        self.report_id = report_id
        self.resource_id = resource_id
        self.detail = detail
        self.created_at = created_at

    def get_report_detail(self):
        """Mengambil detail laporan."""
        return self.detail

    def set_report_detail(self, new_details: str):
        """Mengubah atau memperbarui detail laporan."""
        if not new_details:
            raise ValueError("Detail laporan tidak boleh kosong.")
        self.detail = new_details
        return f"Detail laporan berhasil diperbarui."

    def __str__(self):
        """Representasi string dari laporan."""
        return f"ID Laporan: {self.report_id}, Resource ID: {self.resource_id}, Detail: {self.detail}, Created At: {self.created_at}"
