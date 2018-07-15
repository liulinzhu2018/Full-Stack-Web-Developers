import webbrowser


class Movie():
    """ Movie class is used to save movies' information and show trailer."""
    VAILD_RATINGS = ['G', 'PG', 'PG-13', 'R']

    """ construct function

        Prameters
        ---------
        arg1 : str
            movie title
        arg2 : str
            movie storyline
        arg3 : str
            poster image
        arg4 : str
            trailer youtobe url

        Returns
        -------
        none
    """
    def __init__(
                self,
                movie_title,
                movie_storyline,
                poster_image,
                trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    """show trailer"""
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
