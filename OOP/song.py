class Song:
    """Class to represent a song

    Attributes:
        title (str): The title of the song
        artist (Artist): An Artist object .
        duration (int): The duration of the song in seconds.
    """

    def __init__(self, title, artist, duration):
        """Song init method

        Args:
            title (str): Init the 'title' attribute.
            artist (Artist): At Artist object representing the song's
                            creator.
            duration ( Optional[int]: Init value of the 'duration' attribute.
                Will default to zero if not specified
        """
        self._title = title
        self._artist = artist
        self._duration = duration


class Album:
    """Class to represent an Album.

    Attributes:
        _album_name (str): The name of the album.
        _year (int): The year the albun was released.
        _artist (Artist): The artist responsible for the album.
        If specified, the artist will default to an artist with
        the name "Various Artists".
        _tracks (List [Song]): A list of of the tracks on the album.

    Methods:
        add_song: Use to add a new song to the album's track list.
        show_track_list: Use to show the album's track list.
    """
    def __init__(self, album_name, year, artist=None):
        self._album_name = album_name
        self._year = year

        if artist is None:
            self._artist = Artist("Various Artist")
        else:
            self._artist = artist

        self._tracks = []

    def add_song(self, song, position=None):
        """Adds a song to the track list.

        Args:
            song (Song): A song to add.
            position (Optional [int]): If specified, the song will be added
            to that position in the track list - inserting it between other songs if necessary.
            Otherwise, the song will be added to the end of the list.
        """
        if position is None:
            self._tracks.append(song)
        else:
            self._tracks.insert(position, song)

    def show_track_list(self):
        """Return album's the track list on request.
        """
        tracks = self._tracks

        return tracks


class Artist:
    """Basic class to store artist details.

    Attributes:
        _name (str): The name of the artist.
        _albums (List[Album]): A list of the albums by this artist.
            The list include only those albums in this collection, it is
            not an exhaustive list of the artist's published albums.

    Methods:
        add_album: Use to add a new album to the artist's album list.
        show_albums: Use to show the artist's album list.
    """
    def __init__(self, name):
        self._name = name
        self._albums = []

    def add_album(self, album):
        """Add a new album to the list.

        Args:
            album (Album): Album object to add to the list.
                If the album is already presented, it will not added again
                (although this is yet to implemented).
        """
        self._albums.append(album )


def load_data():

    new_artist = None
    new_album = None
    artist_list = []

    with open() as albums:
        for line in albums:
            artist_field, album_field, year_field, song_field = tuple(line.strip('\n').split('\t'))
            year_field = int(year_field)
            print(artist_field, album_field, year_field, song_field)


if __name__ == "__main__":
    load_data()
