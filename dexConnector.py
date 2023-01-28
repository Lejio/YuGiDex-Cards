import sqlite3
from Card import Card

class YuGiDexDB:

    def __init__(self, db_path):

        self._con = sqlite3.connect(db_path)
        self._cur = self._con.cursor()
        self.currCard = {}

    def search(self, col:str, word: str):

        self._cur
        self.r = self._cur.execute(f"SELECT * FROM card WHERE {col} LIKE '%{word}%'").fetchall()
        names = []

        for i in range(len(self.r)):
            names.append(self.r[i][2])

        return names
        

    def close(self):
        self._con.close()



        