"""
You don’t want to open a DB connection at startup — only when the app actually needs it.

"""

class DataBaseConnection:
    _instance = None
     
    
    def __init__(self): 
        print("connecting to Database")

    
    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls() # global access through the get_instance() method only.

        return cls._instance
    
    def query(self,sql):
        print("executing query....",sql)


# ---- Client Code ----
if __name__ == "__main__":
    db1 = DataBaseConnection.get_instance()
    db2 = DataBaseConnection.get_instance()
    print(db1 is db2)  # True
    db1.query("SELECT * FROM users")


'''
Multiple threads might create objects simultaneously...always it may not be needed ..consider logging system...so double locking comes into picture here.
'''