"""The class representing the concept of playlist.
It includes a list of Song objects and the dates when the playlist was created and completed.
"""

from datetime import date, datetime, time
from util.utility import *
import json

# from music.song import Song
# from util.utility import format_date


class Playlist:
    """The class representing the concept of playlist.
    It includes a list of Song objects and the dates when the playlist was created and completed.
    """

    # Class variables: much like static fields in Java; typically defined and initialized before __init__()
    # Insert one or more class variables (static fields), such as phrases used in __str__(), date_pattern,...

    play_me = 'Play me :)'

    def __init__(self, name, *songs, created=date.today(), completed=date.today()):
        self.name = name
        self.songs = songs
        self.created = created
        self.completed = completed
        # pass                                            # introduce and initialize iterator counter, self.__i

    def __str__(self):
        n = self.name
        s = '; '.join([str(s) for s in self.songs]) if self.songs else '(empty)'
        from_to = format_date(self.created) + ' - ' + format_date(self.completed)
        return '\n'.join([n, s, from_to])

    def __eq__(self, other):
        return self.__dict__ == other.__dict__ if type(self) is type(other) else False

    @staticmethod
    def is_date_valid(d):
        """It is assumed that a playlist has not been created more than ~10 years ago.
        So, the valid date to denote the creation of a playlist is between Jan 01, 2011, and today.
        """
        return date(2011, 1, 1) <= d <= date.today()

    @staticmethod
    def parse_playlist_str(playlist_str):
        """Splits a playlist string into its typical segments.
        """

        l1, l2, l3 = playlist_str.split('\n')
        name = l1
        songs = [Song.from_str(s) for s in l2.split('; ')] if l2 != '(empty)' else []
        created, completed = [datetime.strptime(d, PREFERRED_DATE_FORMAT).date() for d in l3.split(' - ')]
        return name, songs, created, completed

    # Alternative constructor
    @classmethod
    def from_playlist_str(cls, playlist_str):
        name, songs, created, completed = Playlist.parse_playlist_str(playlist_str)
        return cls(name, *songs, created=created, completed=completed)

    def __iter__(self):
        """Once __iter__() and __next__() are implemented in a class,
        we can create an iterator object by calling the iter() built-in function on an object of the class,
        and then call the next() built-in function on that object.
        It is often sufficient to just return self in __iter__(),
        if the iterator counter such as self.__i is introduced and initialized in __init__().
        Alternatively, the iterator counter (self.__i) is introduced and initialized  here.
        """

        self.__i = 0
        return self
        # return self               # sufficient if the iterator counter is introduced and initialized in __init__()

    def __next__(self):
        if self.__i < len(self.songs):
            s = self.songs[self.__i]
            self.__i += 1
            return s
        else:
            raise StopIteration


def next_song(playlist):
    """Generator that shows the songs from a playlist, one at a time.
    yield produces a generator object, on which we call the next() built-in function.
    A great tutorial on generators: https://realpython.com/introduction-to-python-generators/.
    """

    for s in playlist:
        input('Next: ')
        yield s
        print('Yeah!')


class PlaylistEncoder(json.JSONEncoder):
    """JSON encoder for Playlist objects (cls= parameter in json.dumps()).
    """

    def default(self, playlist):
        # recommendation: always use double quotes with JSON

        pass


def playlist_py_to_json(playlist):
    """JSON encoder for Playlist objects (default= parameter in json.dumps()).
    """


def playlist_json_to_py(playlist_json):
    """JSON decoder for Playlist objects (object_hook= parameter in json.loads()).
    """


if __name__ == "__main__":

    from testdata.songs import *

    # Class variables (like static fields in Java; typically defined and initialized before __init__())
    print(Playlist.play_me)
    print()

    # Check the basic methods (__init__(), __str__(),...)
    pl = Playlist('My songs', *[across_the_universe, imagine, happiness_is_a_warm_gun, love],
                  created=date(2020, 2, 13), completed=date.today())
    print(pl)
    print()

    # Check date validator (@staticmethod is_date_valid(<date>))
    print(Playlist.is_date_valid(date(1971, 10, 11)))
    print(Playlist.is_date_valid(date(2018, 10, 11)))
    print()

    # Check the alternative constructor (@classmethod from_playlist_str(<playlist_str>))
    pls = pl.__str__()
    print(Playlist.from_playlist_str(pls))
    print(pl == Playlist.from_playlist_str(pls))
    print()

    # Check the iterator
    i = iter(pl)
    while True:
        try:
            print(next(i))
        except StopIteration:
            break
    print()

    # Repeated attempt to run the iterator fails, because the iterator is exhausted
    i = iter(pl)
    print(next(i))

    # Demonstrate generators
    # next_s = next_song(pl)
    # while True:
    #     try:
    #         print(next(next_s))
    #     except StopIteration:
    #         break
    # print()
    #
    # # Repeated attempt to run the generator fails, because the generator is exhausted
    #
    # next_s = next_song(pl)
    # print(next(next_s))
    print()

    # Demonstrate generator expressions
    e = (i**2 for i in [1, 2, 3])
    print(e)
    print(next(e))
    print(next(e))
    print(next(e))
    # print(next(e))
    print()

    # Demonstrate JSON encoding/decoding of Playlist objects
    # Single object
    print()

    # List of objects
    print()


