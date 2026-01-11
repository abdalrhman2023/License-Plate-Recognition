from difflib import SequenceMatcher

class WatchlistManager:
    def __init__(self, db, th):
        self.db = db
        self.th = th

    def check(self, plate):
        for p, r in self.db.get_watchlist():
            sim = SequenceMatcher(None, plate, p).ratio()
            if sim >= self.th:
                return {"plate": p, "reason": r, "similarity": sim}
        return None
