from ResourceManager.resource_manager import ResourceManager
from LogActivity.log_activity import LogActivity
from ReportManager.report_manager import ReportManager
from Inventaris.inventaris import Inventaris


class ResourceControl:
    def __init__(self, db_name="SIMADA.db"):
        self.resource_manager = ResourceManager(db_name)
        self.log_activity = LogActivity()
        self.report_manager = ReportManager(db_name)
        self.inventory = Inventaris(db_name)

    def create_new_resource(self, resource_name: str, resource_quantity: int):
        if (resource_quantity <= 0):
            return 0
        return self.resource_manager.create_resource(resource_name, resource_quantity)
    
    def get_all_resource_information(self):
        return self.resource_manager.get_all_resource()

    def update_resource_quantity(self, resource_id: int, new_quantity: int, add: bool):
        """Memperbarui jumlah sumber daya."""
        if (new_quantity < 0):
            return 0
        return self.resource_manager.add_or_subtract_resource_quantity(resource_id, new_quantity, add)
    
    def delete_available_resource(self ,id:int):
        return self.resource_manager.delete_resource(id)
    
    def allocate(self, resource_id, quantity, location):
        '''Mengalokasikan sejumlah sumberdaya ke suatu tempat'''
        if (quantity <= 0):
            return 0
        return self.resource_manager.allocate(resource_id, quantity, location)

    def deallocate(self,inventaris_id, quantity, isDelete):
        '''Melakukan dealokasi terhadap sumberdaya di tempat tertentu'''
        if (quantity < 0):
            return 0
        return self.resource_manager.deallocate_manager(inventaris_id, quantity, isDelete)

    def distribute_to(self, inventaris_id, location, quantity, isDelete):
        '''Melakukan distribusi sumber daya dari satu tempat ke tempat lain'''
        if (quantity < 0):
            return 0
        return self.resource_manager.distribute_manager(inventaris_id , location , quantity, isDelete)

    def delete_location(self, inventaris_id):
        return self.resource_manager.delete_location(inventaris_id)

    def get_all_inventaris(self, resource_id):
        return self.resource_manager.get_all_inventaris_manager(resource_id)
    
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
    
    def get_detail_allocation_loc (self, resource_id):
        return self.inventory.get_all_allocation_by_id(resource_id)
        
    def get_all_log_for_resource(self, resource_id):
        return self.log_activity.get_log_activity(resource_id)