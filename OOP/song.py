class Song:
    """Class to represent a song

    Attributes:
        title (str): The title of the song
        artist (Artist): An Artist object .
        duration (int): The duration of the song in seconds.
    """

    def __init__(self, title, artist, duration=None):
        """Song init method

        Args:
            title (str): Init the 'title' attribute.
            artist (Artist): At Artist object representing the song's
                            creator.
            duration ( Optional[int]: Init value of the 'duration' attribute.
                Will default to zero if not specified
        """
        self.title = title
        self.artist = artist
        self.duration = duration


class Album:
    """Class to represent an Album.

    Attributes:
        name (str): The name of the album.
        year (int): The year the albun was released.
        artist (Artist): The artist responsible for the album.
        If specified, the artist will default to an artist with
        the name "Various Artists".
        tracks (List [Song]): A list of of the tracks on the album.

    Methods:
        add_song: Use to add a new song to the album's track list.
        show_track_list: Use to show the album's track list.
    """
    def __init__(self, name, year, artist=None):
        self.name = name
        self.year = year

        if artist is None:
            self.artist = Artist("Various Artist")
        else:
            self.artist = artist

        self.tracks = []

    def add_song(self, song, position=None):
        """Adds a song to the track list.

        Args:
            song (Song): A song to add.
            position (Optional [int]): If specified, the song will be added
            to that position in the track list - inserting it between other songs if necessary.
            Otherwise, the song will be added to the end of the list.
        """
        if position is None:
            self.tracks.append(song)
        else:
            self.tracks.insert(position, song)

    def show_track_list(self):
        """Return album's the track list on request.
        """
        tracks = self.tracks

        return tracks


class Artist:
    """Basic class to store artist details.

    Attributes:
        name (str): The name of the artist.
        albums (List[Album]): A list of the albums by this artist.
            The list include only those albums in this collection, it is
            not an exhaustive list of the artist's published albums.

    Methods:
        add_album: Use to add a new album to the artist's album list.
        show_albums: Use to show the artist's album list.
    """
    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        """Add a new album to the list.

        Args:
            album (Album): Album object to add to the list.
                If the album is already presented, it will not added again
                (although this is yet to implemented).
        """
        self.albums.append(album)


def find_object(field, object_list):
    """Check 'object_list' to see if an object with a 'name' attribute equal
    to 'filed' exists, return it if so."""
    for item in object_list:
        if item.name == field:
            return item
    return None


def load_data():

    new_artist = None
    new_album = None
    artist_list = []

    with open('albums.txt', 'r') as albums:
        for line in albums:
            artist_field, album_field, year_field, song_field = tuple(line.strip('\n').split('\t'))
            year_field = int(year_field)
            print("{}:{}:{}:{}".format(artist_field, album_field, year_field, song_field))

            if new_artist is None:
                new_artist = Artist(artist_field)
                artist_list.append(new_artist)
            elif new_artist.name != artist_field:
                # We've lust read details for a new album
                # retrieve the artist object if there is one.
                # otherwise create a new artist object and add if to the artist list
                new_artist = find_object(artist_field, artist_list)
                if new_artist is None:
                    new_artist = Artist(artist_field)
                    artist_list.append(new_artist)

                # new_artist.add_album(new_album)
                # artist_list.append(new_artist)
                # new_artist = Artist(artist_field)
                # new_album = None

            if new_album is None:
                new_album = Album(album_field, year_field, new_artist)
                new_artist.add_album(new_album)
            elif new_album.name != album_field:
                new_album = find_object(album_field, new_artist.albums)
                if new_album is None:
                    new_album = Album(album_field, year_field, new_artist.albums)
                    new_artist.add_album(new_album)

            new_song = Song(song_field, new_artist)
            new_album.add_song(new_song)

    return artist_list


def create_check_file(artist_list):
    """Create a check file the object data for comparison with the original file"""
    with open('Check_file.txt', 'w') as check_file:
        for new_artist in artist_list:
            for new_album in new_artist.albums:
                for new_song in new_album.tracks:
                    print("{0.name}\t{1.name}\t{1.year}\t{2.title}".format(new_artist, new_album, new_song),
                          file=check_file)


if __name__ == "__main__":
    artist_list = load_data()
    print("There are {} artists".format(len(artist_list)))

    create_check_file(artist_list)
