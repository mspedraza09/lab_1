
from game.persistence.Hash_table.storage_engine import StorageEngine

class SaveScore:
    def __init__(self):
        self.store = StorageEngine()
    
    def save_score(self, player_id, score):
        self.store.save("score", f"score:{player_id}:{score}",{"player": player_id, "score": score} )
    
    def get_all_scores(self):
        scores = []

        for key, offset in self.store.hash_table.items():
            if key.startswith("score:"):
                record = self.store.record_store.read_at(offset)
                if record:
                    scores.append(record["data"])

        return scores
    
    def get_all_scores(self):
        scores = []

        for key, offset in self.store.hash_table.items():
            if key.startswith("score:"):
                record = self.store.record_store.read_at(offset)
                if record:
                    scores.append(record["data"])
        return scores
    
    def get_top_scores(self):
        scores = self.get_all_scores()
        scores.sort(key=lambda x: x["score"], reverse=True)
        return scores[:10]


