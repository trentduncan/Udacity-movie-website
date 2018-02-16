
import webbrowser

class Movie():
    """This class provides a way to store movie related information"""
    VALID_RATINGS = ["G","PG","PG-13","R"]
    
    # The constructor that allows different instances of the class Movie to be created.
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, movie_rating):

        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        if movie_rating in self.VALID_RATINGS:
        	self.rating = movie_rating
        else:
        	self.rating = "Not a Valid Rating"
        

    # Function that takes the instance variable for youtube URL to open up the link in a webbrowser.
    def show_trailer(self):
    	webbrowser.open(self.trailer_youtube_url)
