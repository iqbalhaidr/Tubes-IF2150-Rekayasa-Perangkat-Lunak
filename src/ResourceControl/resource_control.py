from src.ResourceManager.resource_manager import ResourceManager
from src.LogActivity.log_activity import LogActivity
from src.ReportManager.report_manager import ReportManager
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
    
    def get_report_detail_id(self, id : int):
        rm = ReportManager()
        report = rm.get_report_by_id(id)
        if report is None:
            return None
        else:
            detail = report.detail

        return detail
    
    def create_report(self, id_resource ,id_report :int, detail: str):
        if not detail:
            return False #gagal
        return self.report_manager.add_report(id_report, id_resource, detail)
    
    def update_report(self,id_report :int, detail: str):
        if not detail:
            return False #gagal
        return self.report_manager.update_report_by_id(id_report, detail)
    
    def delete_report(self, id):
        return self.report_manager.delete_report_by_id(id)
    
    def check_exist_report(self, id):
        return self.report_manager.check_existing_report(id)
        
