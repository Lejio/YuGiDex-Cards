from dexConnector import YuGiDexDB
from urllib import request


if __name__ == "__main__":

    db_name = "yugidbEN.db"
    
    r = request.urlretrieve(f"https://geneni.info/yugidexdb/{db_name}", db_name)
    db = YuGiDexDB(db_name)
    print(db.search('name', 'Pot of Greed'))