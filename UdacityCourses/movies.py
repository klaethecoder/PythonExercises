import webbrowser, omdb

class Movie():
    def __init__(self, title, storyLine, poster, trailer):
        self.title = title
        self.poster = poster
        self.storyLine = storyLine
        self.trailer = trailer


def showTrailer(trailer):
            webbrowser.open(trailer)
        
toyStory = Movie("Toy Story", "A cowboy doll is profoundly threatened and jealous when a new spaceman figure supplants him as top toy in a boy's room.", "https://m.media-amazon.com/images/M/MV5BMDU2ZWJlMjktMTRhMy00ZTA5LWEzNDgtYmNmZTEwZTViZWJkXkEyXkFqcGdeQXVyNDQ2OTk4MzI@._V1_SY1000_SX670_AL_.jpg", "https://www.imdb.com/title/tt0114709/videoplayer/vi2052129305?ref_=tt_ov_vi")

print(toyStory.title)
showTrailer(toyStory.trailer)