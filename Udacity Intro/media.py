     # -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 16:05:13 2018

@author: orpha
"""
from webbrowser import open as web_open

class Movie():
    """This class is provided by Udacity in a tutorial for learning Object Oriented Programming in Python.
    This class stores some information about a given movie."""
    VALID_RATINGS = ['G', 'PG', 'PG-13', 'R']
    def __init__(self,
               movie_title,
               movie_storyline,
               poster_image,
               trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
    def tell_me_your_name(self):
        print(self.title)
    def show_trailer(self):
        web_open(self.trailer_youtube_url)
        
bladerunner = Movie('Blade Runner',
                    '"I need more life, f......"',
                    'https://images-na.ssl-images-amazon.com/images/I/51I74ym0DrL.jpg',
                    'https://www.youtube.com/watch?v=eogpIG53Cis')

bladerunner.storyline
bladerunner.__dict__
#getattr(bladerunner, )
dir(bladerunner)
bladerunner.tell_me_your_name()
[(s, type(eval('bladerunner.{0}'.format(s)))) for s in dir(bladerunner) if callable(eval('bladerunner.{0}'.format(s)))]

#bladerunner.show_trailer()

#import fresh_tomatoes
Movie.VALID_RATINGS
bladerunner.VALID_RATINGS
Movie.__doc__
bladerunner.__doc__
bladerunner.__module__
bladerunner.__name__ # Class instance has no attribute '__name__'
Movie.__name__ # Base class has attribute '__name__'


def foo():
    """Testing functionalities..."""
foo.__doc__
foo.__module__
foo.__name__ # Arbitrary function has __name__
#fresh_tomatoes.open_movies_page([bladerunner])

a_list = [1,2,3]
a_list.__repr__
