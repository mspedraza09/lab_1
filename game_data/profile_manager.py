from game.persistence.Hash_table.storage_engine import StorageEngine

class SaveProfile:
    def __init__(self):
        self.player = StorageEngine()
    
    def save_profile(self, player_id, data):
        self.player.save("profile", f"profile:{player_id}", data)
    
    def get_profile(self, player_id):
        return self.player.get(f"profile: {player_id}")

    def update_profile(self, player_id, data):
        self.save_profile(player_id, data)