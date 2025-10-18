"""
You are building a file explorer system (like Windows Explorer or Linux Nautilus).
In this system,

a file is a single object,

a folder can contain multiple files or other folders.

You want to perform operations like show_details() or get_size()
uniformly — whether it’s a file or a folder — without caring what type it is.
"""

#Tree like structure problems can be designed using this

from abc import ABC,abstractmethod
class FileSystem(ABC):
    @abstractmethod
    def show_details(self):
        pass 

#leaf 
class File(FileSystem):
    def __init__(self,name,size):
        self.name=name
        self.size=size
    
    def show_details(self,indent):
        print(" "*indent + "File :",self.name,":",self.size,"KB")


#composite 
class Folder(FileSystem):
    def __init__(self,name):
        self.name=name 
        self.contents=[] #files or folders 
    
    def add(self,item:FileSystem):
        self.contents.append(item)
    
    def remove(self,item:FileSystem):
        self.contents.remove(item)
    
    def show_details(self,indent=0):
        print(" "*indent + f"Folder: {self.name}")
        for child in self.contents:
            child.show_details(indent+4)  


#client code
if __name__ == "__main__":
    # Create files
    file1 = File("resume.pdf", 120)
    file2 = File("photo.png", 250)
    file3 = File("notes.txt", 50)

    # Create folders
    work_folder = Folder("Work")
    personal_folder = Folder("Personal")
    root_folder = Folder("Root")

    # Build structure
    work_folder.add(file1)
    personal_folder.add(file2)
    personal_folder.add(file3)
    root_folder.add(work_folder)
    root_folder.add(personal_folder)

    # Display full structure
    root_folder.show_details()

