
''''
Statement: Design a word processor, where each font,size are same for all . 

'''


class CharacterFlyWeight:
    def __init__(self,letter,font,size):
        self.letter = letter
        self.font = font
        self.size = size
    
    def display(self,x,y):
        print(f"Displaying {self.letter} with font of {self.font} and with size of {self.size} at position {x},{y}.................")


#factory to store cache 
class CharacterFactory:
    _cache = {}
    @staticmethod
    def get_character(letter,font,size):
        key=(letter,font,size)
        if key not in CharacterFactory._cache:
            CharacterFactory._cache[key] = CharacterFlyWeight(letter,font,size)

        return CharacterFactory._cache[key]


#client code 
if __name__ == "__main__":
    text = "Hello Hello"
    row=0

    for col,ch in enumerate(text):
        char_obj = CharacterFactory.get_character(ch,"Arial",12) #font, size are intrinsic - shares among objects
        char_obj.display(row,col)
        

    print(f"\nTotal flyweights created: {len(CharacterFactory._cache)}")



