import webbrowser, omdb 
import fresh_tomatoes as ft

class Movie():
    def __init__(self, title, storyLine, poster, trailer):
        self.title = title
        self.poster = poster
        self.storyLine = storyLine
        self.trailer = trailer

    def showTrailer(self):
            webbrowser.open(self.trailer)
        
toyStory = Movie("Toy Story", "A cowboy doll is profoundly threatened and jealous when a new spaceman figure supplants him as top toy in a boy's room.", "https://m.media-amazon.com/images/M/MV5BMDU2ZWJlMjktMTRhMy00ZTA5LWEzNDgtYmNmZTEwZTViZWJkXkEyXkFqcGdeQXVyNDQ2OTk4MzI@._V1_SY1000_SX670_AL_.jpg", "https://www.youtube.com/watch?v=KYz2wyBy3kc")

schoolOfRock = Movie("School of Rock", "After being kicked out of his rock band, Dewey Finn becomes a substitute teacher of an uptight elementary private school, only to try and turn them into a rock band.", "https://m.media-amazon.com/images/M/MV5BMjEwOTMzNjYzMl5BMl5BanBnXkFtZTcwNjczMTQyMQ@@._V1_.jpg", "https://www.youtube.com/watch?v=XCwy6lW5Ixc")

# print(toyStory.title)
# toyStory.showTrailer()

movies = [toyStory, schoolOfRock]
ft.open_movies_page(movies)