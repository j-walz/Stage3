import webbrowser

class Movie():
      def __init__(self, title, storyline, poster, trailer, release_date, director):
          self.title = title
          self.storyline = storyline
          self.poster_image_url = poster
          self.trailer_youtube_url = trailer
          self.release_date = release_date
          self.director = director
      def show_trailer(self):
          webbrowser.open(self.trailer_youtube_url)