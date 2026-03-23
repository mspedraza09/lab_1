from game.persistence.Hash_table.storage_engine import StorageEngine

class SettingVolumen:
    def __init__(self):
        self.store = StorageEngine()
    

    def save_setting_volumen(self, volume_level, data):
        self.store.save("Setting", f"settings:global",{"volume": volume_level} )
    
    
    def get_volume(self):
        settings = self.store.get("settings:global")
        
        if settings is None:
            return 0.50 
        return settings.get("volume", 0.50)