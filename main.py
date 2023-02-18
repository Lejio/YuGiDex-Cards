# from dexConnector import YuGiDexDB
from lang.Types import Type
from lang.lang import Lang

from urllib import request


if __name__ == "__main__":

    # db_name = "yugidbEN.db"
    
    # r = request.urlretrieve(f"https://geneni.info/yugidexdb/{db_name}", db_name)
    # db = YuGiDexDB(db_name)
    # print(db.search('name', 'Blue-Eyes'))
    A = Type(Lang.ITALIAN)
    
    print(A.ATTRIBUTE.DARK.value)