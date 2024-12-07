from ResourceManager import ResourceManager
from LogActivity import LogActivity
from ReportManager import ReportManager
#please check
class ResourceControl:
    def __init__(self, db_name="SIMADA.db"):
        self.resource_manager = ResourceManager(db_name)
        self.log_activity = LogActivity()
        self.report_manager = ReportManager(db_name)

    def add_resource(self, resource_name: str, resource_quantity: int, resource_location: str):
        """Menambahkan sumber daya baru."""
        if resource_quantity <= 0:
            raise ValueError("Quantity harus lebih besar dari nol.")
        
        success = self.resource_manager.create_resource(resource_name, resource_quantity)
        if success:
            self.log_activity.log_new_activity(resource_name, "Penambahan", "Now", resource_quantity, resource_location)
            return f"Sumber daya '{resource_name}' berhasil ditambahkan dengan jumlah {resource_quantity}."
        else:
            return f"Gagal menambahkan sumber daya '{resource_name}', mungkin sudah ada."

    def update_resource_quantity(self, resource_id: int, new_quantity: int):
        """Memperbarui jumlah sumber daya."""
        if new_quantity <= 0:
            raise ValueError("Quantity baru harus lebih besar dari nol.")
        
        existing_quantity = self.resource_manager.get_resource_quantity(resource_id)
        if existing_quantity is None:
            return f"Sumber daya '{resource_id}' tidak ditemukan."
        
        difference = new_quantity - existing_quantity[0]
        add = difference > 0
        self.resource_manager.add_or_subtract_resource_quantity(resource_id, abs(difference), add)
        self.log_activity.log_new_activity(resource_id, "Update", "Now", abs(difference), "N/A")
        return f"Jumlah sumber daya '{resource_id}' berhasil diperbarui ke {new_quantity}."

    def make_report(resource_id: int, reportDetails: String):
        """Menambahkan report baru untuk resource jika belum ada report"""
        isIDValid = self.resource_manager.check_existing_resource(resource_id)
        isExistReport = self.report_manager.check_existing_report(resource_id)

        if not isIDValid:
            return f"Resource ID {resource_id} tidak dapat ditemukan."
        
        if isExistReport:
            return f"Tidak dapat membuat report karena Resource ID {resource_id} sudah memiliki report, silahkan untuk mengupdate informasi jika diperlukan."
        
        self.report_manager.add_report(resource_id, reportDetails)
        return f"Report untuk Resource ID {resource_id} berhasil ditambahkan kedalam database."
