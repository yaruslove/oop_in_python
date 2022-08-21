class Player:
    def __init__ (self,name, old, score):
        self.name=str(name).strip()
        self.old=int(old)
        self.score=int(score)
    def __bool__ (self):
        return self.score>0
    def __repr__ (self):
        return f"cls.Player {self.name}"
    
lst_in= """Балакирев; 34; 2048
        "Mediel; 27; 0
        "Влад; 18; 9012
        "Nina P; 33; 0"""

players=[Player(*map(str, x.split("; "))) for x in lst_in.splitlines()]
players_filtered=list(filter(bool, players))
