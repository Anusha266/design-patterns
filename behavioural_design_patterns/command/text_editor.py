''' 
We are building a Text Editor with the following operations:

Copy text

Paste text

Undo last action

Redo last undone action

cut text

Key Idea:
Each operation will be encapsulated as a Command object. The editor (Invoker) triggers commands without knowing the details of the operation.
'''

#========Implementation==================
'''
Invoker: editor 
concrete commands: copy, paste, undo, redo, save 
Receiver: Document
'''

from abc import ABC,abstractmethod

#=====================Receiver====================
class Document:
    def __init__(self):
        self.content = ""
        self.clipboard=""

    def insert(self,text,pos):
        self.content=self.content[:pos]+text+self.content[pos:]
    
    def delete(self,start,end):
        deleted=self.content[start:end]
        self.content = self.content[:start]+self.content[end:]
        return deleted
    
    def cut(self,start,end):
        self.clipboard=self.content[start:end]
        return self.delete(start,end)

    def copy(self,start,end):
        self.clipboard=self.content[start:end]
    
    def paste(self,start):
        if self.clipboard:
            self.insert(self.clipboard,start)
    
    def __str__(self):
        return self.content
    
#=======================command interface==================
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass 
    def undo(self):
        pass 

#=========================concrete commands===============

class InsertCommand(Command):
    def __init__(self,receiver,text,pos):
        self.receiver = receiver
        self.text=text
        self.pos=pos
    def execute(self):
        self.receiver.insert(self.text,self.pos)
    def undo(self):
        self.receiver.delete(self.pos,self.pos+len(self.text))

class DeleteCommand(Command):
    def __init__(self,receiver,start,end):
        self.receiver=receiver 
        self.start=start
        self.end=end 
        self.deleted=""
    
    def execute(self):
        self.deleted=self.receiver.delete(self.start,self.end)

    def undo(self):
        self.receiver.insert(self.deleted,self.start)

class CopyCommand(Command):
    def __init__(self,receiver,start,end):
        self.receiver = receiver 
        self.start=start
        self.end=end

    def execute(self):
        self.receiver.copy(self.start,self.end)
        
    def undo(self):
        pass #nothing effected with undo for copy
    

class PasteCommand(Command):
    def __init__(self,receiver,pos):
        self.receiver = receiver 
        self.pasted_text=""
        self.pos=pos
    
    def execute(self):
        self.pasted_text=self.receiver.clipboard
        self.receiver.paste(self.pos)
    
    def undo(self):
        start = self.pos
        end = start + len(self.pasted_text)
        self.receiver.delete(start, end)

class CutCommand(Command):
    def __init__(self,receiver,start,end):
        self.receiver=receiver
        self.start=start
        self.end=end 
        self.cut_text=""
    
    def execute(self):
        self.cut_text = self.receiver.cut(self.start,self.end)
    
    def undo(self):
        self.receiver.insert(self.cut_text,self.start)


#===========Invoker =============Editor 
class Editor():
    def __init__(self):
        self.undo_stack = []
        self.redo_stack =[]

    def execute_command(self,command):
        command.execute()
        self.undo_stack.append(command)

    def undo(self):
        if not self.undo_stack:
            print("Nothing to undone.....")
            return
        command = self.undo_stack.pop()
        command.undo()
        self.redo_stack.append(command)

    def redo(self):
        if not self.redo_stack:
            print("Nothing to redo...")
            return 
        command = self.redo_stack.pop()
        command.execute()
        self.undo_stack.append(command)


#client code    
if __name__ == "__main__":
    doc = Document()
    editor = Editor()

    # 1. Insert initial text
    editor.execute_command(InsertCommand(doc, "Hello", 0))
    editor.execute_command(InsertCommand(doc, " World", len(doc.content)))
    print("After insert:", doc)

    # 2. Copy 'Hello'
    editor.execute_command(CopyCommand(doc, 0, 5))

    # 3. Paste at end
    editor.execute_command(PasteCommand(doc, len(doc.content)))
    print("After copy paste at end:", doc)

    # 4. Cut 'World'
    editor.execute_command(CutCommand(doc, 6, 11))
    print("After cut World:", doc)
    print("Clipboard:", doc.clipboard)

    # 5. Paste 'World' at beginning
    editor.execute_command(PasteCommand(doc, 0))
    print("After paste at beginning:", doc)

    # 6. Delete 'Hello' in the middle
    editor.execute_command(DeleteCommand(doc, 5, 10))
    print("After delete Hello in middle:", doc)

    # 7. Undo last three actions
    editor.undo()
    editor.undo()
    editor.undo()
    print("After 3 undos:", doc)

    # 8. Redo last two actions
    editor.redo()
    editor.redo()
    print("After 2 redos:", doc)

    # 9. Insert '!!!' at end
    editor.execute_command(InsertCommand(doc, "!!!", len(doc.content)))
    print("After insert exclamation:", doc)

    # 10. Undo all actions
    while editor.undo_stack:
        editor.undo()
    print("After undoing all:", doc)

    # 11. Redo all actions again
    while editor.redo_stack:
        editor.redo()
    print("After redoing all:", doc)


'''
Learnings:

Invoker dont stores command object as self variable..it will be passed in execute method. It executes undo and redo. 

each receiver will perform all commands business logic. 

command will have execute and undo methods. (mainly for undo methods , command isolated )

'''
        



        
        
    

