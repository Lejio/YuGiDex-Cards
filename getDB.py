from urllib import request

class userUpdate:

    def __init__(self, db_name: str, location: str):
        # db_name test = testing.db
        # location = test.db
        print("\nDownloading..")
        r = request.urlretrieve(f"https://geneni.info/{db_name}.db", f"{location}")
        print("Completed.")