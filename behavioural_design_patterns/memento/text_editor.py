'''
Description:

You are building a simple text editor.

Users can type text and save snapshots (mementos) at any point.

Users can undo to previous snapshots or redo undone snapshots.

The editor does not store commands, only states.
'''

#memento -which actually stores originality of state
class Memento():
    def __init__(self,state):
        self._state=state
    def get_state(self):
        return self._state

#originator - It is an object for which we want to maintain history
class TextEditor():
    def __init__(self):
        self._content=""
    
    def write(self,text):
        self._content+=text 
    
    def show(self):
        print(self._content)
    def save(self):
        return Memento(self._content)
    def restore(self,memento):
        self._content=memento.get_state()

#caretaker  - stores /manages list of states
class History():
    def __init__(self):
        self._mementos=[] 
    def add(self,memento):
        self._mementos.append(memento)
    def undo(self):
        if self._mementos:
            return self._mementos.pop()
        return None


# ======== Client Code ========
if __name__ == "__main__":
    editor = TextEditor()
    history = History()

    # Write initial text
    editor.write("Hello")
    history.add(editor.save())
    editor.show()  # Hello

    # Append more text
    editor.write(" World")
    history.add(editor.save())
    editor.show()  # Hello World

    # Undo last action
    memento = history.undo()
    if memento:
        editor.restore(memento)
    editor.show()  # Hello World

    # Undo again
    memento = history.undo()
    if memento:
        editor.restore(memento)
    editor.show()  # Hello

