class LogActivity:
    def __init__(self):
        self.log_entries = []

    def log_new_activity(self, resource_name: str, action_type: str, timestamp: str, jumlah: int, lokasi: str):
        if jumlah <= 0:
            raise ValueError("Jumlah harus lebih besar dari nol.")
        
        log_entry = {
            "resource_name": resource_name,
            "action_type": action_type,
            "timestamp": timestamp,
            "jumlah": jumlah,
            "lokasi": lokasi
        }
        self.log_entries.append(log_entry)
        return f"Log aktivitas untuk '{resource_name}' berhasil ditambahkan."

    def get_log_activity(self, resource_name: str):
        filtered_logs = [log for log in self.log_entries if log["resource_name"] == resource_name]
        return filtered_logs if filtered_logs else f"Tidak ada log untuk '{resource_name}'."
