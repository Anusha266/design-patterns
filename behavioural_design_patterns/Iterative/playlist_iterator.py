""" 
Scenario: Playlist Iterator

Problem:
You are building a music player. A Playlist contains multiple songs.
You want to iterate over the songs alternatively without exposing the internal list of songs.

Key Points:

The Playlist is the collection.

The SongIterator is the iterator that knows how to traverse the Playlist.

You can have multiple iterators on the same playlist if needed.

"""
from abc import ABC,abstractmethod
class Song(ABC):
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return f"playing {self.name}..."
    

class SongIterator():
    def __init__(self,songs):
        self._songs=songs
        self._index=0
    
    def __iter__(self):
        return self
    def __next__(self):
        if self._index<len(self._songs):
            song= self._songs[self._index]
            self._index+=2
            return song 
        else:
            raise StopIteration
        
    
#playlists can be made 
#song Iterable
class SongCollection():
    def __init__(self):
        self._songs=[]
    
    def add_song(self,song):
        self._songs.append(song)
    def __iter__(self):
        return SongIterator(self._songs)

if __name__=='__main__':
    playlist1 = SongCollection()
    playlist1.add_song(Song("song1"))
    playlist1.add_song(Song("song2"))
    playlist1.add_song(Song("song3"))
    playlist1.add_song(Song("song4"))
    playlist1.add_song(Song("song5"))

    for song in playlist1:
        print(song)
    
    playlist2= SongCollection()
    playlist2.add_song(Song("song3"))
    for song in playlist2:
        print(song)

    

