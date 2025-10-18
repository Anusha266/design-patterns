"""
A user wants to download software.
We will build a Proxy layer that handles:

Virtual Proxy → Downloads the software only when needed (lazy loading).

Protection Proxy → Allows downloads only for authorized users.

Remote Proxy → Simulates downloading from a remote server.
"""
from time import sleep
#Real Subject
class Software:
    def __init__(self,name):
        self.name=name 
        print(f"Preparing {self.name} software package...")
    
    def download(self):
        print(f"Downloading {self.name} ...")
        sleep(1)
        print(f"{self.name} successfully downloaded!")

    
#=====proxy========
class SoftwareProxy:
    def __init__(self,software_name):
        self.software_name=software_name
        self._software=None 
    
    def has_access(self,user):
        if user.role in ['Admin','Premium']:
            return True
        return False
    
    def download(self,user):
        #protection proxy
        if not self.has_access(user):
            print("Request denied for downloading for user:",user.name)
            return
        
        #remote proxy (simulated) - logging before and after calling real object 
        print(f"connecting to remote server for {self.software_name}....")

        #caching/virtual proxy
        if self._software is None:
            print(f"Initializing software object...")
            self._software=Software(self.software_name)
        else:
            print("Using cached software...")
        
        print(f"Data received from remote server. Connection closing...")

        self._software.download()


#User object
class User:
    def __init__(self,name,role):
        self.name=name 
        self.role=role 
    

# ---- Demo ----
if __name__ == "__main__":
    proxy = SoftwareProxy("Chrome")

    user1 = User("Anusha", "Admin")
    user2 = User("Shivacharan", "Guest")

    print("\n--- Trying with admin user------------\n")
    proxy.download(user1)
    print("\n--- Trying again with same user (cached software) ---\n")
    proxy.download(user1)
    print("\n--- Trying with guest user ---\n")
    proxy.download(user2)


    proxy = SoftwareProxy("Adobe")

    user1 = User("Srinivas", "Guest")
    user2 = User("Ajay", "Premium")
    print("\n--- Trying with Guest user------------\n")
    proxy.download(user1)
    print("\n--- Trying with premium user------------\n")
    proxy.download(user2)


