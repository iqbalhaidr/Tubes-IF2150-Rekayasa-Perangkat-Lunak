from ResourceManager.resource_manager import ResourceManager
from LogActivity.log_activity import LogActivity
from ReportManager.report_manager import ReportManager
from Inventaris.inventaris import Inventaris
#please check
class ResourceControl:
    def __init__(self, db_name="SIMADA.db"):
        self.resource_manager = ResourceManager(db_name)
        self.log_activity = LogActivity()
        self.report_manager = ReportManager(db_name)
        self.inventory = Inventaris(db_name)

    def create_new_resource(self, resource_name: str, resource_quantity: int):
        return self.resource_manager.create_resource(resource_name, resource_quantity)

    def update_resource_quantity(self, resource_id: int, new_quantity: int, add: bool):
        """Memperbarui jumlah sumber daya."""
        if new_quantity <= 0:
            return False
        
        conn = self.connect()
        cur = conn.cursor()

        cur.execute("SELECT * FROM Resources WHERE id = ?", (resource_id,))
        resource=  cur.fetchone()
        name_resource = resource[1]
        return self.resource_manager.add_or_subtract_resource_quantity(name_resource, new_quantity, add)
    
    def delete_available_resource(self ,id:int):
        return self.resource_manager.delete_resource(id)
    
    def allocate(self, resource_id, quantity, location):
        '''Mengalokasikan sejumlah sumberdaya ke suatu tempat'''
        return self.resource_manager.allocate(resource_id, quantity, location)

    def deallocate(self,inventaris_id, quantity):
        '''Melakukan dealokasi terhadap sumberdaya di tempat tertentu'''
        if (quantity<0):
            return 0
        return self.inventory.deallocate(inventaris_id, quantity)

    def distribute_to(self, inventaris_id, location, quantity):
        '''Melakukan distribusi sumber daya dari satu tempat ke tempat lain'''
        if (quantity<0):
            return 0
        return self.inventory.deallocate( inventaris_id, location, quantity)

    def delete_location(self, inventaris_id):
        return self.inventory.delete_location_zero_loc_qty(inventaris_id)


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
        
