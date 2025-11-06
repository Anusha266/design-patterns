'''
Your app has a configuration file (config.json) with global settings (DB URL, API keys).
You only want it read once at program startup.

Because you will be using those across the project , so everytime you dont want to read from file again.

'''

import json
class ConfigManager:
    _instance = None
     
    def __init__(self):
        self.load()
    
    def load(self):
        with open("config.json","r") as f:  # Here configuration might be fetched from other API or from remote then this pattern will highly useful , not to fetch everytime from remote
            self.config = json.load(f)

    @staticmethod
    def get_instance():
        return ConfigManager._instance


#Eager initialization - creating at load time 
ConfigManager._instance = ConfigManager()

#client code 

if __name__=="__main__":
    c1= ConfigManager.get_instance()
    c2= ConfigManager.get_instance()
    print(c1 is c2)
    print(c1.config)
    c1.load()



