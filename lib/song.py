class Song:
    pass
class Song:
    # Class attributes to maintain global library insights
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artists_count = {}
    
    # Alias attribute specifically included to satisfy the song_test.py suite
    artist_count = {}

    def __init__(self, name, artist, genre):
        # Initialize instance attributes
        self.name = name
        self.artist = artist
        self.genre = genre
        
        # Automatically trigger class-level updates upon instantiation
        self.add_song_to_count()
        self.add_to_genres(genre)
        self.add_to_artists(artist)
        self.add_to_genre_count(genre)
        self.add_to_artists_count(artist)

    @classmethod
    def add_song_to_count(cls):
        """Increments the global count of all created songs by 1."""
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        """Appends a new genre to the global list, ensuring uniqueness."""
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        """Appends a new artist to the global list, ensuring uniqueness."""
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        """Tracks the frequency of songs belonging to each genre."""
        cls.genre_count[genre] = cls.genre_count.get(genre, 0) + 1

    @classmethod
    def add_to_artists_count(cls, artist):
        """Tracks the frequency of songs associated with each artist."""
        # Updates both the README-specified dictionary and the test-suite-specified dictionary
        cls.artists_count[artist] = cls.artists_count.get(artist, 0) + 1
        cls.artist_count[artist] = cls.artist_count.get(artist, 0) + 1