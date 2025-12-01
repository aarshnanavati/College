# Create a Media base class and a Movie subclass with additional attributes such as genre and rating.
#  Add a method to recommend a movie based on rating and genre.

class Media:
    def __init__(self,title,year):
        self.__title = title
        self.__year = year

    def get_title(self):
        return self.__title

    def get_year(self):
        return self.__year
    
class Movie(Media):
    def __init__(self,title,year,genre,rating):
        super().__init__(title,year)
        self.__genre = genre
        self.__rating = rating

    def get_genre(self):
        return self.__genre
    
    def get_rating(self):
        return self.__rating
    
    def recommend_movie(self):
        if self.get_rating() >= 8.0:
            return f"Highly recommended : '{self.get_title()}' ({self.get_genre()}) -  rating: {self.get_rating()}"
        else:
            return f"Low Recommended : '{self.get_title()}' ({self.get_genre()}) - rating: {self.get_rating()}"
        
if __name__ == "__main__":
    print("Movie entry and recommendation system")

    movies = []
    n = int(input("Enter number of movies:"))

    for i in range(n):
        print("Enter details for movie",i+1)
        title = input("Enter title:")
        year = int(input("Enter year of release:"))
        genre = input("Enter genre:")
        rating = float(input("Enter rating (0-10):"))

        movie = Movie(title,year,genre,rating)
        movies.append(movie)

    print("\nMovie Recommendations:")
    for m in movies:
        print(m.recommend_movie())