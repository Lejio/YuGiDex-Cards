from dexConnector import YuGiDexDB
from YuGiDex_Language.Classifier import Classifier
from YuGiDex_Language.Language import SupportedLanguages

from urllib import request


if __name__ == "__main__":

    db_name = "yugidbEN.db"
    
    r = request.urlretrieve(f"https://geneni.info/yugidexdb/{db_name}", db_name)
    db = YuGiDexDB(db_name)
    print(db.search('name', 'Blue-Eyes'))
    