import webbrowser

class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, release_date):
        """Class created to contain all the attributes about the movies in the website
        'self' is not included in the arguments
        arguments:
        title (str): The title of the movie
        storyline (str): description of the movie
        poster_image (str): URL of the movie poster image
        trailer_youtube_url (str): URL of the movie trailer in youtube
        date (str): date the movie was released
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.date = release_date

    def show_trailer(self):
        """Opens the URL of the selected movie.
        'self' is not included in the arguments
        webbrowser.open: function imported with 'import webbrowser' to open URL on a web browser
        Input: None
        Behavior:  Opens a tab in the default web browser using trailer_youtube_url to the trailer of the movie selected
        Returns: None
        """
        webbrowser.open(self.trailer_youtube_url)
